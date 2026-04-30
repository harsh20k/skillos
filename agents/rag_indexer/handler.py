"""Lambda handler for the RAG index builder.

Triggered by EventBridge at 06:00 daily (before the Planner at 08:00).
Can also be invoked manually: aws lambda invoke --function-name skillos-rag-indexer.

Reads all notes/**/*.md from GitHub, diffs against stored file hashes, embeds
only changed files, and upserts/deletes vectors in the S3 Vectors index.

Environment variables:
  GITHUB_TOKEN, GITHUB_REPO, GITHUB_BRANCH  — GitHub access
  S3_BUCKET                                  — state bucket (stores file_hashes.json)
  VECTOR_BUCKET                              — S3 Vectors vector bucket name
  RAG_CHUNK_SIZE     (optional, default 500)
  RAG_CHUNK_OVERLAP  (optional, default 100)
  RAG_EMBEDDING_MODEL (optional)
"""
from __future__ import annotations

import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: dict, context) -> dict:
    from shared.github_client import GitHubClient
    from shared.rag import upsert_index

    s3_bucket = os.environ.get("S3_BUCKET", "skillos-state")
    vector_bucket = os.environ.get("VECTOR_BUCKET", "")

    if not vector_bucket:
        raise ValueError("VECTOR_BUCKET env var is required")

    gh = GitHubClient()

    notes = _fetch_all_notes(gh)
    logger.info("Fetched %d note files from GitHub", len(notes))

    if not notes:
        logger.warning("No notes found — index not updated.")
        return {"status": "skipped", "reason": "no notes found"}

    stats = upsert_index(notes=notes, s3_bucket=s3_bucket, vector_bucket=vector_bucket)

    logger.info(
        "Index upsert complete — added: %d, updated: %d, deleted: %d, skipped: %d | "
        "chunks upserted: %d, chunks deleted: %d",
        stats["files_added"],
        stats["files_updated"],
        stats["files_deleted"],
        stats["files_skipped"],
        stats["chunks_upserted"],
        stats["chunks_deleted"],
    )

    return {"status": "ok", "files_indexed": len(notes), **stats}


def _fetch_all_notes(gh) -> dict[str, str]:
    """Return {path: content} for all .md files recursively under notes/."""
    notes: dict[str, str] = {}
    _walk(gh, "notes", notes)
    return notes


def _walk(gh, path: str, acc: dict[str, str]) -> None:
    """Recursively walk a GitHub directory path and collect .md files."""
    try:
        entries = gh.list_dir(path)
    except Exception:
        return

    for entry in entries:
        if entry.endswith(".md"):
            try:
                content = gh.get_file(entry)
                acc[entry] = content
            except Exception:
                continue
        elif "." not in entry.split("/")[-1]:
            _walk(gh, entry, acc)
