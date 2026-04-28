"""Reusable query and action functions for the supervisor agent.

These mirror the logic in skillos_slack/bot.py but return strings instead of
calling say(), so they can be used by both the Slack handlers and the
supervisor graph.
"""
from __future__ import annotations

import json
import os
import re
from datetime import date

from shared.github_client import GitHubClient

_DIFFICULTY_LEVELS = ["beginner", "intermediate", "advanced"]


# ---------------------------------------------------------------------------
# Queries (read-only)
# ---------------------------------------------------------------------------

def fetch_todays_tasks(gh: GitHubClient, active_skills: list[dict]) -> str:
    """Return today's full task list with completion status as plain text."""
    today = date.today().isoformat()
    running = [s for s in active_skills if s.get("status", "active") == "active"]
    if not running:
        return "No active skills."

    lines: list[str] = [f"Tasks for {today}:"]
    any_found = False
    for skill in running:
        name = skill["name"]
        display = skill["display_name"]
        try:
            content = gh.get_file(f"skills/{name}/daily/{today}.md")
            task_lines = [l for l in content.splitlines() if l.strip().startswith("- [")]
            if task_lines:
                any_found = True
                lines.append(f"\n{display}:")
                lines.extend(task_lines)
        except Exception:
            continue

    if not any_found:
        return "No tasks found for today. The planner runs at 08:00."
    return "\n".join(lines)


def fetch_remaining_tasks(gh: GitHubClient, active_skills: list[dict]) -> str:
    """Return only unchecked tasks for today."""
    today = date.today().isoformat()
    running = [s for s in active_skills if s.get("status", "active") == "active"]
    lines: list[str] = [f"Remaining tasks for {today}:"]
    any_found = False

    for skill in running:
        name = skill["name"]
        display = skill["display_name"]
        try:
            content = gh.get_file(f"skills/{name}/daily/{today}.md")
            unchecked = [l for l in content.splitlines() if l.strip().startswith("- [ ]")]
            if unchecked:
                any_found = True
                lines.append(f"\n{display}:")
                lines.extend(unchecked)
        except Exception:
            continue

    if not any_found:
        return "All tasks done for today!"
    return "\n".join(lines)


def fetch_why_tasks(gh: GitHubClient, active_skills: list[dict]) -> str:
    """Explain reasoning behind each task using the skill tree DAG."""
    from agents.planner.skill_tree import parse_skill_tree

    today = date.today().isoformat()
    running = [s for s in active_skills if s.get("status", "active") == "active"]
    lines: list[str] = [f"Why each task — {today}:"]
    any_found = False

    for skill in running:
        name = skill["name"]
        display = skill["display_name"]
        try:
            daily_content = gh.get_file(f"skills/{name}/daily/{today}.md")
            tree = parse_skill_tree(gh.get_file(f"skills/{name}/skill-tree.md"))
        except Exception:
            continue

        node_map = {n["id"]: n for n in tree.get("nodes", [])}
        task_lines = [l for l in daily_content.splitlines() if l.strip().startswith("- [")]
        if not task_lines:
            continue

        any_found = True
        lines.append(f"\n{display}:")

        for task_line in task_lines:
            node_match = re.search(r"`#([^`]+)`", task_line)
            if not node_match:
                lines.append(f"{task_line} — no node link found")
                continue
            node_id = node_match.group(1)
            node = node_map.get(node_id)
            if not node:
                lines.append(f"{task_line} — node {node_id} not in skill tree")
                continue
            prereqs = node.get("prerequisites", [])
            if prereqs:
                prereq_labels = [node_map[p]["label"] if p in node_map else p for p in prereqs]
                why = f"Unlocks after: {', '.join(prereq_labels)}"
            else:
                why = "Root node — starting point"
            lines.append(f"{task_line} — {node['label']}: {why}")

    if not any_found:
        return "No tasks found for today."
    return "\n".join(lines)


def fetch_all_skills(gh: GitHubClient, active_skills: list[dict]) -> str:
    """Return a text summary of all skills with status and difficulty."""
    if not active_skills:
        return "No skills yet. Use /learn to get started."

    status_label = {"active": "Active", "paused": "Paused", "completed": "Completed"}
    lines = ["All skills:"]
    for s in active_skills:
        status = status_label.get(s.get("status", "active"), s.get("status", "active"))
        lines.append(
            f"- {s['display_name']} [{status}] ({s.get('difficulty', 'beginner')}) "
            f"started {s.get('start_date', 'unknown')}"
        )
    return "\n".join(lines)


