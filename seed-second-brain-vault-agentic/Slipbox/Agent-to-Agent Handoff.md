# Agent-to-Agent Handoff

**Tags:** #agentic-ai #multi-agent

**Related:** [[Hot Topics List in Agentic AI]] | [[Orchestrator-Worker Pattern]] | [[Shared State Management]]

---

## What is it?
The mechanism by which one agent transfers control (and context) to another agent mid-task.

## Why it's needed
No single agent should handle everything. Handoff allows specialization — Agent A handles intake, hands off to Agent B for deep analysis, then to Agent C for output formatting.

## What must be transferred

| Item | Why |
|---|---|
| Goal / task description | So the receiving agent knows *what* to do |
| Progress so far | Avoids re-doing completed steps |
| Relevant context | Key facts, retrieved docs, decisions made |
| Constraints | Time limits, budget caps, guardrails |

## Handoff patterns

### Explicit handoff
Orchestrator explicitly calls Agent B with a structured payload. Clean, auditable.

### Implicit handoff
Output of Agent A is fed as input to Agent B automatically (pipeline style). Simple but less flexible.

### Human-in-the-loop gate
Handoff pauses for human approval before Agent B starts. Good for high-stakes transitions.

## GroundSense analogy
If a GroundSense alert agent detected an anomaly and handed off to a "remediation agent" with the anomaly details + sensor history — that's a handoff.

## Key risk
**Context loss at handoff** — the receiving agent doesn't have enough context and starts from scratch. Always pass a structured summary, not raw chat history.
