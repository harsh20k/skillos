# Feedback Loops (Agent Design)

**Tags:** #agentic-ai #agent-design

**Related:** [[Hot Topics List in Agentic AI]] | [[Reflection Loops]] | [[Error Handling (Agents)]]

---

## What is it?
Mechanisms that route information about an agent's output quality *back* into the system to improve future behavior — either within a session or across sessions.

## Types of feedback loops

### In-session (short loop)
Agent gets immediate feedback after each action (tool result, error, human correction) and adjusts its next step.

### Post-run (medium loop)
After a full run completes, a critic or evaluator scores the output. Score can trigger a re-run or update the prompt.

### Cross-session (long loop)
Aggregate quality signals over many runs → update system prompt, fine-tune, or adjust retrieval logic.

## Feedback sources
- **Tool results** — did the tool return what was expected?
- **Human annotations** — thumbs up/down, corrections
- **LLM-as-Judge** — automated quality scoring
- **Downstream metrics** — did the action achieve its real-world goal?

## GroundSense analogy
If GroundSense's recommendation led to the wrong irrigation action, that outcome is feedback. Logging it and adjusting the prompt or retrieval is a feedback loop.

## Why it matters
Without feedback loops, agents don't improve — they repeat the same mistakes at scale.

## Pitfall
Feedback loops can introduce **reward hacking** — the agent optimizes for the feedback metric, not the actual goal. Monitor carefully.
