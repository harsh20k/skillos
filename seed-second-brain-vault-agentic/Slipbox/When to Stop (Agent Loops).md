# When to Stop (Agent Loops)

**Tags:** #agentic-ai #agent-loops

**Related:** [[Hot Topics List in Agentic AI]] | [[ReAct]] | [[Reflection Loops]]

---

## The problem
Without a stopping condition, agents loop forever — burning tokens, hitting rate limits, or producing contradictory outputs.

## Stopping strategies

### 1. Max iterations
Hard cap on steps. Simple but blunt — agent may stop mid-task.

### 2. Terminal token / finish signal
Agent emits a special token like `FINAL ANSWER:` to signal completion. Used in ReAct.

### 3. Goal satisfaction check
After each step, a validator checks: *"Is the original goal met?"*

### 4. Confidence threshold
Agent or critic assigns a score; stop when score ≥ threshold.

### 5. Human-in-the-loop gate
For high-risk actions, pause and ask a human before continuing.

## GroundSense analogy
Bedrock Agents have a max iterations setting — if the agent can't resolve the user query in N steps, it returns a fallback response rather than looping.

## Best practice
Use **layered stopping**: max iterations as a hard safety net + semantic finish signal as the preferred exit. Never rely on only one.

## Failure modes
- Too aggressive stopping → incomplete answers
- Too lenient → infinite loops, cost blowups
