"""Lambda handler for the RAG index builder.

Triggered by EventBridge at 06:00 daily (before the Planner at 08:00).
Can also be invoked manually: aws lambda invoke --function-name skillos-rag-indexer.

Reads .md files from S3 (vault/ prefix, populated by GitHub Actions on push),
diffs against stored file hashes, embeds only changed files, and upserts/deletes
vectors in the S3 Vectors index.

Environment variables:
  S3_BUCKET                                  — state bucket (vault/ prefix + file_hashes.json)
  VECTOR_BUCKET                              — S3 Vectors vector bucket name
  RAG_CHUNK_SIZE      (optional, default 500)
  RAG_CHUNK_OVERLAP   (optional, default 100)
  RAG_EMBEDDING_MODEL (optional)
  RAG_EMBED_SLEEP     (optional, default 0.25) — seconds between Titan calls.
                       Set to 0 for bulk/initial indexing runs; throttles are
                       handled by exponential backoff in shared/rag.py.
"""
from __future__ import annotations

import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: dict, context) -> dict:
    from shared.rag import upsert_index

    s3_bucket = os.environ.get("S3_BUCKET", "skillos-state")
    vector_bucket = os.environ.get("VECTOR_BUCKET", "")

    if not vector_bucket:
        raise ValueError("VECTOR_BUCKET env var is required")

    # Allow caller to restrict which roots are processed, e.g. {"roots": ["Inbox"]}
    roots = event.get("roots") if event else None
    if roots:
        logger.info("Processing subset of roots: %s", roots)

    notes = _fetch_all_notes_from_s3(s3_bucket, roots=roots)
    logger.info("Fetched %d note files from S3", len(notes))

    if not notes:
        logger.warning("No notes found in S3 — index not updated.")
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


_INDEX_ROOTS = ["notes", "Slipbox", "Inbox", "Outbox", "Areas"]
_VAULT_PREFIX = "vault/"


def _fetch_all_notes_from_s3(s3_bucket: str, roots: list[str] | None = None) -> dict[str, str]:
    """Return {s3_key: content} for all .md files under vault/ indexed roots.

    Args:
        s3_bucket: S3 bucket containing vault/ prefix.
        roots: subset of _INDEX_ROOTS to process; defaults to all roots.
    """
    active_roots = roots if roots else _INDEX_ROOTS
    s3 = boto3.client("s3")
    notes: dict[str, str] = {}
    for root in active_roots:
        prefix = f"{_VAULT_PREFIX}{root}/"
        paginator = s3.get_paginator("list_objects_v2")
        root_count = 0
        for page in paginator.paginate(Bucket=s3_bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                key = obj["Key"]
                if key.endswith(".md"):
                    body = s3.get_object(Bucket=s3_bucket, Key=key)["Body"]
                    notes[key] = body.read().decode("utf-8", errors="replace")
                    root_count += 1
        logger.info("  %s: %d files", root, root_count)
    return notes
