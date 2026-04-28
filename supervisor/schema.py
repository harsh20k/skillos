"""Pydantic models for the LLM-powered supervisor agent."""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


class SupervisorDecision(BaseModel):
    """Structured output from the intent classification node."""

    intent: Literal["intake", "track", "query", "action", "unknown"] = Field(
        description="The classified intent bucket."
    )
    action: Optional[
        Literal["pause", "resume", "harder", "easier", "skip", "reshuffle"]
    ] = Field(
        default=None,
        description="Specific action to execute. Required when intent='action'.",
    )
    skill: Optional[str] = Field(
        default=None,
        description="Skill name extracted from the message (kebab-case). Null if not mentioned.",
    )
    query_type: Optional[
        Literal[
            "todays_tasks",
            "remaining_tasks",
            "why_tasks",
            "list_skills",
            "skill_status",
        ]
    ] = Field(
        default=None,
        description="Type of read-only query. Required when intent='query'.",
    )
    reasoning: str = Field(
        description="One-sentence explanation of classification for LangSmith traceability."
    )
