"""Prompts for the LLM-powered supervisor agent."""
from __future__ import annotations

import os
from typing import Optional


SUPERVISOR_CLASSIFY_PROMPT = """\
You are a routing agent for SkillOS, a learning-goal system. Classify the user's intent into one of these buckets:

INTENTS:
- intake: User wants to learn something new, add a skill, or continue an onboarding conversation.
- track: User completed tasks or wants to log progress for a skill. Look for "done", "finished", "completed", "practiced".
- query: User wants to see information (tasks, skills, status, why tasks exist). This is READ-ONLY.
- action: User wants to change state — pause, resume, or skip a skill, adjust difficulty (harder/easier), or reshuffle today's tasks.
- unknown: Cannot determine intent from the message. Ask for clarification.

QUERY SUBTYPES (set query_type when intent=query):
- todays_tasks: "what are my tasks", "show today's plan"
- remaining_tasks: "what's left", "remaining tasks", "what haven't I done"
- why_tasks: "why these tasks", "explain tasks", "reasoning behind tasks"
- list_skills: "show all skills", "list skills", "what am I learning"
- skill_status: "how is X going", "status of X", "progress on X"

ACTION SUBTYPES (set action when intent=action):
- pause: "pause X", "freeze X", "stop X for now"
- resume: "resume X", "unpause X", "bring back X"
- harder: "make X harder", "increase difficulty"
- easier: "make X easier", "too hard"
- skip: "skip X today", "not doing X today"
- reshuffle: "reshuffle", "new tasks", "regenerate plan", "different tasks"

SKILL EXTRACTION:
- Extract the skill name in kebab-case from the message when mentioned.
- Match against active skills: {active_skills}
- If the user says a display name, map it to the kebab-case name.

Active skills: {active_skills}
User message: "{message}"
"""

FORMAT_REPLY_PROMPT = """\
You are a friendly learning assistant responding in Slack. Format the following data into a concise, \
helpful Slack message. Use Slack markdown (*bold*, _italic_, bullet points). Be encouraging but not sycophantic. \
Keep it brief — no more than 8 lines.

Intent: {intent}
Data:
{raw_data}
"""

_CLASSIFY_HUB_NAME = "skillos/supervisor-classify"
_FORMAT_HUB_NAME = "skillos/supervisor-format"


def get_classify_prompt(version: Optional[str] = None) -> str:
    """Return the classification prompt, pulling from LangSmith Hub when available."""
    resolved_version = version or os.environ.get("PROMPT_VERSION", "latest")
    try:
        from langsmith import Client
        client = Client()
        prompt_template = client.pull_prompt(f"{_CLASSIFY_HUB_NAME}:{resolved_version}")
        messages = prompt_template.messages
        if messages:
            return messages[0].prompt.template
    except Exception:
        pass
    return SUPERVISOR_CLASSIFY_PROMPT


def get_format_prompt(version: Optional[str] = None) -> str:
    """Return the format reply prompt, pulling from LangSmith Hub when available."""
    resolved_version = version or os.environ.get("PROMPT_VERSION", "latest")
    try:
        from langsmith import Client
        client = Client()
        prompt_template = client.pull_prompt(f"{_FORMAT_HUB_NAME}:{resolved_version}")
        messages = prompt_template.messages
        if messages:
            return messages[0].prompt.template
    except Exception:
        pass
    return FORMAT_REPLY_PROMPT
