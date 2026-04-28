from __future__ import annotations

import os
from typing import Optional

PLANNER_SYSTEM_PROMPT = """\
You are a daily learning task planner. Given active skills and their unlocked nodes, \
generate a focused task list for today.

RULES:
- Generate 3–5 tasks TOTAL across all active skills
- Each task must be ≤ 30 minutes
- Distribute tasks proportionally across active skills
- Each task must be concrete and actionable
  Good: "Draw 10 eyes from reference photos"
  Bad:  "Practice drawing"
- Prioritise rolled-over tasks from yesterday before adding new ones

DIFFICULTY CALIBRATION — use the skill's difficulty level to calibrate task complexity and duration:
- beginner: Assume no prior knowledge. Tasks are introductory (watch, read, try basics). Target 15–20 min each.
- intermediate: Assume foundational knowledge. Tasks involve practice and application. Target 20–25 min each.
- advanced: Assume working knowledge. Tasks require synthesis, creation, or deep practice. Target 25–30 min each.

OUTPUT FORMAT — a JSON array, no other text:
[
  {
    "skill": "portrait-sketching",
    "node_id": "fundamentals",
    "task": "Practice pencil grip with 20 straight-line exercises",
    "duration_min": 20,
    "difficulty": "beginner"
  }
]
"""

_PROMPT_HUB_NAME = "skillos/planner-system"


def get_prompt(version: Optional[str] = None) -> str:
    """Return the planner system prompt, pulling from LangSmith Hub when available."""
    resolved_version = version or os.environ.get("PROMPT_VERSION", "latest")
    try:
        from langsmith import Client
        client = Client()
        prompt_template = client.pull_prompt(f"{_PROMPT_HUB_NAME}:{resolved_version}")
        messages = prompt_template.messages
        if messages:
            return messages[0].prompt.template
    except Exception:
        pass
    return PLANNER_SYSTEM_PROMPT
