# Agent Framework Landscape (2026)

From Pavan's lecture — six options mapped by control vs abstraction.

## The options

| Option | Type | Key trait |
|---|---|---|
| DIY / No framework | DIY | Direct LLM API + own tool orchestration. Maximum control. |
| MCP | Protocol | "USB-C for AI." 97M+ downloads. JSON-RPC 2.0. NOT a framework — composes with everything. |
| LangGraph | Framework | Graph-based state machines. Cyclic graphs, checkpoints, HITL. Used by LinkedIn, Uber, Klarna. |
| CrewAI / n8n | Framework | Role-based crews (autonomous) + flows (deterministic). 100K+ devs. Easier onboarding. |
| OpenAI Agents SDK | Framework | Agents, handoffs, guardrails, sessions. Successor to Swarm. 100+ LLMs. OpenAI-leaning. |
| MS Agent Framework | Framework | AutoGen + Semantic Kernel merged (Oct 2025). .NET + Python. Azure-leaning. |

## Key mental model: these compose, not compete

- **MCP** is a protocol — any framework can consume MCP tools
- **LangGraph** is the orchestration engine — it calls LLMs, manages graph state
- **LiteLLM** sits under LangGraph to keep the LLM provider swappable
- **K8s** is the deployment layer — turns agent graph nodes into independently scalable pods
- **Spring Boot** is the public-facing gateway — auth, routing, rate limiting

## Why LangGraph for Project 3 (Multi-Agent Swarm on K8s)

- Production-grade: used at LinkedIn, Uber, Klarna
- Stateful graph: supports retries, checkpointing, human-in-the-loop (HITL)
- Each graph node maps naturally to a K8s pod
- Platform-agnostic: no cloud vendor lock-in
- CrewAI/n8n are simpler but not K8s-grade
- OpenAI SDK and MS Framework lean toward specific vendors — defeats platform-agnostic goal

## Your Project 3 stack
```
MCP (tool definitions)
  + LangGraph (orchestration graph)
  + LiteLLM (provider-agnostic LLM calls)
  + FastAPI (agent microservices)
  + Spring Boot (public API gateway)
  + Kubernetes (swarm deployment + autoscaling)
```

## Differentiator on Kaggle
Most submissions = a CrewAI script.  
Yours = a LangGraph swarm on K8s with MCP tools and a Spring Boot gateway.  
That's a portfolio statement, not just a solution.

## Related notes
- [[Multi-Agent with CrewAI]]
- [[Orchestrator-Worker Pattern]]
- [[Tool Orchestration]]
- [[Hot Topics in Agentic AI]]
- [[Agent-to-Agent Handoff]]
- [[LangChain Basics]]
