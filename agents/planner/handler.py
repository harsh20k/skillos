"""Lambda handler for the Planner agent (EventBridge 08:00).

The graph's entry node (load_state) reads active_skills from GitHub
and skip_state from S3, so no pre-populated state is needed here.
"""
from agents.planner.graph import build_planner_graph


def lambda_handler(event: dict, context) -> dict:
    graph = build_planner_graph()
    result = graph.invoke({
        "active_skills": [],
        "skip_state": {},
        "skill_trees": {},
        "unlocked": {},
        "daily_tasks": [],
    })
    skills_planned = [s["name"] for s in result.get("active_skills", [])]
    return {"status": "ok", "skills_planned": skills_planned}
