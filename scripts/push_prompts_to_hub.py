#!/usr/bin/env python3
"""One-time script to upload current SkillOS prompts to LangSmith Prompt Hub.

Run from the repo root:
  LANGCHAIN_API_KEY=<key> python scripts/push_prompts_to_hub.py

After running, prompts appear in LangSmith under the 'skillos' namespace.
Agents will pull these at runtime via get_prompt() in each prompt.py module.

To create a new version (e.g. for A/B testing):
  1. Edit the prompt string below (or edit in LangSmith UI)
  2. Re-run this script — LangSmith creates a new commit/version automatically
  3. Deploy a Lambda alias with PROMPT_VERSION=<commit-hash> to route traffic to it
"""
import sys
import os

# Ensure repo root is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate

from agents.intake.prompt import INTAKE_SYSTEM_PROMPT
from agents.planner.prompt import PLANNER_SYSTEM_PROMPT
from agents.tracker.prompt import TRACKER_SYSTEM_PROMPT

PROMPTS = {
    "skillos/intake-system": INTAKE_SYSTEM_PROMPT,
    "skillos/planner-system": PLANNER_SYSTEM_PROMPT,
    "skillos/tracker-system": TRACKER_SYSTEM_PROMPT,
}


def push_all():
    client = Client()
    for hub_name, content in PROMPTS.items():
        template = ChatPromptTemplate.from_messages([("system", content)])
        client.push_prompt(hub_name, object=template, is_public=False)
        print(f"Pushed: {hub_name}")
    print("\nDone. View prompts at https://smith.langchain.com/hub")


if __name__ == "__main__":
    push_all()
