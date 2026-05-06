"""Lambda handler for the Intake agent.

Triggered by Slack /learn command (via Slack bot Lambda).
Uses the GitHub checkpointer to maintain conversation state across invocations.
"""
from datetime import datetime, timedelta, timezone

from langchain_core.messages import HumanMessage

from agents.intake.graph import build_intake_graph
from checkpointer.github_checkpointer import GitHubCheckpointer
from shared.github_client import GitHubClient

_TIMEOUT_HOURS = 1


def lambda_handler(event: dict, context) -> dict:
    """
    Expected event:
      {"user_id": "U123ABC", "message": "I want to learn portrait sketching"}

    Returns:
      {"reply": "...", "done": false}
    """
    user_id: str = event["user_id"]
    message: str = event["message"]

    gh = GitHubClient()
    checkpointer = GitHubCheckpointer(gh)
    thread_id = f"intake-{user_id}"
    config = {"configurable": {"thread_id": thread_id}}

    existing = checkpointer.get_tuple(config)
    if existing:
        meta = existing.metadata or {}
        done = existing.checkpoint.get("channel_values", {}).get("done", False)

        stale = False
        ts_str = meta.get("written_at")
        if ts_str:
            written_at = datetime.fromisoformat(ts_str)
            stale = (datetime.now(tz=timezone.utc) - written_at) > timedelta(hours=_TIMEOUT_HOURS)

        if done or stale:
            checkpointer.delete(thread_id)

    graph = build_intake_graph(gh=gh, checkpointer=checkpointer)
    result = graph.invoke(
        {"messages": [HumanMessage(content=message)]},
        config=config,
    )

    last_msg = result["messages"][-1]
    return {
        "reply": getattr(last_msg, "content", ""),
        "done": result.get("done", False),
    }
