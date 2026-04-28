from __future__ import annotations

import os
from typing import Optional
from pydantic import BaseModel, Field


INTAKE_SYSTEM_PROMPT = """\
You are a learning coach helping a user build a structured skill tree.

Your job: understand the user's learning goal precisely, then scaffold a skill tree.

CLARIFICATION RULES:
- If the goal is vague (e.g. "get better at X"), ask ONE focused question to sharpen it.
- Ask at most 2–3 clarifying questions before deciding you have enough to proceed.
- When you have enough specificity, set ready=true and include the skill tree.
- If clarification_turns >= 5, you MUST set ready=true and produce the skill tree now.

SKILL TREE FORMAT — when ready=true, populate skill_tree:
{
  "skill_name": "kebab-case-name",
  "display_name": "Human Readable Name",
  "nodes": [
    {
      "id": "node-id",
      "label": "What the user does in one session",
      "prerequisites": [],
      "duration_min": 25,
      "status": "unlocked"
    }
  ]
}

CONSTRAINTS on the skill tree:
- Each node: 20–30 minutes
- 8–12 nodes total
- Exactly one root node (prerequisites: []), status "unlocked"; all others "locked"
- Node IDs are kebab-case

OUTPUT: Respond ONLY with a JSON object matching the schema provided. No markdown, no prose.
"""

# Signal kept for backward compatibility but no longer used for routing
READY_SIGNAL = "[READY]"

_PROMPT_HUB_NAME = "skillos/intake-system"


def get_prompt(version: Optional[str] = None) -> str:
    """Return the intake system prompt.

    Pulls from LangSmith Prompt Hub when LANGCHAIN_API_KEY is set.
    Falls back to the hardcoded INTAKE_SYSTEM_PROMPT on any error.

    Version resolution order:
      1. `version` argument
      2. PROMPT_VERSION env var (set per Lambda alias for A/B testing)
      3. "latest"
    """
    resolved_version = version or os.environ.get("PROMPT_VERSION", "latest")
    try:
        from langsmith import Client
        client = Client()
        prompt_template = client.pull_prompt(f"{_PROMPT_HUB_NAME}:{resolved_version}")
        # pull_prompt returns a ChatPromptTemplate; extract system message content
        messages = prompt_template.messages
        if messages:
            return messages[0].prompt.template
    except Exception:
        pass
    return INTAKE_SYSTEM_PROMPT


class ClarifyResponse(BaseModel):
    """Structured output from the intake clarify node."""

    ready: bool = Field(
        description="True when enough information exists to scaffold the skill tree."
    )
    reply: str = Field(
        description="The message to send to the user (a question, or a confirmation when ready)."
    )
    skill_tree: Optional[dict] = Field(
        default=None,
        description="The full skill tree JSON. Required when ready=true, null otherwise.",
    )
