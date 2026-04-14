---
title: "Agentic AI — Pavankumar Sakare (DeepSense)"
speaker: "Pavankumar Sakare"
company: "DeepSense"
date: 2026-04-06
tags:
  - agentic-ai
  - guest-talk
  - n8n
  - automation
  - deepsense
---

## Speaker

**Pavankumar Sakare** — AI Engineer at **DeepSense**, Halifax. Covered agentic AI concepts and shared two production AI agent systems built using **n8n**.

My Professor Lu Yang invited him today in the class today for sharing his insights and Agentic AI project experience.

---

## Topics Covered

### Agent vs Workflow vs Pipeline
- **Pipeline**: linear, fixed sequence of steps, no decision-making
- **Workflow**: branching logic, conditionals, but still pre-defined
- **Agent**: dynamic — observes, reasons, decides what to do next at runtime

---

### Model → Assistant → Agent
- **Model**: raw LLM, just generates text
- **Assistant**: model + memory + system prompt (e.g. ChatGPT)
- **Agent**: assistant + tools + loop + ability to act in the world

---

### Anthropic's 5+1 Agentic Patterns
1. **Prompt Chaining** — output of one LLM call feeds into the next
2. **Routing** — classify the input first, then send to the right specialist prompt/agent
3. **Parallelisation** — run multiple LLM calls simultaneously, merge results
4. **Orchestrator → Workers** — one agent plans, delegates to specialised sub-agents
5. **Evaluator → Optimiser** — one agent generates, another critiques and improves
6. **+1 Autonomous Agent** — fully self-directed, decides its own next steps in a loop

---

### Multi-Agent Architecture Patterns
1. **Orchestrator-Worker** — central coordinator + specialist workers
2. **Peer-to-Peer (Swarm)** — agents communicate directly with each other, no central authority
3. **Hierarchical** — nested layers of orchestrators and workers
4. **Human-in-the-Loop** — agent pauses at key decision points for human approval

---

### How Multi-Agent is Deployed on AWS
- Bedrock Agents as the reasoning layer
- Lambda as tool/action executors
- EventBridge for event-driven triggers
- Step Functions for orchestrating multi-step workflows
- DynamoDB / S3 for shared state and memory

---

### Context Window of an LLM
- The total token space the model can "see" at once
- Everything competes for this space: system prompt, history, tools, retrieved docs
- Bigger isn't always better — context rot degrades performance past a threshold
- See also: [[Context Window Bloat]], [[Token Budgeting]]

---

### Memory Architecture in AI Agents — 5 Layers

#### Layer 1: Core Memory Foundation
- **Short-term memory** — in-context, current conversation/session only
- **Long-term memory** — persisted across sessions (files, DB, vector store)

#### Layer 2: Knowledge + Context Assembly
- **Entity memory** — tracks specific entities (people, places, objects) mentioned
- **Contextual memory** — assembles relevant background for the current query

#### Layer 3: Personalisation Layer
- **User memory** — stores user preferences, history, behaviour patterns over time

---

### Key Technical Concepts
1. **Function Calling** — structured way for LLMs to invoke tools with typed arguments
2. **Context Window Budget** — intentionally allocating token limits across prompt components
3. **Structured Output** — forcing LLM responses into JSON/typed schemas for downstream use
4. **Caching** — KV cache reuse to reduce latency and cost on repeated/similar inputs

---

### Frameworks Overview

| Framework | Notes |
|---|---|
| **DIY** | Build your own agent loop in Python — full control, most work |
| **MCP** | Solves the N×M integration problem — one protocol for all tool connections |
| **LangGraph** | Graph-based agent orchestration, good for complex branching flows |
| **CrewAI / n8n** | Role-based multi-agent (CrewAI) or visual workflow automation (n8n) |
| **OpenAI Agents SDK** | OpenAI's official agent framework |
| **MS Agent Framework** | Microsoft's offering, integrates with Azure ecosystem |

---

### Google Gemini Embeddings — From Tokens to Vector Space
- Text → tokenised → passed through model → embedding vector produced
- Each token/sentence maps to a point in high-dimensional vector space
- Similar meanings → nearby vectors (cosine similarity)
- Foundation of semantic search and RAG retrieval

