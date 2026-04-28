"""Lambda entry point for the LLM-powered supervisor agent.

Invoked by the Slack bot Lambda via /skillos command.

Event payload:
  {"message": "what are my tasks today?", "user_id": "U12345"}

Returns:
  {"reply": "Here are your tasks for today..."}
"""
from __future__ import annotations

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: dict, context) -> dict:
    from supervisor.graph import build_supervisor_graph

    message = event.get("message", "")
    user_id = event.get("user_id", "default")

    if not message:
        return {"reply": "Usage: `/skillos <what you want to do>`\nExamples: 'show my tasks', 'I finished portrait practice', 'pause public-speaking'"}

    logger.info("Supervisor invoked: user=%s message=%s", user_id, message[:100])

    graph = build_supervisor_graph()
    result = graph.invoke({
        "message": message,
        "user_id": user_id,
        "active_skills": [],
        "decision": None,
        "raw_data": None,
        "reply": "",
    })

    reply = result.get("reply", "Something went wrong. Try a specific command like `/todays-tasks`.")
    logger.info("Supervisor reply: %s", reply[:200])

    return {"reply": reply}
