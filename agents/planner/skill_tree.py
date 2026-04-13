"""Parse skill-tree.md into a DAG dict and compute node unlock state."""
import json
import re


def parse_skill_tree(content: str) -> dict:
    """Extract the JSON block from a skill-tree.md file."""
    match = re.search(r"```json\s*([\s\S]+?)\s*```", content)
    if not match:
        raise ValueError("No JSON block found in skill-tree.md")
    return json.loads(match.group(1))


def get_unlocked_nodes(tree: dict) -> list[dict]:
    """Return nodes whose prerequisites are all marked done/completed."""
    nodes: list[dict] = tree.get("nodes", [])
    done_ids = {n["id"] for n in nodes if n.get("status") in ("done", "completed")}
    return [
        n
        for n in nodes
        if n.get("status") == "unlocked"
        and set(n.get("prerequisites", [])).issubset(done_ids)
    ]


def mark_node_done(tree: dict, node_id: str) -> dict:
    """Mark node_id as done and unlock any nodes whose prerequisites are now satisfied."""
    nodes: list[dict] = tree["nodes"]

    for node in nodes:
        if node["id"] == node_id:
            node["status"] = "done"
            break

    done_ids = {n["id"] for n in nodes if n.get("status") in ("done", "completed")}

    for node in nodes:
        if node.get("status") == "locked":
            if set(node.get("prerequisites", [])).issubset(done_ids):
                node["status"] = "unlocked"

    return tree
