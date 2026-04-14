# Reflection Loops

**Tags:** #agentic-ai #agent-loops

**Related:** [[Hot Topics List in Agentic AI]] | [[ReAct]] | [[When to Stop]]

---

## What is it?
After producing an output, the agent (or a separate critic LLM) **evaluates its own work** and decides whether to revise it.

## Loop Structure
```
Generate → Reflect/Critique → Revise → Reflect → ... → Accept
```

## Two flavours
- **Self-reflection** — same LLM critiques its own output in a follow-up prompt
- **Critic agent** — a separate LLM acts as a judge (LLM-as-Judge pattern)

## Why it matters
LLMs are better at *finding flaws in existing text* than producing perfect text on the first pass. Reflection exploits this asymmetry.

## GroundSense analogy
Imagine GroundSense generating a site risk report, then passing it to a second prompt that asks: *"Is this report complete? What's missing?"* — that second pass is a reflection loop.

## Risks
- Can loop indefinitely without a stopping condition
- Critic can be sycophantic (agrees with everything)
- Adds latency and token cost per iteration

## When to use
- High-stakes outputs (reports, code, summaries)
- When first-pass quality is consistently insufficient
