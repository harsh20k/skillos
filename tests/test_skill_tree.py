"""Unit tests for skill tree DAG parsing and node unlock logic."""
import json

import pytest

from agents.planner.skill_tree import get_unlocked_nodes, mark_node_done, parse_skill_tree

# Embedded backtick fences are fine in Python triple-quoted strings
SAMPLE_TREE_MD = """# Skill Tree: Portrait Sketching

```json
{
  "skill_name": "portrait-sketching",
  "display_name": "Portrait Sketching",
  "nodes": [
    {"id": "fundamentals", "label": "Pencil fundamentals", "prerequisites": [],               "duration_min": 25, "status": "unlocked"},
    {"id": "shapes",       "label": "Basic shapes",        "prerequisites": ["fundamentals"], "duration_min": 25, "status": "locked"},
    {"id": "proportions",  "label": "Facial proportions",  "prerequisites": ["shapes"],       "duration_min": 30, "status": "locked"},
    {"id": "eyes",         "label": "Drawing eyes",        "prerequisites": ["proportions"],  "duration_min": 25, "status": "locked"}
  ]
}
```
"""


# ---------------------------------------------------------------------------
# parse_skill_tree
# ---------------------------------------------------------------------------

def test_parse_extracts_json():
    tree = parse_skill_tree(SAMPLE_TREE_MD)
    assert tree["skill_name"] == "portrait-sketching"
    assert len(tree["nodes"]) == 4


def test_parse_raises_on_missing_json():
    with pytest.raises(ValueError, match="No JSON block"):
        parse_skill_tree("# No JSON here")


# ---------------------------------------------------------------------------
# get_unlocked_nodes
# ---------------------------------------------------------------------------

def test_unlocked_returns_root_only():
    tree = parse_skill_tree(SAMPLE_TREE_MD)
    unlocked = get_unlocked_nodes(tree)
    assert len(unlocked) == 1
    assert unlocked[0]["id"] == "fundamentals"


def test_unlocked_empty_when_all_locked():
    tree = {
        "nodes": [
            {"id": "a", "prerequisites": ["b"], "status": "unlocked"},
        ]
    }
    # No node is "done", so even though "a" is unlocked its prereq "b" is absent → not returned
    assert get_unlocked_nodes(tree) == []


# ---------------------------------------------------------------------------
# mark_node_done
# ---------------------------------------------------------------------------

def test_mark_done_updates_status():
    tree = parse_skill_tree(SAMPLE_TREE_MD)
    tree = mark_node_done(tree, "fundamentals")
    node = next(n for n in tree["nodes"] if n["id"] == "fundamentals")
    assert node["status"] == "done"


def test_mark_done_unlocks_direct_dependent():
    tree = parse_skill_tree(SAMPLE_TREE_MD)
    tree = mark_node_done(tree, "fundamentals")
    shapes = next(n for n in tree["nodes"] if n["id"] == "shapes")
    assert shapes["status"] == "unlocked"


def test_mark_done_does_not_unlock_transitive():
    """Completing fundamentals must NOT unlock proportions (requires shapes first)."""
    tree = parse_skill_tree(SAMPLE_TREE_MD)
    tree = mark_node_done(tree, "fundamentals")
    proportions = next(n for n in tree["nodes"] if n["id"] == "proportions")
    assert proportions["status"] == "locked"


def test_chain_unlock():
    """Completing fundamentals then shapes should unlock proportions."""
    tree = parse_skill_tree(SAMPLE_TREE_MD)
    tree = mark_node_done(tree, "fundamentals")
    tree = mark_node_done(tree, "shapes")
    proportions = next(n for n in tree["nodes"] if n["id"] == "proportions")
    assert proportions["status"] == "unlocked"
