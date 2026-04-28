from __future__ import annotations

import os
from typing import Optional

TRACKER_SYSTEM_PROMPT = """\
You are a learning progress logger. The user has just completed tasks for a skill.

Write a concise progress note (2–4 sentences) that:
- Summarises what was practised
- Notes any apparent difficulty or observation
- Is encouraging but not sycophantic

Output ONLY the note text — no headers, no formatting, no preamble.
"""

_PROMPT_HUB_NAME = "skillos/tracker-system"


def get_prompt(version: Optional[str] = None) -> str:
    """Return the tracker system prompt, pulling from LangSmith Hub when available."""
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
    return TRACKER_SYSTEM_PROMPT
