# Orchestrator/Worker Pattern

**Tags:** #agentic-ai #multi-agent

**Related:** [[Hot Topics List in Agentic AI]] | [[Agent-to-Agent Handoff]] | [[Shared State Management]]

---

## What is it?
A multi-agent architecture where one **orchestrator agent** plans and delegates, and multiple **worker agents** execute specific subtasks independently.

## Structure
```
User → Orchestrator
         ├── Worker A (research)
         ├── Worker B (write)
         └── Worker C (validate)
              → Orchestrator aggregates → Final output
```

## Orchestrator responsibilities
- Decompose the goal into subtasks
- Assign subtasks to appropriate workers
- Collect and merge results
- Decide if re-work is needed

## Worker responsibilities
- Execute one focused task
- Return a structured result
- No awareness of the broader goal

## GroundSense analogy
Imagine a "master GroundSense agent" that calls specialized sub-agents: one for soil analysis, one for weather lookup, one for irrigation scheduling. The master orchestrates; each specialist executes.

## Benefits
- Workers can run **in parallel** → faster execution
- Workers are **swappable** → easy to upgrade one capability
- Orchestrator stays focused on coordination, not execution

## Pitfall
Orchestrator becomes a bottleneck. If it hallucinates a bad delegation decision, all workers execute the wrong thing.
