# Hot Topics in Agentic AI

**Tags:** #agentic-ai #moc

> Map of Content — links to all core agentic AI concepts worth knowing for interviews and system design.

---

## 🔁 Agent Loops
How agents think and act in cycles.

- [[ReAct]] — Reasoning + Acting interleaved; the core loop pattern
- [[Plan-and-Execute]] — Generate a full plan upfront, then execute step by step
- [[Reflection Loops]] — Agent critiques its own output and revises
- [[When to Stop (Agent Loops)]] — Stopping conditions: max iterations, finish signals, confidence thresholds

---

## 🛠 Agent Design
Internal mechanics of a well-built agent.

- [[Tool Orchestration]] — How agents select, sequence, and call tools
- [[State Design (Scratchpad)]] — Where agents store intermediate working memory
- [[Output Parsing (Agents)]] — Extracting structured data from raw LLM text
- [[Error Handling (Agents)]] — Recovering from tool failures, hallucinations, and timeouts
- [[Feedback Loops (Agent Design)]] — Routing quality signals back to improve the agent

---

## 🤝 Multi-Agent
Patterns for coordinating multiple agents.

- [[Orchestrator-Worker Pattern]] — One coordinator + many specialist workers
- [[Agent-to-Agent Handoff]] — Transferring control and context between agents
- [[Shared State Management]] — Avoiding race conditions across concurrent agents

---

## 🚀 Prod vs Local
What breaks when you go to production.

- [[Cold Starts (Agentic AI)]] — Latency spikes from idle Lambda/container/model warmup
- [[Concurrency Issues (Agents)]] — Race conditions, duplicate actions, rate limit collisions
- [[Context Window Bloat]] — Context filling up with history, tool outputs, and retrieved docs
- [[Semantic Caching]] — Cache LLM responses by similarity, not exact match
- [[Token Budgeting]] — Allocating token limits across prompt components intentionally

---

## See also
- [[Multi-Agent with CrewAI]]
- [[LangChain Basics]]
- [[LLM-as-Judge Evaluation]]
- [[Chunking Strategies]]
- [[Latency & Observability]]
