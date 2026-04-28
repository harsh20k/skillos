"""LLM-powered supervisor graph.

Routes natural language from /skillos to the correct agent or action:
  load_context → classify_intent → run_{intake|tracker|query|action} → format_reply → END

The classify_intent node uses structured output (SupervisorDecision) to determine
which handler to invoke. The format_reply node wraps raw data into a friendly
Slack message.

Existing individual slash commands (/learn, /done, /pause, etc.) remain unchanged;
/skillos is an additional unified entry point.
"""
from __future__ import annotations

import json
import os
from typing import Optional

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict

from shared.github_client import GitHubClient
from shared.llm import get_llm
from supervisor.actions import (
    execute_difficulty,
    execute_pause,
    execute_reshuffle,
    execute_resume,
    execute_skip,
    fetch_all_skills,
    fetch_remaining_tasks,
    fetch_skill_status,
    fetch_todays_tasks,
    fetch_why_tasks,
)
from supervisor.prompt import get_classify_prompt, get_format_prompt
from supervisor.schema import SupervisorDecision


class SupervisorState(TypedDict):
    message: str
    user_id: str
    active_skills: list[dict]
    decision: Optional[dict]
    raw_data: Optional[str]
    reply: str


def build_supervisor_graph(gh: Optional[GitHubClient] = None):
    llm = get_llm()
    structured_llm = llm.with_structured_output(SupervisorDecision)
    _gh = gh or GitHubClient()

    # ------------------------------------------------------------------
    # Nodes
    # ------------------------------------------------------------------

    def load_context(state: SupervisorState) -> dict:
        try:
            raw = _gh.get_file("skills/active.json")
            active: list[dict] = json.loads(raw)
        except Exception:
            active = []
        return {"active_skills": active}

    def classify_intent(state: SupervisorState) -> dict:
        skill_names = [
            f"{s['name']} ({s['display_name']})" for s in state.get("active_skills", [])
        ]
        prompt_template = get_classify_prompt()
        prompt_text = prompt_template.format(
            active_skills=", ".join(skill_names) if skill_names else "(none)",
            message=state["message"],
        )

        decision: SupervisorDecision = structured_llm.invoke(
            [SystemMessage(content=prompt_text)]
        )
        return {"decision": decision.model_dump()}

    def run_intake(state: SupervisorState) -> dict:
        """Delegate to the Intake Lambda for multi-turn persistence."""
        import boto3

        client = boto3.client("lambda")
        intake_name = os.environ.get("INTAKE_LAMBDA_NAME", "skillos-intake")
        payload = {
            "user_id": state.get("user_id", "default"),
            "message": state["message"],
        }
        resp = client.invoke(
            FunctionName=intake_name,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload).encode(),
        )
        result = json.loads(resp["Payload"].read())
        return {"raw_data": result.get("reply", "Intake is processing your request.")}

    def run_tracker(state: SupervisorState) -> dict:
        decision = state.get("decision", {})
        skill = decision.get("skill", "")
        if not skill:
            return {"raw_data": "I couldn't determine which skill you completed. Please specify, e.g. 'done with portrait-sketching'."}

        import boto3

        client = boto3.client("lambda")
        tracker_name = os.environ.get("TRACKER_LAMBDA_NAME", "skillos-tracker")
        payload = {
            "skill": skill,
            "user_id": state.get("user_id", "default"),
            "context": state["message"],
        }
        resp = client.invoke(
            FunctionName=tracker_name,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload).encode(),
        )
        result = json.loads(resp["Payload"].read())

        if result.get("status") == "error":
            return {"raw_data": f"Error: {result.get('message', 'unknown error')}"}

        note = result.get("note", "")
        unlocked = result.get("unlocked", [])
        msg = f"Progress logged for {skill}.\nNote: {note}"
        if unlocked:
            msg += f"\nNewly unlocked nodes: {', '.join(unlocked)}"
        return {"raw_data": msg}

    def run_query(state: SupervisorState) -> dict:
        decision = state.get("decision", {})
        query_type = decision.get("query_type", "todays_tasks")
        active_skills = state.get("active_skills", [])
        skill = decision.get("skill")

        handlers = {
            "todays_tasks": lambda: fetch_todays_tasks(_gh, active_skills),
            "remaining_tasks": lambda: fetch_remaining_tasks(_gh, active_skills),
            "why_tasks": lambda: fetch_why_tasks(_gh, active_skills),
            "list_skills": lambda: fetch_all_skills(_gh, active_skills),
            "skill_status": lambda: fetch_skill_status(_gh, active_skills, skill or ""),
        }

        handler = handlers.get(query_type, handlers["todays_tasks"])
        return {"raw_data": handler()}

    def run_action(state: SupervisorState) -> dict:
        decision = state.get("decision", {})
        action = decision.get("action")
        skill = decision.get("skill", "")

        if action == "pause":
            return {"raw_data": execute_pause(_gh, skill)}
        elif action == "resume":
            return {"raw_data": execute_resume(_gh, skill)}
        elif action == "harder":
            return {"raw_data": execute_difficulty(_gh, skill, "harder")}
        elif action == "easier":
            return {"raw_data": execute_difficulty(_gh, skill, "easier")}
        elif action == "skip":
            return {"raw_data": execute_skip(_gh, skill)}
        elif action == "reshuffle":
            return {"raw_data": execute_reshuffle()}
        else:
            return {"raw_data": f"Unknown action: {action}"}

    def format_reply(state: SupervisorState) -> dict:
        raw_data = state.get("raw_data")
        decision = state.get("decision", {})
        intent = decision.get("intent", "unknown")

        if not raw_data:
            return {"reply": "I'm not sure what you'd like to do. Try something like 'show my tasks' or 'I want to learn guitar'."}

        # For intake, the Intake Lambda already formats its reply
        if intent == "intake":
            return {"reply": raw_data}

        prompt_template = get_format_prompt()
        prompt_text = prompt_template.format(intent=intent, raw_data=raw_data)

        response = llm.invoke([SystemMessage(content=prompt_text)])
        return {"reply": getattr(response, "content", raw_data)}

    # ------------------------------------------------------------------
    # Route
    # ------------------------------------------------------------------

    def route_after_classify(state: SupervisorState) -> str:
        decision = state.get("decision", {})
        intent = decision.get("intent", "unknown")
        if intent in ("intake", "track", "query", "action"):
            return intent
        return "unknown"

    # ------------------------------------------------------------------
    # Graph
    # ------------------------------------------------------------------

    graph = StateGraph(SupervisorState)
    graph.add_node("load_context", load_context)
    graph.add_node("classify_intent", classify_intent)
    graph.add_node("run_intake", run_intake)
    graph.add_node("run_tracker", run_tracker)
    graph.add_node("run_query", run_query)
    graph.add_node("run_action", run_action)
    graph.add_node("format_reply", format_reply)

    graph.set_entry_point("load_context")
    graph.add_edge("load_context", "classify_intent")
    graph.add_conditional_edges(
        "classify_intent",
        route_after_classify,
        {
            "intake": "run_intake",
            "track": "run_tracker",
            "query": "run_query",
            "action": "run_action",
            "unknown": "format_reply",
        },
    )
    for node in ("run_intake", "run_tracker", "run_query", "run_action"):
        graph.add_edge(node, "format_reply")
    graph.add_edge("format_reply", END)

    return graph.compile()
