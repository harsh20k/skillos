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
from datetime import date, datetime
from typing import Any, Dict, Iterator, Optional, Sequence
from uuid import UUID

from langchain_core.messages import BaseMessage, message_to_dict
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.base import (
    BaseCheckpointSaver,
    Checkpoint,
    CheckpointMetadata,
    CheckpointTuple,
)

from shared.github_client import GitHubClient


def _json_safe(obj: Any) -> Any:
    """Recursively convert values so json.dumps can persist GitHub checkpoint envelopes.

    LangGraph checkpoint metadata (and nested structures) may contain BaseMessage
    instances that are not JSON-serializable.
    """
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return obj
    if isinstance(obj, BaseMessage):
        return message_to_dict(obj)
    if isinstance(obj, dict):
        return {str(k): _json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_json_safe(x) for x in obj]
    if isinstance(obj, set):
        return [_json_safe(x) for x in obj]
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, UUID):
        return str(obj)
    if hasattr(obj, "model_dump") and callable(obj.model_dump):
        try:
            return _json_safe(obj.model_dump())
        except Exception:
            pass
    if hasattr(obj, "dict") and callable(obj.dict):
        try:
            return _json_safe(obj.dict())
        except Exception:
            pass
    return str(obj)


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
        meta_raw: dict = {} if metadata is None else dict(metadata)

        envelope = {
            "thread_id": thread_id,
            "checkpoint_id": checkpoint_id,
            "checkpoint": self._serialize(checkpoint),
            "metadata": _json_safe(meta_raw),
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

    def put_writes(
        self,
        config: RunnableConfig,
        writes: Sequence[tuple[str, Any]],
        task_id: str,
        task_path: str = "",
    ) -> None:
        """Persist intermediate task writes.

        This checkpointer stores only the latest checkpoint envelope in GitHub and
        does not currently materialize pending writes separately.
        """
        return None

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
