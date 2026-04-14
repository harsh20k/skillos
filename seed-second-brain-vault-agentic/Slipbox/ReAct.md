# ReAct

**Tags:** #agentic-ai #agent-loops

**Related:** [[Hot Topics List in Agentic AI]] | [[Plan-and-Execute]] | [[Reflection Loops]]

---

## What is it?
ReAct = **Reasoning + Acting**. The agent interleaves *thinking* (reasoning trace) with *acting* (tool calls) in a tight loop.

## Loop Structure
```
Thought → Action → Observation → Thought → Action → ...
```

1. **Thought** — LLM reasons about what to do next
2. **Action** — calls a tool (search, API, function)
3. **Observation** — receives tool output
4. Repeat until answer found

## Why it works
The reasoning trace keeps the model "on track" — it doesn't jump straight to answers. Each observation updates context for the next thought.

## GroundSense analogy
Every Bedrock Agent invocation follows this pattern — the agent decides which action group to call, gets a result, then reasons about the next step before responding.

## Limitations
- Reasoning traces consume tokens fast
- Can get stuck in loops if observations are uninformative
- No global plan — purely reactive, step by step

## When to use
- Tasks where the next step depends on what you just learned
- Dynamic, unpredictable environments

## The Reasoning Step (Deep Dive)

The **Thought** step is the LLM generating text *before* committing to a tool call — essentially the agent talking to itself.

### What happens during reasoning:
1. **Interpret** — parse the last observation / current state
2. **Plan** — decide which tool to call and with what input
3. **Decide** — check if the goal is already met (stop?) or another action is needed

### In practice
In LangChain / Bedrock Agents, this appears as a `Thought:` prefix in the scratchpad. It's not a separate module — it's the LLM's chain-of-thought before the action token.

> *"The user wants X. I have Y. I should call tool Z to get the missing piece."*

### Key insight
Reasoning ≠ planning a full sequence upfront. It's a **local, one-step decision** made fresh after each observation. This is why ReAct is reactive — not strategic like [[Plan-and-Execute]].
