# Advanced AI Topics — Next 10

Continuation of the [[ML & RAG Learning Roadmap]] — topics 13–22 in incremental order.

| #   | Topic                                                              | Why next                                                          | What it unlocks                                                |
| --- | ------------------------------------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------- |
| 13  | **Prompt Engineering Patterns** (CoT, ReAct, few-shot)             | Directly applies to GroundSense agent prompts today               | Systematic way to improve agent reasoning                      |
| 14  | **Structured Outputs & Function Calling**                          | Builds on tool use already known                                  | Reliably get JSON out of LLMs, type-safe pipelines             |
| 15  | **Agentic Reasoning Patterns** (ReAct, Reflexion, self-correction) | Extends #13 — how agents think and recover from errors            | Agents that fix their own mistakes                             |
| 16  | **Memory Systems for Agents** (short-term, long-term, episodic)    | Extends CrewAI — agents that remember across turns                | Stateful agents, personalisation                               |
| 17  | **GraphRAG**                                                       | Extends FAISS — relationships between chunks, not just similarity | Better retrieval when answers span multiple documents          |
| 18  | **Vector DB Deep Dive** (Pinecone, Weaviate, pgvector)             | Production-grade FAISS alternatives                               | Metadata filtering, hybrid search, managed infra               |
| 19  | **Fine-tuning LLMs** (LoRA / QLoRA)                                | Builds on HuggingFace — adapting models to your domain            | Domain-specific models, smaller + cheaper                      |
| 20  | **Guardrails & Safety** (input/output validation)                  | Production necessity — applies to everything above                | Prevent prompt injection, toxic outputs, hallucination leakage |
| 21  | **Cost Optimisation** (token counting, caching, model routing)     | Production economics — applies to GroundSense directly            | Cut Bedrock costs, route cheap queries to smaller models       |
| 22  | **MLOps for LLMs** (versioning, deployment, rollback)              | Closes the loop — shipping and maintaining models                 | Production ML lifecycle end to end                             |

## Where to Start
Topics **#13 and #14** give the most immediate value for GroundSense and are the most common interview topics for AI engineering roles.

## Related
- [[ML & RAG Learning Roadmap]] — the first 12 topics
