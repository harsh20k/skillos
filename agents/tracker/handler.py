"""Lambda handler for the Tracker agent (Slack /done command via API Gateway)."""
from agents.tracker.graph import TrackerState, build_tracker_graph
from shared.github_client import GitHubClient


def lambda_handler(event: dict, context) -> dict:
    """
    Expected event:
      {"skill": "portrait-sketching", "user_id": "U123ABC", "context": "finished eye exercises"}

    Returns:
      {"status": "ok", "note": "...", "unlocked": [...]}
      {"status": "error", "message": "..."}
    """
    skill = event.get("skill", "").strip()
    if not skill:
        return {"status": "error", "message": "skill is required"}

    gh = GitHubClient()
    graph = build_tracker_graph(gh=gh)
    result = graph.invoke(
        TrackerState(
            skill=skill,
            user_id=event.get("user_id", "unknown"),
            context=event.get("context", ""),
            progress_note="",
            skill_tree={},
            completed_node_ids=[],
            unlocked_nodes=[],
            error=None,
        )
    )

    if result.get("error"):
        return {"status": "error", "message": result["error"]}

    return {
        "status": "ok",
        "note": result.get("progress_note", ""),
        "unlocked": result.get("unlocked_nodes", []),
    }
