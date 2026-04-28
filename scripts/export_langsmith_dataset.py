#!/usr/bin/env python3
"""Export real LangSmith run traces into golden regression datasets.

Run from the repo root:
  LANGCHAIN_API_KEY=<key> python scripts/export_langsmith_dataset.py

For each agent type (intake, planner, tracker) this script:
  1. Queries recent successful runs from the LangSmith project
  2. Extracts input/output pairs
  3. Creates (or updates) a LangSmith dataset with those examples

The datasets are used by tests/eval/run_regression.py for regression testing
and by LangSmith Experiments for prompt comparison.

Optional env vars:
  LANGSMITH_PROJECT   — project name (default: "skillos")
  EXPORT_LIMIT        — max runs to export per agent (default: 50)
"""
import os
import sys
from datetime import datetime, timedelta, timezone

from langsmith import Client

PROJECT = os.environ.get("LANGSMITH_PROJECT", "skillos")
LIMIT = int(os.environ.get("EXPORT_LIMIT", "50"))

# LangSmith dataset names
DATASETS = {
    "intake": "skillos-intake-golden",
    "planner": "skillos-planner-golden",
    "tracker": "skillos-tracker-golden",
}

# Run name patterns to match per agent (LangSmith traces include the graph node names)
RUN_NAME_PATTERNS = {
    "intake": ["IntakeSubgraph", "intake", "clarify"],
    "planner": ["PlannerSubgraph", "planner", "generate_tasks"],
    "tracker": ["TrackerSubgraph", "tracker", "generate_note"],
}


def _get_or_create_dataset(client: Client, name: str, description: str) -> str:
    """Return dataset ID, creating it if it doesn't exist."""
    try:
        dataset = client.read_dataset(dataset_name=name)
        return dataset.id
    except Exception:
        dataset = client.create_dataset(dataset_name=name, description=description)
        return dataset.id


def _extract_io(run) -> tuple[dict, dict] | None:
    """Extract a clean input/output pair from a LangSmith run."""
    try:
        inputs = run.inputs or {}
        outputs = run.outputs or {}
        if not inputs or not outputs:
            return None
        return dict(inputs), dict(outputs)
    except Exception:
        return None


def export_agent(client: Client, agent: str, dataset_name: str) -> int:
    """Export runs for one agent into a LangSmith dataset. Returns count added."""
    dataset_id = _get_or_create_dataset(
        client,
        dataset_name,
        f"Golden regression examples for SkillOS {agent} agent",
    )

    since = datetime.now(tz=timezone.utc) - timedelta(days=30)

    # Fetch runs matching agent patterns
    added = 0
    for pattern in RUN_NAME_PATTERNS[agent]:
        try:
            runs = list(client.list_runs(
                project_name=PROJECT,
                run_type="chain",
                filter=f'eq(status, "success")',
                execution_order=1,
                limit=LIMIT,
                start_time=since,
            ))
        except Exception as exc:
            print(f"  Warning: could not fetch runs for pattern '{pattern}': {exc}")
            continue

        for run in runs:
            if not (run.name and any(p.lower() in run.name.lower() for p in RUN_NAME_PATTERNS[agent])):
                continue
            pair = _extract_io(run)
            if pair is None:
                continue
            inputs, outputs = pair
            try:
                client.create_example(
                    inputs=inputs,
                    outputs=outputs,
                    dataset_id=dataset_id,
                    source_run_id=run.id,
                )
                added += 1
            except Exception:
                # Example may already exist (duplicate source_run_id) — skip
                continue

        if added > 0:
            break  # Found runs with this pattern, no need to try other patterns

    return added


def main():
    client = Client()
    print(f"Exporting LangSmith runs from project '{PROJECT}' (last 30 days, limit {LIMIT}/agent)\n")

    total = 0
    for agent, dataset_name in DATASETS.items():
        count = export_agent(client, agent, dataset_name)
        print(f"  {agent:10s} → {dataset_name}: {count} examples added")
        total += count

    print(f"\nTotal: {total} examples exported.")
    print("View datasets at https://smith.langchain.com/datasets")


if __name__ == "__main__":
    main()
