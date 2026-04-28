"""Lambda handler for the RAG index builder.

Triggered by EventBridge at 06:00 daily (before the Planner at 08:00).
Can also be invoked manually: aws lambda invoke --function-name skillos-rag-indexer.

Reads all notes/**/*.md from GitHub, chunks them, embeds with Bedrock Titan,
and writes the FAISS index + chunk manifest to S3.

Environment variables:
  GITHUB_TOKEN, GITHUB_REPO, GITHUB_BRANCH  — GitHub access
  S3_BUCKET                                  — state bucket
  RAG_CHUNK_SIZE     (optional, default 500)
  RAG_CHUNK_OVERLAP  (optional, default 100)
  RAG_EMBEDDING_MODEL (optional)
"""
from __future__ import annotations

import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: dict, context) -> dict:
    from shared.github_client import GitHubClient
    from shared.rag import build_index

    s3_bucket = os.environ.get("S3_BUCKET", "skillos-state")

    gh = GitHubClient()

    # Recursively list notes/
    notes = _fetch_all_notes(gh)
    logger.info("Fetched %d note files from GitHub", len(notes))

    if not notes:
        logger.warning("No notes found — index not updated.")
        return {"status": "skipped", "reason": "no notes found"}

    chunk_count = build_index(notes=notes, s3_bucket=s3_bucket)
    logger.info("Built FAISS index with %d chunks, uploaded to s3://%s/rag/", chunk_count, s3_bucket)

    return {"status": "ok", "files_indexed": len(notes), "chunks": chunk_count}


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
            # Looks like a directory (no extension) — recurse
            _walk(gh, entry, acc)
