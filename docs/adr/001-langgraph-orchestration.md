# ADR-001: Use LangGraph for Multi-Agent Orchestration

**Date:** 2026-04-13
**Status:** Accepted
**Deciders:** Harsh Pandey

---

## Context

SkillOS requires four agents (Intake, Planner, Skip Detector, Tracker) to coordinate around shared state. The initial design called for each agent to be a standalone Lambda with a single Anthropic SDK call, reconstructing context from GitHub/S3 on every invocation.

This works for simple single-shot LLM calls, but creates friction as agents grow more complex:

- Multi-step reasoning (e.g. Intake's clarification loop) requires manual state threading
- Tool-calling logic (read skill tree → decide → write tasks) must be hand-rolled
- No standard way to trace, replay, or debug agent runs
- Branching logic (e.g. "is goal specific enough? if not, ask again") is imperative code with no graph representation

We evaluated three options:

1. **Raw Anthropic SDK** — minimal deps, full control, but all orchestration is bespoke
2. **LangGraph** — graph-based state machine, built-in tool calling, checkpointing, and observability
3. **CrewAI** — higher-level abstraction, less control, less industry traction for serverless

---

## Decision

Use **LangGraph** with the **supervisor + subgraph** pattern.

Each agent becomes a `StateGraph` with typed state (`TypedDict`), explicit nodes, and conditional edges. A top-level `SupervisorGraph` routes incoming triggers to the appropriate subgraph.

```
SupervisorGraph
├── IntakeSubgraph     (clarify → assess → scaffold)
├── PlannerSubgraph    (read_state → generate_tasks → write_daily)
├── SkipDetectorNode   (pure logic, no LLM)
└── TrackerSubgraph    (validate → generate_note → commit)
```

LLM calls use **Claude 3.5 Sonnet via Amazon Bedrock** (`langchain-aws` `ChatBedrock`), authenticated via IAM — no API keys in code or environment variables.

**LangSmith** is enabled for all runs to provide tracing, token accounting, and node-level timing without custom logging infrastructure.

A **custom LangGraph checkpointer** (`checkpointer/github_checkpointer.py`) persists graph state as GitHub commits, preserving the "GitHub as memory" design principle while integrating cleanly with LangGraph's checkpointing interface.

---

## Consequences

### Positive

- Agent logic is expressed as an explicit, inspectable state machine rather than imperative code
- Tool-calling (read/write GitHub, S3) is handled by LangGraph's tool node — no manual retry/error handling
- LangSmith gives full observability out of the box — every run is traceable without custom logging
- Supervisor pattern is directly aligned with Anthropic's published multi-agent architecture recommendations
- Bedrock + IAM auth is more secure and AWS-native than direct Anthropic API key usage
- Custom GitHub checkpointer preserves the "every state change is a commit" design principle

### Negative

- LangGraph adds ~15 MB to Lambda package size (mitigated by Lambda layers)
- LangSmith requires an additional API key in Secrets Manager
- Custom checkpointer is non-trivial to implement correctly (must implement `BaseCheckpointSaver` interface)
- LangGraph's async model requires care with Lambda's execution context

### Neutral

- Stateless Lambda model is preserved — LangGraph graphs are instantiated fresh per invocation; checkpointer handles persistence
- GitHub + S3 remain the source of truth; LangGraph state is a working-memory layer on top

---

## Alternatives considered

### Raw Anthropic SDK

Rejected. Sufficient for single-shot calls but requires hand-rolling all orchestration, tool-calling, retry logic, and observability. Harder to maintain as agent complexity grows. Signals less architectural sophistication.

### CrewAI

Rejected. Higher-level abstraction reduces control over state management and tool routing. Smaller industry footprint than LangGraph for serverless/AWS deployments. Less alignment with the explicit state machine model we want.

---

## References

- [LangGraph multi-agent supervisor pattern](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/)
- [LangGraph custom checkpointers](https://langchain-ai.github.io/langgraph/how-tos/persistence_custom_storage/)
- [Anthropic multi-agent architecture patterns](https://www.anthropic.com/research/building-effective-agents)
- [LangChain AWS Bedrock integration](https://python.langchain.com/docs/integrations/chat/bedrock/)

