"""RAG utilities for SkillOS: chunking, embedding, FAISS index build and query.

Index layout on S3:
  s3://{bucket}/rag/notes.faiss  — FAISS flat IP index (float32 vectors)
  s3://{bucket}/rag/chunks.json  — parallel list of chunk metadata dicts

Configuration (env vars):
  RAG_CHUNK_SIZE       default 500  — max chars per chunk
  RAG_CHUNK_OVERLAP    default 100  — overlap between consecutive chunks
  RAG_TOP_K            default 5    — number of chunks returned per query
  RAG_EMBEDDING_MODEL  default amazon.titan-embed-text-v2:0
"""
from __future__ import annotations

import io
import json
import os
import tempfile
from typing import Optional

import boto3
import numpy as np

_DEFAULT_EMBEDDING_MODEL = "amazon.titan-embed-text-v2:0"
_FAISS_KEY = "rag/notes.faiss"
_CHUNKS_KEY = "rag/chunks.json"

# Module-level index cache to reuse across Lambda warm invocations
_cached_index = None
_cached_chunks: Optional[list[dict]] = None
_cached_bucket: Optional[str] = None


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------

def chunk_text(text: str, path: str, chunk_size: int = 500, overlap: int = 100) -> list[dict]:
    """Split text into overlapping character-level chunks."""
    chunks: list[dict] = []
    start = 0
    idx = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk_text_ = text[start:end].strip()
        if chunk_text_:
            chunks.append({"text": chunk_text_, "path": path, "chunk_idx": idx})
        start += chunk_size - overlap
        idx += 1
    return chunks


# ---------------------------------------------------------------------------
# Embedding
# ---------------------------------------------------------------------------

def _embed_batch(texts: list[str], model_id: str, bedrock_client) -> list[list[float]]:
    """Embed a batch of texts using Bedrock Titan Embeddings."""
    vectors: list[list[float]] = []
    for text in texts:
        body = json.dumps({"inputText": text[:8192]})
        resp = bedrock_client.invoke_model(
            modelId=model_id,
            body=body,
            contentType="application/json",
            accept="application/json",
        )
        result = json.loads(resp["body"].read())
        vectors.append(result["embedding"])
    return vectors


def _get_bedrock_client():
    region = os.environ.get("BEDROCK_REGION", os.environ.get("AWS_REGION", "us-east-1"))
    return boto3.client("bedrock-runtime", region_name=region)


# ---------------------------------------------------------------------------
# Index build (called by rag_indexer Lambda)
# ---------------------------------------------------------------------------

def build_index(
    notes: dict[str, str],
    s3_bucket: str,
    chunk_size: Optional[int] = None,
    overlap: Optional[int] = None,
    embedding_model: Optional[str] = None,
) -> int:
    """Build a FAISS index from a dict of {path: content} and upload to S3.

    Args:
        notes: mapping of GitHub path → file content
        s3_bucket: S3 bucket name for storing the index
        chunk_size, overlap, embedding_model: override env-var defaults

    Returns:
        Number of chunks indexed.
    """
    import faiss  # type: ignore

    chunk_size = chunk_size or int(os.environ.get("RAG_CHUNK_SIZE", "500"))
    overlap = overlap or int(os.environ.get("RAG_CHUNK_OVERLAP", "100"))
    model_id = embedding_model or os.environ.get("RAG_EMBEDDING_MODEL", _DEFAULT_EMBEDDING_MODEL)
    bedrock = _get_bedrock_client()

    all_chunks: list[dict] = []
    for path, content in notes.items():
        all_chunks.extend(chunk_text(content, path, chunk_size, overlap))

    if not all_chunks:
        return 0

    texts = [c["text"] for c in all_chunks]
    vectors = _embed_batch(texts, model_id, bedrock)
    matrix = np.array(vectors, dtype=np.float32)

    dim = matrix.shape[1]
    index = faiss.IndexFlatIP(dim)  # inner-product (cosine after normalisation)
    faiss.normalize_L2(matrix)
    index.add(matrix)

    # Serialise FAISS index to bytes
    with tempfile.NamedTemporaryFile(suffix=".faiss", delete=False) as tmp:
        faiss.write_index(index, tmp.name)
        with open(tmp.name, "rb") as f:
            index_bytes = f.read()

    s3 = boto3.client("s3")
    s3.put_object(Bucket=s3_bucket, Key=_FAISS_KEY, Body=index_bytes)
    s3.put_object(
        Bucket=s3_bucket,
        Key=_CHUNKS_KEY,
        Body=json.dumps(all_chunks, ensure_ascii=False).encode(),
        ContentType="application/json",
    )

    # Invalidate module-level cache so next query loads fresh index
    global _cached_index, _cached_chunks, _cached_bucket
    _cached_index = None
    _cached_chunks = None
    _cached_bucket = None

    return len(all_chunks)


# ---------------------------------------------------------------------------
# Index query (called at intake time)
# ---------------------------------------------------------------------------

def _load_index(s3_bucket: str):
    """Download and cache the FAISS index and chunk metadata from S3."""
    import faiss  # type: ignore

    global _cached_index, _cached_chunks, _cached_bucket

    if _cached_index is not None and _cached_bucket == s3_bucket:
        return _cached_index, _cached_chunks

    s3 = boto3.client("s3")
    idx_resp = s3.get_object(Bucket=s3_bucket, Key=_FAISS_KEY)
    idx_bytes = idx_resp["Body"].read()

    with tempfile.NamedTemporaryFile(suffix=".faiss", delete=False) as tmp:
        tmp.write(idx_bytes)
        tmp_path = tmp.name
    index = faiss.read_index(tmp_path)

    chunks_resp = s3.get_object(Bucket=s3_bucket, Key=_CHUNKS_KEY)
    chunks: list[dict] = json.loads(chunks_resp["Body"].read())

    _cached_index = index
    _cached_chunks = chunks
    _cached_bucket = s3_bucket
    return index, chunks


def query_notes(query: str, s3_bucket: str, top_k: int = 5) -> list[dict]:
    """Embed a query and return top-k relevant note chunks.

    Returns a list of dicts with keys: text, source (path), score, chunk_idx.
    Raises an exception if the index does not exist on S3 (caller should catch).
    """
    import faiss  # type: ignore

    model_id = os.environ.get("RAG_EMBEDDING_MODEL", _DEFAULT_EMBEDDING_MODEL)
    bedrock = _get_bedrock_client()

    index, chunks = _load_index(s3_bucket)

    query_vecs = _embed_batch([query], model_id, bedrock)
    query_matrix = np.array(query_vecs, dtype=np.float32)
    faiss.normalize_L2(query_matrix)

    scores, indices = index.search(query_matrix, top_k)
    results: list[dict] = []
    for rank, (score, i) in enumerate(zip(scores[0], indices[0])):
        if i < 0:
            continue
        chunk = chunks[i]
        results.append({
            "text": chunk["text"],
            "source": chunk["path"],
            "score": float(score),
            "chunk_idx": chunk.get("chunk_idx", rank),
        })
    return results
