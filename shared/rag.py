"""RAG utilities for SkillOS: chunking, embedding, S3 Vectors index upsert and query.

Index layout:
  S3 Vector Bucket: var.rag_vector_bucket
    Index name: "notes"
    Vector keys: "{sha256(path)[:8]}-{chunk_idx}"
    Metadata per vector: {"text": ..., "path": ..., "chunk_idx": ...}

  S3 State Bucket: {S3_BUCKET}/rag/file_hashes.json
    {"notes/foo.md": "<sha256>", ...}  — used for incremental diffing

Configuration (env vars):
  RAG_CHUNK_SIZE       default 500  — max chars per chunk
  RAG_CHUNK_OVERLAP    default 100  — overlap between consecutive chunks
  RAG_TOP_K            default 5     — number of chunks returned per query
  RAG_EMBEDDING_MODEL  default amazon.titan-embed-text-v2:0
  RAG_EMBED_SLEEP      default 0.25  — seconds between Titan calls; set to 0 for bulk indexing
  VECTOR_BUCKET        — S3 Vectors vector bucket name
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from typing import Optional

import boto3
from botocore.exceptions import ClientError

_DEFAULT_EMBEDDING_MODEL = "amazon.titan-embed-text-v2:0"
_VECTOR_INDEX_NAME = "notes"
_HASHES_KEY = "rag/file_hashes.json"


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

def _embed_one(text: str, model_id: str, bedrock_client) -> list[float]:
    """Embed a single text with exponential backoff on throttling.

    botocore retries are disabled on this client (max_attempts=1) so our
    backoff loop has full control over retry timing.
    """
    body = json.dumps({"inputText": text[:8192]})
    for attempt in range(8):
        try:
            resp = bedrock_client.invoke_model(
                modelId=model_id,
                body=body,
                contentType="application/json",
                accept="application/json",
            )
            # Steady-state delay to stay under Titan's per-second quota.
            # Set RAG_EMBED_SLEEP=0 for bulk/initial indexing runs (throttles handled by backoff).
            sleep_s = float(os.environ.get("RAG_EMBED_SLEEP", "0.25"))
            if sleep_s > 0:
                time.sleep(sleep_s)
            return json.loads(resp["body"].read())["embedding"]
        except Exception as e:
            code = ""
            if hasattr(e, "response"):
                code = e.response.get("Error", {}).get("Code", "")
            import logging as _log
            _log.getLogger().warning("embed attempt=%d code=%r type=%s", attempt, code, type(e).__name__)
            if code in ("ThrottlingException", "TooManyRequestsException") and attempt < 7:
                wait = min(2 ** attempt + 1, 60)
                _log.getLogger().info("throttled — sleeping %ds", wait)
                time.sleep(wait)
                continue
            raise


def _embed_batch(texts: list[str], model_id: str, bedrock_client) -> list[list[float]]:
    """Embed a batch of texts using Bedrock Titan Embeddings."""
    return [_embed_one(t, model_id, bedrock_client) for t in texts]


_rag_bedrock_client = None
_rag_bedrock_expiry = None


def _get_bedrock_client():
    """Return a bedrock-runtime client, optionally via cross-account assume-role.

    Mirrors the pattern in shared/llm.py but returns a plain boto3 client
    (not a LangChain wrapper) with botocore retries disabled so our backoff
    loop owns all retry logic.
    """
    from botocore.config import Config
    from datetime import datetime, timezone

    global _rag_bedrock_client, _rag_bedrock_expiry

    cfg = Config(retries={"max_attempts": 1, "mode": "standard"})
    region = os.environ.get("BEDROCK_REGION", os.environ.get("AWS_REGION", "us-east-1"))
    role_arn = os.environ.get("BEDROCK_ASSUME_ROLE_ARN", "")

    if not role_arn:
        return boto3.client("bedrock-runtime", region_name=region, config=cfg)

    # Cross-account: cache creds per container, refresh 60s before expiry
    now = datetime.now(timezone.utc)
    if _rag_bedrock_client is not None and _rag_bedrock_expiry is not None:
        if (_rag_bedrock_expiry - now).total_seconds() > 60:
            return _rag_bedrock_client

    session_name = os.environ.get("BEDROCK_ASSUME_ROLE_SESSION_NAME", "skillos-rag-session")
    external_id = os.environ.get("BEDROCK_ASSUME_ROLE_EXTERNAL_ID", "")

    assume_kwargs: dict = {"RoleArn": role_arn, "RoleSessionName": session_name}
    if external_id:
        assume_kwargs["ExternalId"] = external_id

    creds = boto3.client("sts").assume_role(**assume_kwargs)["Credentials"]

    _rag_bedrock_client = boto3.client(
        "bedrock-runtime",
        region_name=region,
        aws_access_key_id=creds["AccessKeyId"],
        aws_secret_access_key=creds["SecretAccessKey"],
        aws_session_token=creds["SessionToken"],
        config=cfg,
    )
    _rag_bedrock_expiry = creds["Expiration"]
    return _rag_bedrock_client


def _get_s3vectors_client():
    region = os.environ.get("AWS_REGION", "us-east-1")
    return boto3.client("s3vectors", region_name=region)


# ---------------------------------------------------------------------------
# Stable chunk key: deterministic across re-runs
# ---------------------------------------------------------------------------

def _chunk_key(path: str, chunk_idx: int) -> str:
    return f"{hashlib.sha256(path.encode()).hexdigest()[:8]}-{chunk_idx}"


# ---------------------------------------------------------------------------
# Hash map helpers (incremental diff)
# ---------------------------------------------------------------------------

def _load_hashes(s3_bucket: str) -> dict[str, str]:
    s3 = boto3.client("s3")
    try:
        resp = s3.get_object(Bucket=s3_bucket, Key=_HASHES_KEY)
        return json.loads(resp["Body"].read())
    except s3.exceptions.NoSuchKey:
        return {}
    except Exception:
        return {}


def _save_hashes(s3_bucket: str, hashes: dict[str, str]) -> None:
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=s3_bucket,
        Key=_HASHES_KEY,
        Body=json.dumps(hashes, ensure_ascii=False).encode(),
        ContentType="application/json",
    )


def _file_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()


# ---------------------------------------------------------------------------
# Index upsert (called by rag_indexer Lambda)
# ---------------------------------------------------------------------------

def upsert_index(
    notes: dict[str, str],
    s3_bucket: str,
    vector_bucket: str,
    chunk_size: Optional[int] = None,
    overlap: Optional[int] = None,
    embedding_model: Optional[str] = None,
) -> dict:
    """Incrementally upsert vectors into S3 Vectors for changed/new/deleted notes.

    Args:
        notes: mapping of GitHub path → file content (current state)
        s3_bucket: S3 bucket for storing file_hashes.json
        vector_bucket: S3 Vectors vector bucket name
        chunk_size, overlap, embedding_model: override env-var defaults

    Returns:
        Stats dict with keys: files_added, files_updated, files_deleted, chunks_upserted, chunks_deleted, files_skipped
    """
    chunk_size = chunk_size or int(os.environ.get("RAG_CHUNK_SIZE", "500"))
    overlap = overlap or int(os.environ.get("RAG_CHUNK_OVERLAP", "100"))
    model_id = embedding_model or os.environ.get("RAG_EMBEDDING_MODEL", _DEFAULT_EMBEDDING_MODEL)
    bedrock = _get_bedrock_client()
    s3v = _get_s3vectors_client()

    stored_hashes = _load_hashes(s3_bucket)
    current_paths = set(notes.keys())
    stored_paths = set(stored_hashes.keys())

    deleted_paths = stored_paths - current_paths
    changed_paths = {
        path for path in current_paths
        if _file_hash(notes[path]) != stored_hashes.get(path)
    }
    skipped = len(current_paths) - len(changed_paths)

    stats = {
        "files_added": len(changed_paths - stored_paths),
        "files_updated": len(changed_paths & stored_paths),
        "files_deleted": len(deleted_paths),
        "chunks_upserted": 0,
        "chunks_deleted": 0,
        "files_skipped": skipped,
    }

    # --- Delete vectors for removed files ---
    for path in deleted_paths:
        old_chunks = chunk_text(stored_hashes.get(path, ""), path, chunk_size, overlap)
        keys_to_delete = [_chunk_key(path, c["chunk_idx"]) for c in old_chunks]
        if keys_to_delete:
            s3v.delete_vectors(
                vectorBucketName=vector_bucket,
                indexName=_VECTOR_INDEX_NAME,
                keys=keys_to_delete,
            )
            stats["chunks_deleted"] += len(keys_to_delete)
        stored_hashes.pop(path, None)

    # --- Upsert vectors for changed/new files ---
    total_changed = len(changed_paths)
    for i, path in enumerate(sorted(changed_paths), 1):
        content = notes[path]
        chunks = chunk_text(content, path, chunk_size, overlap)

        import logging as _log
        _log.getLogger().info("[%d/%d] embedding %s (%d chunks)", i, total_changed, path, len(chunks))

        if not chunks:
            stored_hashes[path] = _file_hash(content)
            continue

        texts = [c["text"] for c in chunks]
        vectors = _embed_batch(texts, model_id, bedrock)

        put_vectors = [
            {
                "key": _chunk_key(path, c["chunk_idx"]),
                "data": {"float32": v},
                "metadata": {
                    "text": c["text"],
                    "path": c["path"],
                    "chunk_idx": c["chunk_idx"],
                },
            }
            for c, v in zip(chunks, vectors)
        ]

        # S3 Vectors PutVectors accepts up to 500 vectors per call
        _batch_put_vectors(s3v, vector_bucket, put_vectors)
        stats["chunks_upserted"] += len(put_vectors)
        stored_hashes[path] = _file_hash(content)

    _save_hashes(s3_bucket, stored_hashes)
    return stats


def _batch_put_vectors(s3v_client, vector_bucket: str, vectors: list[dict], batch_size: int = 500) -> None:
    """PutVectors in batches of up to 500 (S3 Vectors API limit)."""
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i : i + batch_size]
        s3v_client.put_vectors(
            vectorBucketName=vector_bucket,
            indexName=_VECTOR_INDEX_NAME,
            vectors=batch,
        )


# ---------------------------------------------------------------------------
# Index query (called at intake time)
# ---------------------------------------------------------------------------

def query_notes(
    query: str,
    s3_bucket: str,
    top_k: int = 5,
    vector_bucket: Optional[str] = None,
) -> list[dict]:
    """Embed a query and return top-k relevant note chunks via S3 Vectors.

    Returns a list of dicts with keys: text, source (path), score, chunk_idx.
    Raises an exception if the index does not exist (caller should catch).
    """
    vector_bucket = vector_bucket or os.environ.get("VECTOR_BUCKET", "")
    if not vector_bucket:
        raise ValueError("VECTOR_BUCKET env var is required for S3 Vectors query")

    model_id = os.environ.get("RAG_EMBEDDING_MODEL", _DEFAULT_EMBEDDING_MODEL)
    bedrock = _get_bedrock_client()
    s3v = _get_s3vectors_client()

    query_vecs = _embed_batch([query], model_id, bedrock)
    query_vector = query_vecs[0]

    resp = s3v.query_vectors(
        vectorBucketName=vector_bucket,
        indexName=_VECTOR_INDEX_NAME,
        queryVector={"float32": query_vector},
        topK=top_k,
        returnMetadata=True,
    )

    results: list[dict] = []
    for item in resp.get("vectors", []):
        meta = item.get("metadata", {})
        results.append({
            "text": meta.get("text", ""),
            "source": meta.get("path", ""),
            "score": float(item.get("score", 0.0)),
            "chunk_idx": meta.get("chunk_idx", 0),
        })
    return results
