# Token Budgeting

**Tags:** #agentic-ai #prod-vs-local

**Related:** [[Hot Topics List in Agentic AI]] | [[Context Window Bloat]] | [[Semantic Caching]]

---

## What is it?
Deliberately allocating and managing token usage across the different components of an agent's context — system prompt, history, retrieved docs, tool outputs, and response — to stay within limits and control cost.

## Why it matters in prod
- Token cost scales linearly with usage — agentic loops can easily use 10x tokens of a single call
- Exceeding context limits causes hard failures
- Inefficient token use = bloated latency and wasted spend

## Budget breakdown (example for 32K context)

| Component | Allocation |
|---|---|
| System prompt | ~1,000 tokens (fixed) |
| Conversation history | ~4,000 tokens (windowed) |
| Retrieved RAG chunks | ~8,000 tokens (top-K controlled) |
| Tool outputs | ~4,000 tokens (pruned) |
| Scratchpad / reasoning | ~3,000 tokens |
| Response headroom | ~4,000 tokens |
| Safety buffer | ~8,000 tokens |

## Strategies

### Hard caps per component
Enforce max token counts per section. Truncate or summarize when exceeded.

### Dynamic allocation
Adjust component budgets based on task type — a research task gets more retrieval budget; a simple Q&A gets less.

### Token-aware chunking
When retrieving RAG docs, pick chunks whose combined token count stays within budget.

### Monitor and alert
Track tokens per request in prod. Alert when average approaches 80% of limit.

## GroundSense analogy
GroundSense's system prompt + sensor data + retrieved knowledge base chunks all share the same context window. Without budgeting, a verbose sensor log could crowd out the instructions.

## Key insight
Token budgeting is an engineering constraint, not a nice-to-have. Treat it like memory management.
