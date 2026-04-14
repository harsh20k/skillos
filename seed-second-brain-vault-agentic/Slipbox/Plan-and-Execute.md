# Plan-and-Execute

**Tags:** #agentic-ai #agent-loops

**Related:** [[Hot Topics List in Agentic AI]] | [[ReAct]] | [[Reflection Loops]]

---

## What is it?
A two-phase agent pattern:
1. **Plan** — LLM generates a full multi-step plan upfront
2. **Execute** — each step is carried out (often by a separate executor agent or tool)

## Flow
```
User Goal → Planner LLM → [Step 1, Step 2, Step 3...] → Executor → Result
```

## Vs. ReAct
| | ReAct | Plan-and-Execute |
|---|---|---|
| Planning | Step by step | Upfront |
| Adaptability | High | Low (re-plan needed) |
| Token use | Moderate | More upfront, less per step |
| Good for | Dynamic tasks | Structured, predictable tasks |

## GroundSense analogy
If GroundSense needed to "gather docs → analyze → write report → send email" in sequence, a planner would lay out all 4 steps before any execution begins.

## Weakness
If step 2 fails or returns unexpected output, the whole plan may be stale — requires a **re-planner** to handle deviations.

## When to use
- Long-horizon tasks with predictable sub-steps
- When you want visibility into what the agent *intends* to do before it acts
