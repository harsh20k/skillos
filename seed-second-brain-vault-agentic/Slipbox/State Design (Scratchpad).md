# State Design (Scratchpad)

**Tags:** #agentic-ai #agent-design

**Related:** [[Hot Topics List in Agentic AI]] | [[Tool Orchestration]] | [[Context Window Bloat]]

---

## What is it?
Where and how an agent stores intermediate results, reasoning traces, and working memory during a task — its "scratchpad."

## Types of state

| Type | Where stored | Lifespan |
|---|---|---|
| **In-context** | System/user prompt | Single session |
| **External memory** | DB, vector store | Persistent |
| **Scratchpad** | Part of the prompt | Per loop iteration |
| **Structured state** | JSON object passed between steps | Per workflow run |

## Scratchpad pattern
The agent writes intermediate thoughts/results into a structured section of the prompt that gets carried forward each iteration.

```
[Scratchpad]
- Retrieved 3 docs about soil moisture
- Threshold exceeded at Zone B
- Need to check weather forecast next
```

## GroundSense analogy
Each Lambda invocation in GroundSense passes context forward via the session attributes in Bedrock — that's essentially a scratchpad between action group calls.

## Design principles
- Keep scratchpad **structured** (JSON > freeform text) for reliable parsing
- Prune stale entries — old intermediate results waste tokens
- Separate "facts gathered" from "decisions made"

## Risk
Unbounded scratchpad growth → context window bloat. Always cap or summarize.
