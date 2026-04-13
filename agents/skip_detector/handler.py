"""Lambda handler for the Skip Detector (EventBridge 23:00)."""
from agents.skip_detector.rollover import detect_and_write_rollover
from shared.github_client import GitHubClient


def lambda_handler(event: dict, context) -> dict:
    gh = GitHubClient()
    skip_state = detect_and_write_rollover(gh)
    return {"status": "ok", "skipped": list(skip_state.keys())}
