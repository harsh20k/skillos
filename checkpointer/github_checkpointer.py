"""
Custom LangGraph checkpointer backed by GitHub commits.

Each checkpoint is stored as a JSON file at:
  .langgraph/{thread_id}/latest.json

Every save = one GitHub commit, preserving the
"every state change is a commit" invariant from the core design.

Implements the BaseCheckpointSaver interface (langgraph 0.2.x).
"""
from __future__ import annotations

import base64
import json
from typing import Any, Dict, Iterator, Optional

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.base import (
    BaseCheckpointSaver,
    Checkpoint,
    CheckpointMetadata,
    CheckpointTuple,
)

from shared.github_client import GitHubClient


class GitHubCheckpointer(BaseCheckpointSaver):
    def __init__(self, gh: Optional[GitHubClient] = None) -> None:
        super().__init__()
        self._gh = gh or GitHubClient()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _path(self, thread_id: str) -> str:
        return f".langgraph/{thread_id}/latest.json"

    def _serialize(self, checkpoint: Checkpoint) -> dict:
        type_str, data = self.serde.dumps_typed(checkpoint)
        return {
            "type": type_str,
            "data": base64.b64encode(data).decode("ascii"),
        }

    def _deserialize(self, stored: dict) -> Checkpoint:
        data_bytes = base64.b64decode(stored["data"])
        return self.serde.loads_typed((stored["type"], data_bytes))

    # ------------------------------------------------------------------
    # BaseCheckpointSaver interface
    # ------------------------------------------------------------------

    def get_tuple(self, config: RunnableConfig) -> Optional[CheckpointTuple]:
        thread_id: str = config["configurable"].get("thread_id", "default")
        try:
            raw = self._gh.get_file(self._path(thread_id))
            envelope = json.loads(raw)
            checkpoint = self._deserialize(envelope["checkpoint"])
            metadata: CheckpointMetadata = envelope.get("metadata", {})
            return CheckpointTuple(
                config=config,
                checkpoint=checkpoint,
                metadata=metadata,
                parent_config=None,
                pending_writes=None,
            )
        except Exception:
            return None

    def put(
        self,
        config: RunnableConfig,
        checkpoint: Checkpoint,
        metadata: CheckpointMetadata,
        new_versions: Any,
    ) -> RunnableConfig:
        thread_id: str = config["configurable"].get("thread_id", "default")
        checkpoint_id: str = checkpoint.get("id", "unknown")

        envelope = {
            "thread_id": thread_id,
            "checkpoint_id": checkpoint_id,
            "checkpoint": self._serialize(checkpoint),
            "metadata": dict(metadata),
        }

        self._gh.write_file(
            self._path(thread_id),
            json.dumps(envelope, indent=2),
            f"checkpoint: {thread_id} @ {checkpoint_id[:8]}",
        )

        return {
            **config,
            "configurable": {
                **config.get("configurable", {}),
                "checkpoint_id": checkpoint_id,
            },
        }

    def list(
        self,
        config: Optional[RunnableConfig],
        *,
        filter: Optional[Dict[str, Any]] = None,
        before: Optional[RunnableConfig] = None,
        limit: Optional[int] = None,
    ) -> Iterator[CheckpointTuple]:
        # Minimal implementation: yield the single latest checkpoint per thread
        if config is None:
            return
        result = self.get_tuple(config)
        if result is not None:
            yield result
