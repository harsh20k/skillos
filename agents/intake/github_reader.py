"""Read user notes from GitHub to provide context during intake.

Two retrieval modes:
- fetch_notes_summary: legacy fallback — concatenates first N chars of each note.
- fetch_notes_for_query: RAG-backed retrieval via S3 Vectors.
  Falls back to fetch_notes_summary if the index is missing or RAG is disabled.
"""
import logging
import os

from shared.github_client import GitHubClient

logger = logging.getLogger(__name__)

_MAX_FILE_CHARS = 2_000
_MAX_TOTAL_CHARS = 8_000


def fetch_notes_summary(client: GitHubClient) -> str:
    """Return a concatenated summary of all .md files under notes/."""
    paths = client.list_dir("notes")
    logger.info("[RAG] fetch_notes_summary: list_dir('notes') returned %d paths", len(paths) if paths else 0)
    if not paths:
        logger.warning("[RAG] fetch_notes_summary: no paths found under notes/")
        return ""

    parts: list[str] = []
    for path in paths:
        if not path.endswith(".md"):
            continue
        try:
            content = client.get_file(path)
            parts.append(f"### {path}\n{content[:_MAX_FILE_CHARS]}")
        except Exception as e:
            logger.warning("[RAG] fetch_notes_summary: failed to read %s: %s", path, e)
            continue

    result = "\n\n".join(parts)[:_MAX_TOTAL_CHARS]
    logger.info("[RAG] fetch_notes_summary: returning %d chars from %d files", len(result), len(parts))
    return result


def fetch_notes_for_query(client: GitHubClient, query: str) -> str:
    """Return relevant note chunks for the given query using RAG.

    Uses S3 Vectors for retrieval. Falls back to fetch_notes_summary if RAG is unavailable.
    """
    s3_bucket = os.environ.get("S3_BUCKET", "skillos-state")
    vector_bucket = os.environ.get("VECTOR_BUCKET", "")
    top_k = int(os.environ.get("RAG_TOP_K", "5"))

    logger.info(
        "[RAG] fetch_notes_for_query: query=%r s3_bucket=%r vector_bucket=%r top_k=%d",
        query[:120], s3_bucket, vector_bucket, top_k,
    )

    try:
        from shared.rag import query_notes
        chunks = query_notes(query=query, s3_bucket=s3_bucket, top_k=top_k)
        logger.info("[RAG] query_notes returned %d chunks", len(chunks))
        if chunks:
            for i, c in enumerate(chunks):
                logger.info(
                    "[RAG] chunk[%d]: source=%r score=%.4f text_len=%d preview=%r",
                    i, c.get("source"), c.get("score"), len(c.get("text", "")), c.get("text", "")[:80],
                )
        if not chunks:
            logger.warning("[RAG] query_notes returned 0 chunks — falling back to notes_summary")
            return fetch_notes_summary(client)
        parts = [f"### {c['source']} (score: {c['score']:.3f})\n{c['text']}" for c in chunks]
        result = "\n\n".join(parts)
        logger.info("[RAG] RAG result: %d chars from %d chunks", len(result), len(chunks))
        return result
    except Exception as e:
        logger.exception("[RAG] query_notes raised %s: %s — falling back to notes_summary", type(e).__name__, e)
        return fetch_notes_summary(client)
