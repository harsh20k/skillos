# Shared State Management

**Tags:** #agentic-ai #multi-agent

**Related:** [[Hot Topics List in Agentic AI]] | [[Orchestrator-Worker Pattern]] | [[Agent-to-Agent Handoff]]

---

## What is it?
How multiple agents read from and write to a common state store without conflicting with each other.

## The problem
When two agents update the same state simultaneously, you get race conditions, stale reads, or corrupted state — the classic distributed systems problem, now applied to agents.

## State storage options

| Option | Best for |
|---|---|
| In-memory dict | Single-process, simple workflows |
| Redis / DynamoDB | Multi-agent, low-latency shared access |
| Message queue (SQS) | Async state passing between agents |
| Vector DB | Shared semantic memory / knowledge |

## Consistency strategies
- **Optimistic locking** — each agent reads a version number; write fails if version changed since read
- **Single writer** — only the orchestrator writes; workers read only
- **Event sourcing** — agents emit events; state is rebuilt from the event log (auditable)

## GroundSense analogy
If GroundSense had multiple agents updating a "field status" record simultaneously (soil agent + weather agent), they'd need locking or a single-writer pattern to avoid overwriting each other's updates.

## Best practice
- Prefer **immutable state + append-only logs** over mutable shared objects
- Treat shared state like a database — use transactions or atomic operations
- Always version your shared state objects

## Key risk
Deadlock — Agent A waits for Agent B to release a lock, which is waiting for Agent A. Use timeouts.
