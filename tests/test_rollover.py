"""Unit tests for Skip Detector rollover logic. No AWS, no LLM required."""
import json
from unittest.mock import MagicMock, patch

import pytest

import agents.skip_detector.rollover as rollover_mod
from agents.skip_detector.rollover import (
    MAX_ROLLOVER,
    _parse_incomplete_tasks,
    detect_and_write_rollover,
)


# ---------------------------------------------------------------------------
# _parse_incomplete_tasks
# ---------------------------------------------------------------------------

def test_parse_finds_incomplete_tasks():
    content = (
        "# Daily Tasks — 2026-04-13\n\n"
        "## Portrait Sketching\n\n"
        "- [ ] [25min] Draw 10 eyes from reference  `#fundamentals`\n"
        "- [x] [20min] Practice straight lines  `#lines`\n"
        "- [ ] [30min] Study facial proportions  `#proportions`\n"
    )
    tasks = _parse_incomplete_tasks(content)
    assert len(tasks) == 2
    assert tasks[0] == {"task": "Draw 10 eyes from reference", "duration_min": 25, "node_id": "fundamentals"}
    assert tasks[1]["node_id"] == "proportions"


def test_parse_empty_content():
    assert _parse_incomplete_tasks("") == []


def test_parse_all_done():
    content = "- [x] [25min] Completed task  `#node1`\n"
    assert _parse_incomplete_tasks(content) == []


# ---------------------------------------------------------------------------
# detect_and_write_rollover
# ---------------------------------------------------------------------------

def _make_gh(has_progress: bool, daily_content: str | None = None):
    gh = MagicMock()
    gh.get_file.side_effect = lambda path: (
        json.dumps([{"name": "portrait-sketching", "display_name": "Portrait Sketching"}])
        if path == "skills/active.json"
        else (daily_content or "")
    )
    gh.commit_exists_today.return_value = has_progress
    return gh


def test_rollover_caps_at_max():
    daily = (
        "- [ ] [25min] Task 1  `#node1`\n"
        "- [ ] [25min] Task 2  `#node2`\n"
        "- [ ] [25min] Task 3  `#node3`\n"
    )
    gh = _make_gh(has_progress=False, daily_content=daily)

    with patch.object(rollover_mod, "boto3") as mock_boto3:
        mock_boto3.client.return_value = MagicMock()
        result = detect_and_write_rollover(gh)

    assert "portrait-sketching" in result
    assert len(result["portrait-sketching"]["rollover_tasks"]) <= MAX_ROLLOVER


def test_no_rollover_when_progress_exists():
    gh = _make_gh(has_progress=True)

    with patch.object(rollover_mod, "boto3") as mock_boto3:
        mock_boto3.client.return_value = MagicMock()
        result = detect_and_write_rollover(gh)

    assert result == {}


def test_skip_state_written_to_s3():
    gh = _make_gh(has_progress=False, daily_content="- [ ] [25min] Task  `#node1`\n")
    mock_s3 = MagicMock()

    with patch.object(rollover_mod, "boto3") as mock_boto3:
        mock_boto3.client.return_value = mock_s3
        detect_and_write_rollover(gh)

    mock_s3.put_object.assert_called_once()
    call_kwargs = mock_s3.put_object.call_args.kwargs
    assert call_kwargs["Key"] == "skip_state.json"
    written = json.loads(call_kwargs["Body"].decode())
    assert "portrait-sketching" in written
