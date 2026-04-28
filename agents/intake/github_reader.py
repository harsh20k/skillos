"""Read user notes from GitHub to provide context during intake.

Two retrieval modes:
- fetch_notes_summary: legacy fallback — concatenates first N chars of each note.
- fetch_notes_for_query: RAG-backed retrieval when the FAISS index exists on S3.
  Falls back to fetch_notes_summary if the index is missing or RAG is disabled.
"""
import os

from shared.github_client import GitHubClient

_MAX_FILE_CHARS = 2_000
_MAX_TOTAL_CHARS = 8_000


def fetch_notes_summary(client: GitHubClient) -> str:
    """Return a concatenated summary of all .md files under notes/."""
    paths = client.list_dir("notes")
    if not paths:
        return ""

    parts: list[str] = []
    for path in paths:
        if not path.endswith(".md"):
            continue
        try:
            content = client.get_file(path)
            parts.append(f"### {path}\n{content[:_MAX_FILE_CHARS]}")
        except Exception:
            continue

    return "\n\n".join(parts)[:_MAX_TOTAL_CHARS]


def fetch_notes_for_query(client: GitHubClient, query: str) -> str:
    """Return relevant note chunks for the given query using RAG.

    Uses FAISS-backed retrieval when the index exists on S3 (WS1).
    Falls back to fetch_notes_summary if RAG is unavailable.
    """
    s3_bucket = os.environ.get("S3_BUCKET", "skillos-state")
    top_k = int(os.environ.get("RAG_TOP_K", "5"))

    try:
        from shared.rag import query_notes
        chunks = query_notes(query=query, s3_bucket=s3_bucket, top_k=top_k)
        if not chunks:
            return fetch_notes_summary(client)
        parts = [f"### {c['source']} (score: {c['score']:.3f})\n{c['text']}" for c in chunks]
        return "\n\n".join(parts)
    except Exception:
        # RAG index not built yet — degrade gracefully to full summary
        return fetch_notes_summary(client)
