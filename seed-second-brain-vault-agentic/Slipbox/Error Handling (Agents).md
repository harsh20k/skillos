# Error Handling (Agents)

**Tags:** #agentic-ai #agent-design

**Related:** [[Hot Topics List in Agentic AI]] | [[Output Parsing (Agents)]] | [[When to Stop (Agent Loops)]]

---

## What is it?
How an agent detects, recovers from, or gracefully handles failures during execution — tool errors, parsing failures, timeouts, hallucinations.

## Error categories

| Error type | Example | Recovery |
|---|---|---|
| Tool failure | API timeout, 500 error | Retry with backoff |
| Parsing failure | LLM returned malformed JSON | Re-prompt with correction |
| Hallucinated tool args | Agent invents a parameter | Schema validation + rejection |
| Infinite loop | Agent keeps calling same tool | Max iterations guard |
| Out-of-scope | Agent tries to do something it shouldn't | Guardrails / refusal |

## Recovery patterns

### Retry
Re-attempt the failed step N times before escalating.

### Fallback
If primary tool fails, try an alternative (e.g., cached result).

### Graceful degradation
Return a partial result with a clear message rather than crashing.

### Error injection into context
Tell the agent what failed: *"Tool X returned error 429. Do not retry it. Use Tool Y instead."*

## GroundSense analogy
GroundSense uses CloudWatch alarms and guardrails — if an action group Lambda fails, Bedrock returns an error to the agent which can then decide to reroute.

## Best practice
- Treat errors as **observations** in the agent loop — feed them back so the agent can adapt
- Never silently swallow errors — the agent needs to know what happened
