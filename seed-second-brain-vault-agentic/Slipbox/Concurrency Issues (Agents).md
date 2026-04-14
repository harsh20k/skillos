# Concurrency Issues (Agents)

**Tags:** #agentic-ai #prod-vs-local

**Related:** [[Hot Topics List in Agentic AI]] | [[Shared State Management]] | [[Cold Starts (Agentic AI)]]

---

## What is it?
Problems that arise when multiple agent instances run simultaneously — sharing state, hitting rate limits, or producing conflicting outputs.

## Common issues

### Race conditions
Two agents read the same state, both compute an update, one overwrites the other's result.

### Rate limit collisions
Multiple agents hammering the same LLM API or tool simultaneously → 429 errors.

### Duplicate actions
Two agents both decide to send the same email / trigger the same alert.

### Inconsistent context
Agent A's output is used by Agent B before Agent A finishes → B acts on stale data.

## GroundSense analogy
If 10 fields trigger alerts simultaneously, 10 GroundSense agent invocations run concurrently. Without concurrency controls, they could all try to update the same DynamoDB record or exhaust Lambda concurrency limits.

## Mitigation strategies
- **Idempotency keys** — tag each agent run; detect and skip duplicate actions
- **Distributed locks** (Redis, DynamoDB conditional writes) — prevent simultaneous writes
- **Rate limiting / throttling** — queue excess requests instead of hitting API limits
- **Single-writer pattern** — only one agent writes; others read

## Local vs Prod difference
Locally you test one request at a time. In prod, concurrency is the default — design for it from the start.
