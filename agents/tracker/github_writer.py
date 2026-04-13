"""GitHub write operations for the Tracker agent."""
from __future__ import annotations

import json
from datetime import date

from agents.planner.skill_tree import mark_node_done, parse_skill_tree
from shared.github_client import GitHubClient


def write_progress(gh: GitHubClient, skill: str, note: str) -> None:
    today = date.today().isoformat()
    try:
        existing = gh.get_file(f"skills/{skill}/progress.md")
    except Exception:
        existing = f"# Progress: {skill}\n\n"

    entry = f"\n## {today}\n\n{note}\n"
    gh.write_file(
        f"skills/{skill}/progress.md",
        existing + entry,
        f"progress: {skill} {today}",
    )


def unlock_nodes(gh: GitHubClient, skill: str, completed_node_ids: list[str]) -> list[str]:
    """Mark nodes done in skill-tree.md; return list of newly unlocked node IDs."""
    content = gh.get_file(f"skills/{skill}/skill-tree.md")
    tree = parse_skill_tree(content)

    for node_id in completed_node_ids:
        tree = mark_node_done(tree, node_id)

    tree_md = (
        f"# Skill Tree: {tree.get('display_name', skill)}\n\n"
        f"```json\n{json.dumps(tree, indent=2)}\n```\n"
    )
    gh.write_file(
        f"skills/{skill}/skill-tree.md",
        tree_md,
        f"skill-tree: unlock nodes {skill}",
    )

    return [n["id"] for n in tree["nodes"] if n.get("status") == "unlocked"]


def dry_run_diff(skill: str, note: str) -> str:
    """Return a human-readable preview of what would be written."""
    today = date.today().isoformat()
    return (
        f"[DRY RUN] Would append to skills/{skill}/progress.md:\n"
        f"\n## {today}\n\n{note}\n"
    )
