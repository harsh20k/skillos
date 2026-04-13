"""LangGraph subgraph for the Intake agent.

Flow (per Lambda invocation — human-in-the-loop via checkpointer):
  read_notes → clarify → [wait for next human message | scaffold → write_outputs]

The graph pauses at END after each clarify turn; the checkpointer persists
state so the next Slack message resumes the conversation.
"""
from __future__ import annotations

import json
from datetime import date
from typing import Annotated, Optional

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from agents.intake.github_reader import fetch_notes_summary
from agents.intake.prompt import INTAKE_SYSTEM_PROMPT, READY_SIGNAL
from shared.github_client import GitHubClient
from shared.llm import get_llm


class IntakeState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    notes_summary: str
    clarification_turns: int
    skill_tree_json: Optional[dict]
    active_skills: list[dict]
    done: bool


def build_intake_graph(gh: Optional[GitHubClient] = None, checkpointer=None):
    llm = get_llm()
    _gh = gh or GitHubClient()

    def read_notes(state: IntakeState) -> dict:
        if state.get("notes_summary"):
            return {}
        summary = fetch_notes_summary(_gh)
        return {"notes_summary": summary, "clarification_turns": 0, "done": False}

    def clarify(state: IntakeState) -> dict:
        context = state.get("notes_summary", "")
        suffix = f"\n\nUser's existing notes for context:\n{context}" if context else ""
        msgs: list[BaseMessage] = [SystemMessage(content=INTAKE_SYSTEM_PROMPT + suffix)]
        msgs += state["messages"]
        response = llm.invoke(msgs)
        turns = state.get("clarification_turns", 0) + 1
        return {"messages": [response], "clarification_turns": turns}

    def route_after_clarify(state: IntakeState) -> str:
        last = state["messages"][-1]
        content: str = getattr(last, "content", "")
        if READY_SIGNAL in content or state.get("clarification_turns", 0) >= 3:
            return "scaffold"
        return "wait"  # pause; resume on next human message

    def scaffold_skill_tree(state: IntakeState) -> dict:
        last = state["messages"][-1]
        content: str = getattr(last, "content", "")

        if "```json" in content:
            json_str = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            json_str = content.split("```")[1].split("```")[0].strip()
        else:
            # Ask the LLM to emit only JSON
            follow_up = llm.invoke(
                state["messages"]
                + [HumanMessage(content="Output ONLY the ```json skill tree block now.")]
            )
            raw: str = getattr(follow_up, "content", "")
            json_str = raw.split("```json")[1].split("```")[0].strip() if "```json" in raw else raw.strip()

        return {"skill_tree_json": json.loads(json_str)}

    def write_outputs(state: IntakeState) -> dict:
        tree = state["skill_tree_json"]
        skill_name = tree["skill_name"]

        tree_md = (
            f"# Skill Tree: {tree['display_name']}\n\n"
            f"```json\n{json.dumps(tree, indent=2)}\n```\n"
        )
        _gh.write_file(
            f"skills/{skill_name}/skill-tree.md",
            tree_md,
            f"skill-tree: scaffold {skill_name}",
        )
        _gh.write_file(
            f"skills/{skill_name}/progress.md",
            f"# Progress: {tree['display_name']}\n\n_No entries yet._\n",
            f"progress: init {skill_name}",
        )

        try:
            existing_raw = _gh.get_file("skills/active.json")
            active: list[dict] = json.loads(existing_raw)
        except Exception:
            active = []

        if not any(s["name"] == skill_name for s in active):
            active.append(
                {
                    "name": skill_name,
                    "display_name": tree["display_name"],
                    "start_date": date.today().isoformat(),
                    "difficulty": "beginner",
                }
            )
            _gh.write_file(
                "skills/active.json",
                json.dumps(active, indent=2),
                f"skills: add {skill_name}",
            )

        return {"active_skills": active, "done": True}

    graph = StateGraph(IntakeState)
    graph.add_node("read_notes", read_notes)
    graph.add_node("clarify", clarify)
    graph.add_node("scaffold_skill_tree", scaffold_skill_tree)
    graph.add_node("write_outputs", write_outputs)

    graph.set_entry_point("read_notes")
    graph.add_edge("read_notes", "clarify")
    graph.add_conditional_edges(
        "clarify",
        route_after_clarify,
        {"scaffold": "scaffold_skill_tree", "wait": END},
    )
    graph.add_edge("scaffold_skill_tree", "write_outputs")
    graph.add_edge("write_outputs", END)

    return graph.compile(checkpointer=checkpointer)
