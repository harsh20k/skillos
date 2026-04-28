"""Shared fixtures for LLM evaluation tests.

Requires:
  LANGCHAIN_API_KEY  — to pull datasets from LangSmith
  GITHUB_TOKEN       — to run agents against GitHub state
  GITHUB_REPO        — e.g. harsh20k/skillos
  BEDROCK_MODEL_ID   — Bedrock model for agent invocations
"""
import os
import pytest


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "eval: LLM evaluation tests (slow, requires API keys)")
    config.addinivalue_line("markers", "langsmith: tests that pull from LangSmith datasets")


@pytest.fixture(scope="session")
def langsmith_client():
    """Return an authenticated LangSmith client, skip if API key missing."""
    api_key = os.environ.get("LANGCHAIN_API_KEY")
    if not api_key:
        pytest.skip("LANGCHAIN_API_KEY not set — skipping LangSmith eval tests")
    from langsmith import Client
    return Client()


@pytest.fixture(scope="session")
def eval_project_name():
    return os.environ.get("LANGSMITH_PROJECT", "skillos")
