"""Top-level supervisor graph.

Routes incoming triggers to the correct agent subgraph:
  trigger_type "intake" → IntakeSubgraph
  trigger_type "plan"   → PlannerSubgraph
  trigger_type "track"  → TrackerSubgraph
  trigger_type "skip"   → SkipDetector (pure logic, no subgraph)

LangSmith tracing is enabled automatically when the env vars
LANGCHAIN_TRACING_V2=true and LANGCHAIN_API_KEY are set.
"""
from __future__ import annotations

from typing import Literal, Optional

from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict


class SupervisorState(TypedDict):
    trigger_type: Literal["intake", "plan", "skip", "track"]
    payload: dict
    result: dict


def build_supervisor_graph():
    def route(state: SupervisorState) -> str:
        return state["trigger_type"]

    def run_intake(state: SupervisorState) -> dict:
        from agents.intake.graph import build_intake_graph
        from checkpointer.github_checkpointer import GitHubCheckpointer
        from langchain_core.messages import HumanMessage
        from shared.github_client import GitHubClient

        gh = GitHubClient()
        graph = build_intake_graph(gh=gh, checkpointer=GitHubCheckpointer(gh))
        payload = state["payload"]
        config = {"configurable": {"thread_id": f"intake-{payload.get('user_id', 'default')}"}}
        result = graph.invoke(
            {"messages": [HumanMessage(content=payload.get("message", ""))]},
            config=config,
        )
        return {"result": result}

    def run_planner(state: SupervisorState) -> dict:
        from agents.planner.graph import PlannerState, build_planner_graph

        graph = build_planner_graph()
        result = graph.invoke(
            PlannerState(
                active_skills=[],
                skip_state={},
                skill_trees={},
                unlocked={},
                daily_tasks=[],
            )
        )
        return {"result": result}

    def run_tracker(state: SupervisorState) -> dict:
        from agents.tracker.graph import TrackerState, build_tracker_graph
        from shared.github_client import GitHubClient

        gh = GitHubClient()
        graph = build_tracker_graph(gh=gh)
        payload = state["payload"]
        result = graph.invoke(
            TrackerState(
                skill=payload.get("skill", ""),
                user_id=payload.get("user_id", ""),
                context=payload.get("context", ""),
                progress_note="",
                skill_tree={},
                completed_node_ids=[],
                unlocked_nodes=[],
                error=None,
            )
        )
        return {"result": result}

    def run_skip(state: SupervisorState) -> dict:
        from agents.skip_detector.rollover import detect_and_write_rollover
        from shared.github_client import GitHubClient

        skip_state = detect_and_write_rollover(GitHubClient())
        return {"result": {"skipped": list(skip_state.keys())}}

    graph = StateGraph(SupervisorState)
    graph.add_node("router", lambda state: {})  # no-op routing node
    graph.add_node("intake", run_intake)
    graph.add_node("plan", run_planner)
    graph.add_node("track", run_tracker)
    graph.add_node("skip", run_skip)

    graph.set_entry_point("router")
    graph.add_conditional_edges(
        "router",
        route,
        {"intake": "intake", "plan": "plan", "track": "track", "skip": "skip"},
    )
    for node in ("intake", "plan", "track", "skip"):
        graph.add_edge(node, END)

    return graph.compile()
