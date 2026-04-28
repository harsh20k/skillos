"""LangGraph subgraph for the Intake agent.

Flow (per Lambda invocation — human-in-the-loop via checkpointer):
  read_notes → clarify → [wait for next human message | scaffold → write_outputs]

The graph pauses at END after each clarify turn; the checkpointer persists
state so the next Slack message resumes the conversation.

Multi-turn routing uses structured output (ClarifyResponse) so routing is
based on a parsed boolean rather than fragile string matching.
"""
from __future__ import annotations

import json
from datetime import date
from typing import Annotated, Optional

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from agents.intake.github_reader import fetch_notes_for_query, fetch_notes_summary
from agents.intake.prompt import ClarifyResponse, get_prompt as get_intake_prompt
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
    structured_llm = llm.with_structured_output(ClarifyResponse)
    _gh = gh or GitHubClient()

    def read_notes(state: IntakeState) -> dict:
        if state.get("notes_summary"):
            return {}
        # Try to extract the user's goal from the first human message for RAG retrieval
        first_human = next(
            (m for m in state.get("messages", []) if isinstance(m, HumanMessage)),
            None,
        )
        query = getattr(first_human, "content", "") if first_human else ""

        if query:
            summary = fetch_notes_for_query(_gh, query)
        else:
            summary = fetch_notes_summary(_gh)

        return {"notes_summary": summary, "clarification_turns": 0, "done": False}

    def clarify(state: IntakeState) -> dict:
        context = state.get("notes_summary", "")
        suffix = f"\n\nUser's existing notes for context:\n{context}" if context else ""

        turns = state.get("clarification_turns", 0)
        soft_cap_nudge = ""
        if turns >= 5:
            soft_cap_nudge = (
                "\n\nYou have asked several clarifying questions. "
                "You MUST set ready=true and produce the skill tree in this response."
            )

        msgs: list[BaseMessage] = [
            SystemMessage(content=get_intake_prompt() + suffix + soft_cap_nudge)
        ]
        msgs += state["messages"]

        response: ClarifyResponse = structured_llm.invoke(msgs)

        # Store the structured response as an AI message so message history stays clean
        from langchain_core.messages import AIMessage
        ai_msg = AIMessage(content=response.reply)

        return {
            "messages": [ai_msg],
            "clarification_turns": turns + 1,
            "_clarify_response": response,
        }

    def route_after_clarify(state: IntakeState) -> str:
        # The structured response is stored transiently in state; fall back gracefully
        resp: Optional[ClarifyResponse] = state.get("_clarify_response")
        if resp is not None and resp.ready:
            return "scaffold"
        # Soft cap: force scaffold after 6 turns regardless
        if state.get("clarification_turns", 0) >= 6:
            return "scaffold"
        return "wait"

    def scaffold_skill_tree(state: IntakeState) -> dict:
        # Use the skill tree from the structured response if available
        resp: Optional[ClarifyResponse] = state.get("_clarify_response")
        if resp is not None and resp.skill_tree:
            return {"skill_tree_json": resp.skill_tree}

        # Fallback: ask the LLM to emit the tree from conversation history
        from langchain_core.output_parsers import JsonOutputParser
        follow_up = llm.invoke(
            state["messages"]
            + [HumanMessage(content="Output ONLY the JSON skill tree object now, no prose.")]
        )
        raw: str = getattr(follow_up, "content", "")
        if "```json" in raw:
            json_str = raw.split("```json")[1].split("```")[0].strip()
        elif "```" in raw:
            json_str = raw.split("```")[1].split("```")[0].strip()
        else:
            json_str = raw.strip()

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
                    "status": "active",
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
