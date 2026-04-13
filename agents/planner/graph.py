"""LangGraph subgraph for the Planner agent.

Single-invocation graph (no human loop):
  load_state → parse_skill_trees → generate_tasks → write_daily_md
"""
from __future__ import annotations

import json
import os
from datetime import date
from typing import Optional

import boto3
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict

from agents.planner.prompt import PLANNER_SYSTEM_PROMPT
from agents.planner.skill_tree import get_unlocked_nodes, parse_skill_tree
from shared.github_client import GitHubClient
from shared.llm import get_llm

_S3_BUCKET = os.environ.get("S3_BUCKET", "skillos-state")
_SKIP_STATE_KEY = "skip_state.json"


class PlannerState(TypedDict):
    active_skills: list[dict]
    skip_state: dict
    skill_trees: dict       # skill_name -> parsed tree dict
    unlocked: dict          # skill_name -> list of unlocked node dicts
    daily_tasks: list[dict]


def build_planner_graph(gh: Optional[GitHubClient] = None):
    llm = get_llm()
    _gh = gh or GitHubClient()
    s3 = boto3.client("s3")

    def load_state(state: PlannerState) -> dict:
        raw = _gh.get_file("skills/active.json")
        active: list[dict] = json.loads(raw)

        try:
            resp = s3.get_object(Bucket=_S3_BUCKET, Key=_SKIP_STATE_KEY)
            skip_state: dict = json.loads(resp["Body"].read())
        except s3.exceptions.NoSuchKey:
            skip_state = {}

        return {"active_skills": active, "skip_state": skip_state}

    def parse_skill_trees(state: PlannerState) -> dict:
        trees: dict = {}
        unlocked: dict = {}
        for skill in state["active_skills"]:
            name = skill["name"]
            try:
                content = _gh.get_file(f"skills/{name}/skill-tree.md")
                tree = parse_skill_tree(content)
                trees[name] = tree
                unlocked[name] = get_unlocked_nodes(tree)
            except Exception:
                trees[name] = {}
                unlocked[name] = []
        return {"skill_trees": trees, "unlocked": unlocked}

    def generate_tasks(state: PlannerState) -> dict:
        context_parts: list[str] = []
        for skill in state["active_skills"]:
            name = skill["name"]
            nodes = state["unlocked"].get(name, [])
            skipped = state["skip_state"].get(name, {}).get("rollover_tasks", [])
            context_parts.append(
                f"Skill: {skill['display_name']} (difficulty: {skill['difficulty']})\n"
                f"Unlocked nodes: {json.dumps(nodes)}\n"
                f"Rolled-over tasks from yesterday: {json.dumps(skipped)}"
            )

        prompt = "\n\n---\n\n".join(context_parts)
        response = llm.invoke(
            [SystemMessage(content=PLANNER_SYSTEM_PROMPT), HumanMessage(content=prompt)]
        )
        content: str = getattr(response, "content", "")
        if "```json" in content:
            json_str = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            json_str = content.split("```")[1].split("```")[0].strip()
        else:
            json_str = content.strip()
        return {"daily_tasks": json.loads(json_str)}

    def write_daily_md(state: PlannerState) -> dict:
        today = date.today().isoformat()
        tasks = state["daily_tasks"]

        by_skill: dict[str, list] = {}
        for task in tasks:
            by_skill.setdefault(task["skill"], []).append(task)

        lines = [f"# Daily Tasks — {today}\n"]
        for skill_name, skill_tasks in by_skill.items():
            display = next(
                (s["display_name"] for s in state["active_skills"] if s["name"] == skill_name),
                skill_name,
            )
            lines.append(f"\n## {display}\n")
            for t in skill_tasks:
                lines.append(f"- [ ] [{t['duration_min']}min] {t['task']}  `#{t['node_id']}`")

        content = "\n".join(lines) + "\n"

        for skill in state["active_skills"]:
            _gh.write_file(
                f"skills/{skill['name']}/daily/{today}.md",
                content,
                f"plan: daily tasks {today}",
            )

        # Clear skip state now that rollover has been consumed
        s3.put_object(
            Bucket=_S3_BUCKET,
            Key=_SKIP_STATE_KEY,
            Body=b"{}",
            ContentType="application/json",
        )
        return {}

    graph = StateGraph(PlannerState)
    graph.add_node("load_state", load_state)
    graph.add_node("parse_skill_trees", parse_skill_trees)
    graph.add_node("generate_tasks", generate_tasks)
    graph.add_node("write_daily_md", write_daily_md)

    graph.set_entry_point("load_state")
    graph.add_edge("load_state", "parse_skill_trees")
    graph.add_edge("parse_skill_trees", "generate_tasks")
    graph.add_edge("generate_tasks", "write_daily_md")
    graph.add_edge("write_daily_md", END)

    return graph.compile()
