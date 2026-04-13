"""Lambda handler for the Intake agent.

Triggered by Slack /learn command (via Slack bot Lambda).
Uses the GitHub checkpointer to maintain conversation state across invocations.
"""
from langchain_core.messages import HumanMessage

from agents.intake.graph import build_intake_graph
from checkpointer.github_checkpointer import GitHubCheckpointer
from shared.github_client import GitHubClient


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
    graph = build_intake_graph(gh=gh, checkpointer=checkpointer)

    config = {"configurable": {"thread_id": f"intake-{user_id}"}}
    result = graph.invoke(
        {"messages": [HumanMessage(content=message)]},
        config=config,
    )

    last_msg = result["messages"][-1]
    return {
        "reply": getattr(last_msg, "content", ""),
        "done": result.get("done", False),
    }
