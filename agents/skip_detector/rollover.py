"""Skip detection and rollover logic. Pure Python — no LLM, no LangGraph."""
from __future__ import annotations

import json
import os
import re
from datetime import date
from typing import Any

import boto3

from shared.github_client import GitHubClient

MAX_ROLLOVER = 2
_S3_BUCKET = os.environ.get("S3_BUCKET", "skillos-state")
_SKIP_STATE_KEY = "skip_state.json"


def _parse_incomplete_tasks(content: str) -> list[dict]:
    """Extract unchecked tasks from a daily MD file."""
    tasks: list[dict] = []
    for line in content.splitlines():
        match = re.match(r"- \[ \] \[(\d+)min\] (.+?)\s+`#(.+?)`", line)
        if match:
            tasks.append(
                {
                    "duration_min": int(match.group(1)),
                    "task": match.group(2).strip(),
                    "node_id": match.group(3).strip(),
                }
            )
    return tasks


def detect_and_write_rollover(gh: GitHubClient) -> dict[str, Any]:
    """
    For each active skill with no progress commit today, write rollover tasks to S3.
    Returns the skip_state dict written (empty dict if everyone progressed).
    """
    s3 = boto3.client("s3")
    today = date.today().isoformat()

    all_skills: list[dict] = json.loads(gh.get_file("skills/active.json"))
    # Only check skills that are actively running; skip paused/completed
    active = [s for s in all_skills if s.get("status", "active") == "active"]
    skip_state: dict[str, Any] = {}

    for skill in active:
        name = skill["name"]
        if gh.commit_exists_today(name):
            continue

        try:
            daily_content = gh.get_file(f"skills/{name}/daily/{today}.md")
            all_tasks = _parse_incomplete_tasks(daily_content)
        except Exception:
            all_tasks = []

        skip_state[name] = {
            "skipped_date": today,
            "rollover_tasks": all_tasks[:MAX_ROLLOVER],
        }

    s3.put_object(
        Bucket=_S3_BUCKET,
        Key=_SKIP_STATE_KEY,
        Body=json.dumps(skip_state, indent=2).encode(),
        ContentType="application/json",
    )
    return skip_state
