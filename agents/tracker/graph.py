"""LangGraph subgraph for the Tracker agent.

Single-invocation graph:
  validate_skill → load_skill_tree → generate_note → dry_run → commit_progress
                ↘ handle_error (if skill not found)
"""
from __future__ import annotations

import json
from datetime import date
from typing import Optional

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict

from agents.tracker.github_writer import dry_run_diff, unlock_nodes, write_progress
from agents.tracker.prompt import TRACKER_SYSTEM_PROMPT
from agents.planner.skill_tree import parse_skill_tree
from shared.github_client import GitHubClient
from shared.llm import get_llm


class TrackerState(TypedDict):
    skill: str
    user_id: str
    context: str                    # optional user message e.g. "finished the eye exercises"
    progress_note: str
    skill_tree: dict
    completed_node_ids: list[str]
    unlocked_nodes: list[str]
    error: Optional[str]


def build_tracker_graph(gh: Optional[GitHubClient] = None, checkpointer=None):
    llm = get_llm()
    _gh = gh or GitHubClient()

    def validate_skill(state: TrackerState) -> dict:
        skill = state["skill"]
        try:
            active: list[dict] = json.loads(_gh.get_file("skills/active.json"))
            names = [s["name"] for s in active]
            if skill not in names:
                return {"error": f"Skill '{skill}' not found. Active: {names}"}
        except Exception as exc:
            return {"error": str(exc)}
        return {"error": None}

    def route_after_validate(state: TrackerState) -> str:
        return "handle_error" if state.get("error") else "load_skill_tree"

    def load_skill_tree(state: TrackerState) -> dict:
        content = _gh.get_file(f"skills/{state['skill']}/skill-tree.md")
        tree = parse_skill_tree(content)
        # Mark all currently unlocked nodes as the ones being completed
        completed = [n["id"] for n in tree.get("nodes", []) if n.get("status") == "unlocked"]
        return {"skill_tree": tree, "completed_node_ids": completed}

    def generate_note(state: TrackerState) -> dict:
        prompt = (
            f"Skill: {state['skill']}\n"
            f"Date: {date.today().isoformat()}\n"
            f"Completed nodes: {state['completed_node_ids']}\n"
            f"User message: {state.get('context') or '(none)'}"
        )
        response = llm.invoke(
            [SystemMessage(content=TRACKER_SYSTEM_PROMPT), HumanMessage(content=prompt)]
        )
        note = getattr(response, "content", "")
        # Show diff before committing
        print(dry_run_diff(state["skill"], note))
        return {"progress_note": note}

    def commit_progress(state: TrackerState) -> dict:
        write_progress(_gh, state["skill"], state["progress_note"])
        newly_unlocked = unlock_nodes(_gh, state["skill"], state["completed_node_ids"])
        return {"unlocked_nodes": newly_unlocked}

    def handle_error(state: TrackerState) -> dict:
        return {}

    graph = StateGraph(TrackerState)
    graph.add_node("validate_skill", validate_skill)
    graph.add_node("load_skill_tree", load_skill_tree)
    graph.add_node("generate_note", generate_note)
    graph.add_node("commit_progress", commit_progress)
    graph.add_node("handle_error", handle_error)

    graph.set_entry_point("validate_skill")
    graph.add_conditional_edges(
        "validate_skill",
        route_after_validate,
        {"handle_error": "handle_error", "load_skill_tree": "load_skill_tree"},
    )
    graph.add_edge("load_skill_tree", "generate_note")
    graph.add_edge("generate_note", "commit_progress")
    graph.add_edge("commit_progress", END)
    graph.add_edge("handle_error", END)

    return graph.compile(checkpointer=checkpointer)
