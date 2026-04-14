# Tool Orchestration

**Tags:** #agentic-ai #agent-design

**Related:** [[Hot Topics List in Agentic AI]] | [[State Design (Scratchpad)]] | [[Error Handling (Agents)]]

---

## What is it?
How an agent selects, sequences, and manages calls to external tools (APIs, databases, functions, other agents).

## Key decisions
- **Which tool to call** — driven by the LLM's reasoning or a router
- **When to call it** — sequential vs. parallel
- **What to pass** — argument construction from context
- **What to do with the result** — inject into next prompt or memory

## Patterns

### Sequential
Tool A → Tool B → Tool C. Safe, predictable, slow.

### Parallel
Call Tool A and Tool B simultaneously, merge results. Faster but requires dependency analysis.

### Conditional
If Tool A returns X, call Tool B; else call Tool C. Common in branching workflows.

## GroundSense analogy
GroundSense's 5 action groups are tools. The Bedrock Agent decides at each step which action group to invoke — that decision logic is tool orchestration.

## Common pitfalls
- Calling tools with hallucinated arguments
- Not handling tool timeouts gracefully
- Missing tool results being silently ignored
- Over-calling (redundant tool calls eating budget)

## Best practice
Define clear tool schemas with descriptions — the LLM selects tools based on their descriptions, so vague names = wrong calls.
