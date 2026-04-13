"""Lambda handler for the Planner agent (EventBridge 08:00)."""
from agents.planner.graph import PlannerState, build_planner_graph


def lambda_handler(event: dict, context) -> dict:
    graph = build_planner_graph()
    graph.invoke(
        PlannerState(
            active_skills=[],
            skip_state={},
            skill_trees={},
            unlocked={},
            daily_tasks=[],
        )
    )
    return {"status": "ok"}