def fetch_skill_status(gh: GitHubClient, active_skills: list[dict], skill_name: str) -> str:
    """Return status info for a specific skill."""
    skill = next((s for s in active_skills if s["name"] == skill_name), None)
    if not skill:
        return f"Skill '{skill_name}' not found. Active skills: {[s['name'] for s in active_skills]}"

    today = date.today().isoformat()
    status = skill.get("status", "active")
    difficulty = skill.get("difficulty", "beginner")

    lines = [
        f"{skill['display_name']}:",
        f"  Status: {status}",
        f"  Difficulty: {difficulty}",
        f"  Started: {skill.get('start_date', 'unknown')}",
    ]

    try:
        daily = gh.get_file(f"skills/{skill_name}/daily/{today}.md")
        total = daily.count("- [ ]") + daily.count("- [x]")
        done = daily.count("- [x]")
        lines.append(f"  Today: {done}/{total} tasks done")
    except Exception:
        lines.append("  Today: no tasks yet")

    try:
        progress = gh.get_file(f"skills/{skill_name}/progress.md")
        entry_count = progress.count("## 20")
        lines.append(f"  Progress entries: {entry_count}")
    except Exception:
        pass

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Actions (state-changing)
# ---------------------------------------------------------------------------

def execute_pause(gh: GitHubClient, skill: str) -> str:
    """Pause a skill. Returns confirmation message."""
    return _set_status(gh, skill, "paused")


def execute_resume(gh: GitHubClient, skill: str) -> str:
    """Resume a paused skill. Returns confirmation message."""
    return _set_status(gh, skill, "active")


def _set_status(gh: GitHubClient, skill: str, new_status: str) -> str:
    action = "pause" if new_status == "paused" else "resume"
    try:
        active: list[dict] = json.loads(gh.get_file("skills/active.json"))
        for s in active:
            if s["name"] == skill:
                s["status"] = new_status
                gh.write_file(
                    "skills/active.json",
                    json.dumps(active, indent=2),
                    f"skills: {action} {skill}",
                )
                if new_status == "paused":
                    return f"Paused {skill}. It will be excluded from planning and skip detection."
                return f"Resumed {skill}. It will be included in tomorrow's plan."
        return f"Skill '{skill}' not found."
    except Exception as exc:
        return f"Error: {exc}"


def execute_difficulty(gh: GitHubClient, skill: str, direction: str) -> str:
    """Adjust difficulty for a skill. direction is 'harder' or 'easier'."""
    delta = 1 if direction == "harder" else -1
    try:
        active: list[dict] = json.loads(gh.get_file("skills/active.json"))
        for s in active:
            if s["name"] == skill:
                idx = _DIFFICULTY_LEVELS.index(s.get("difficulty", "beginner"))
                new_idx = max(0, min(idx + delta, len(_DIFFICULTY_LEVELS) - 1))
                s["difficulty"] = _DIFFICULTY_LEVELS[new_idx]
                gh.write_file(
                    "skills/active.json",
                    json.dumps(active, indent=2),
                    f"skills: difficulty {direction} {skill}",
                )
                return f"Adjusted {skill} to {s['difficulty']}."
        return f"Skill '{skill}' not found."
    except Exception as exc:
        return f"Error: {exc}"


def execute_skip(gh: GitHubClient, skill: str) -> str:
    """Mark a skill as skipped for today."""
    import boto3

    s3 = boto3.client("s3")
    bucket = os.environ.get("S3_BUCKET", "skillos-state")
    key = "skip_state.json"

    try:
        existing = json.loads(s3.get_object(Bucket=bucket, Key=key)["Body"].read())
    except Exception:
        existing = {}

    existing[skill] = {"skipped_date": date.today().isoformat(), "rollover_tasks": []}
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(existing, indent=2).encode(),
        ContentType="application/json",
    )
    return f"Skipped {skill} for today. Tasks will roll over to tomorrow (max 2)."


def execute_reshuffle() -> str:
    """Invoke the Planner Lambda to regenerate today's tasks."""
    import boto3

    client = boto3.client("lambda")
    planner_name = os.environ.get("PLANNER_LAMBDA_NAME", "skillos-planner")
    client.invoke(
        FunctionName=planner_name,
        InvocationType="RequestResponse",
        Payload=b"{}",
    )
    return "Tasks reshuffled! Today's plan has been regenerated."