---

### Memory Retrieval: BM25 vs Vector vs Hybrid
- **BM25** — keyword-based, fast, exact match, no semantic understanding
- **Vector** — semantic similarity via embeddings, handles paraphrasing well
- **Hybrid** — combines both: BM25 for precision, vector for recall
- See also: [[Semantic search]], [[BM25]]

---

### Safety: OWASP Top 10 for Agentic AI
Key risks specific to AI agents (beyond standard LLM risks):
- Prompt injection via tool outputs or external content
- Excessive agency — agent taking unintended high-impact actions
- Insecure tool use — tools with overly broad permissions
- Sensitive data exposure through retrieval or memory
- Lack of human oversight on autonomous decisions

---

### Context Engineering > Prompt Engineering
- Prompt engineering = how you phrase the instruction
- Context engineering = what you put in the window, how you structure it, what you leave out
- As models get more capable, most failures become **context failures**, not intelligence failures
- See also: [[A Guide to Context Engineering for LLMs]]

---

## Projects

### Project 1: AI Meeting Assistant
- Auto-extracts action items, owners, deadlines from meeting transcripts
- Sends summary emails to participants
- Creates Outlook calendar events automatically
- Built with n8n + LLM nodes, in production at DeepSense

### Project 2: Invoice Processing Agent
- Picks up invoice attachments from incoming emails
- Parses vendor, amount, date, line items using LLM
- Writes structured data to a database
- Generates spend summaries
- Built with n8n + LLM nodes, in production at DeepSense

---

## Connections to My Work

| Session Topic | My Notes |
|---|---|
| Anthropic 5+1 patterns | [[Hot Topics in Agentic AI]] |
| Orchestrator-Worker | [[Orchestrator-Worker Pattern]] |
| Memory architecture | [[State Design (Scratchpad)]] |
| Context window | [[Context Window Bloat]], [[Token Budgeting]] |
| Function calling / structured output | [[Output Parsing (Agents)]], [[Tool Orchestration]] |
| BM25 vs Vector vs Hybrid | [[Semantic search]] |
| Context engineering | [[A Guide to Context Engineering for LLMs]] |
| AWS multi-agent deployment | [[GroundSense Project Description]] |
| MCP | [[Hot Topics in Agentic AI]] |

---

## Related Notes
- [[Hot Topics in Agentic AI]]
- [[A Guide to Context Engineering for LLMs]]
- [[Multi-Agent with CrewAI]]
- [[LangChain Basics]]
- [[Semantic search]]
- [[Token Budgeting]]
- [[Context Window Bloat]]
- [[GroundSense Project Description]]
- [[Deepsense projects]]

---

## Claude Conversation — Topics Covered (2026-04-09)

Notes created from this conversation are all saved in Slipbox. Topics discussed:

1. Platform-agnostic multi-agent system design
2. Connecting multi-agent systems to a Spring Boot backend
3. Project 3 — Multi-Agent Swarm on Kubernetes
4. Agent Framework Landscape 2026 (DIY / MCP / LangGraph / CrewAI / OpenAI Agents SDK / MS Agent Framework)
5. Embeddings — Tokens to Vector Space (Gemini multimodal embeddings)
6. Memory Retrieval — BM25 vs Vector vs Hybrid
7. Project 2 — AI Invoice Intake, Approval & Reminder Workflow
8. Invoice project tech stack
9. LangGraph maturity vs other frameworks
10. Project — AI Meeting Intelligence (n8n multi-agent workflow)
11. S3 directory structure for meeting intelligence system
12. Trustworthy Agents in Practice — Anthropic article

### Slipbox notes created
- [[Agent Framework Landscape 2026]]
- [[Embeddings — Tokens to Vector Space]]
- [[Memory Retrieval — BM25 vs Vector vs Hybrid]]
- [[AI Invoice Intake Approval and Reminder Workflow]]
- [[AI Meeting Intelligence — Multi-Agent n8n Workflow]]
- [[Trustworthy Agents in Practice — Anthropic]]
