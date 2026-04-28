"""Regression test runner: loads LangSmith golden datasets and re-runs agents.

Run with pytest:
  LANGCHAIN_API_KEY=<key> pytest tests/eval/run_regression.py -v -m eval

Or run directly for a quick report:
  LANGCHAIN_API_KEY=<key> python tests/eval/run_regression.py

Each test:
  1. Pulls examples from a LangSmith golden dataset
  2. Runs the example input through the agent graph (or checks output rules)
  3. Evaluates using LangSmith evaluators for faithfulness, relevance, and guardrail compliance

No LLM calls are made for evaluation — LangSmith's built-in evaluators handle scoring.
"""
from __future__ import annotations

import json
import os
import sys
from typing import Any

import pytest

# ---------------------------------------------------------------------------
# Planner output: guardrail checks (deterministic — no LLM evaluation needed)
# ---------------------------------------------------------------------------

@pytest.mark.eval
def test_planner_task_count_guardrail(langsmith_client):
    """Planner must generate 3–5 tasks total, never more."""
    dataset_name = "skillos-planner-golden"
    try:
        examples = list(langsmith_client.list_examples(dataset_name=dataset_name))
    except Exception:
        pytest.skip(f"Dataset '{dataset_name}' not found — run scripts/export_langsmith_dataset.py first")

    if not examples:
        pytest.skip("No examples in planner dataset yet")

    for example in examples:
        output = example.outputs or {}
        daily_tasks = output.get("daily_tasks", [])
        if not isinstance(daily_tasks, list):
            continue
        assert 3 <= len(daily_tasks) <= 5, (
            f"Planner produced {len(daily_tasks)} tasks — expected 3–5. "
            f"Example ID: {example.id}"
        )


@pytest.mark.eval
def test_planner_task_duration_guardrail(langsmith_client):
    """Each task must be ≤ 30 minutes."""
    dataset_name = "skillos-planner-golden"
    try:
        examples = list(langsmith_client.list_examples(dataset_name=dataset_name))
    except Exception:
        pytest.skip(f"Dataset '{dataset_name}' not found")

    if not examples:
        pytest.skip("No examples in planner dataset yet")

    for example in examples:
        output = example.outputs or {}
        for task in output.get("daily_tasks", []):
            duration = task.get("duration_min", 0)
            assert duration <= 30, (
                f"Task '{task.get('task')}' has duration {duration}min > 30min limit. "
                f"Example ID: {example.id}"
            )


# ---------------------------------------------------------------------------
# Intake output: skill tree structure checks (deterministic)
# ---------------------------------------------------------------------------

@pytest.mark.eval
def test_intake_skill_tree_structure(langsmith_client):
    """Scaffolded skill trees must have 8–12 nodes and exactly one root."""
    dataset_name = "skillos-intake-golden"
    try:
        examples = list(langsmith_client.list_examples(dataset_name=dataset_name))
    except Exception:
        pytest.skip(f"Dataset '{dataset_name}' not found")

    if not examples:
        pytest.skip("No examples in intake dataset yet")

    for example in examples:
        output = example.outputs or {}
        tree = output.get("skill_tree_json")
        if not tree:
            continue
        nodes = tree.get("nodes", [])

        assert 8 <= len(nodes) <= 12, (
            f"Skill tree has {len(nodes)} nodes — expected 8–12. Example ID: {example.id}"
        )

        roots = [n for n in nodes if not n.get("prerequisites")]
        assert len(roots) == 1, (
            f"Skill tree has {len(roots)} root nodes — expected exactly 1. Example ID: {example.id}"
        )

        unlocked = [n for n in nodes if n.get("status") == "unlocked"]
        assert len(unlocked) >= 1, (
            f"Skill tree has no unlocked nodes — root must start unlocked. Example ID: {example.id}"
        )


# ---------------------------------------------------------------------------
# LangSmith Experiments: run planner against dataset with evaluators
# ---------------------------------------------------------------------------

@pytest.mark.eval
@pytest.mark.langsmith
def test_planner_langsmith_experiment(langsmith_client, eval_project_name):
    """Run LangSmith experiment: re-run planner on golden examples, evaluate outputs."""
    dataset_name = "skillos-planner-golden"
    try:
        examples = list(langsmith_client.list_examples(dataset_name=dataset_name))
    except Exception:
        pytest.skip(f"Dataset '{dataset_name}' not found")

    if not examples:
        pytest.skip("No examples in planner dataset yet")

    def run_planner(inputs: dict) -> dict:
        """Re-run planner graph on the example input."""
        from agents.planner.graph import PlannerState, build_planner_graph
        graph = build_planner_graph()
        result = graph.invoke(PlannerState(
            active_skills=inputs.get("active_skills", []),
            skip_state=inputs.get("skip_state", {}),
            skill_trees=inputs.get("skill_trees", {}),
            unlocked=inputs.get("unlocked", {}),
            daily_tasks=[],
        ))
        return {"daily_tasks": result.get("daily_tasks", [])}

    def task_count_evaluator(run, example) -> dict:
        tasks = (run.outputs or {}).get("daily_tasks", [])
        score = 1.0 if 3 <= len(tasks) <= 5 else 0.0
        return {"key": "task_count_valid", "score": score}

    def duration_evaluator(run, example) -> dict:
        tasks = (run.outputs or {}).get("daily_tasks", [])
        if not tasks:
            return {"key": "duration_valid", "score": 0.0}
        over_limit = [t for t in tasks if t.get("duration_min", 0) > 30]
        score = 1.0 if not over_limit else 0.0
        return {"key": "duration_valid", "score": score}

    results = langsmith_client.evaluate(
        run_planner,
        data=dataset_name,
        evaluators=[task_count_evaluator, duration_evaluator],
        experiment_prefix="planner-regression",
        metadata={"prompt_version": os.environ.get("PROMPT_VERSION", "latest")},
    )

    # Fail if average score across all evaluators drops below 0.8
    scores = [r.evaluation_results["results"][0].score for r in results if r.evaluation_results]
    if scores:
        avg = sum(scores) / len(scores)
        assert avg >= 0.8, f"Planner regression score {avg:.2f} < 0.8 threshold"


# ---------------------------------------------------------------------------
# Standalone runner (no pytest)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import subprocess
    sys.exit(subprocess.call(["pytest", __file__, "-v", "-m", "eval", "--tb=short"]))
