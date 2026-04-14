# AI Invoice Intake, Approval & Reminder Workflow

From Pavan's lecture — Project 2 example. A practical finance-ops agentic workflow.

## What it is

An end-to-end agentic pipeline that takes a messy real-world input (invoice PDF via email) and ends with real operational actions — not just a summary.

**Correct framing:** "Agentic invoice operations workflow" or "AI-powered invoice intake and approval system" — stronger than "fully autonomous finance agent" because it explicitly includes parallel verification, policy checks, and human-in-the-loop approvals.

## End-to-end flow

```
Invoice PDF email arrives
  → AWS email receiving (intake)
  ↓
Textract extracts structured fields
  (Invoice No, Date, Vendor, Amount, Tax, Terms, Conditions)
  ↓
Parallel sub-agents run simultaneously:
  ├── Duplicate / prior invoice check
  ├── Vendor / party verification
  ├── Amount / date / terms validation
  └── Policy / approval routing (HITL decision)
  ↓
Conditional Slack approval (only if low confidence or policy threshold hit)
  ↓
Commit to downstream systems:
  ├── Enter into database (accounting record)
  ├── Notify accounts head
  ├── Confirm receipt to sender
  ├── Update payables / receivables
  └── Create Outlook reminders (due-date follow-ups)
```

## Why each design decision matters

| Decision | Why |
|---|---|
| Parallel sub-agents | Reduces latency — checks run simultaneously, not sequentially |
| HITL only when needed | Keeps automation high, human effort low — approval only on exceptions |
| Starts from messy input (PDF email) | Real-world grounding — not a clean API call |
| Ends with operational actions | Not just extraction — actual DB writes, Slack messages, calendar reminders |
| Policy-based routing | Deterministic rules decide when to escalate — reduces hallucination risk |

## Agentic AI concepts demonstrated

- **Orchestrator-worker pattern** — main agent routes to parallel sub-agents
- **Parallel execution** — sub-agents run simultaneously (latency reduction)
- **Human-in-the-loop (HITL)** — conditional Slack approval gate
- **Tool use** — Textract (document AI), Slack API, DB write, Outlook API
- **Structured extraction** — PDF → JSON fields via document AI
- **Conditional branching** — policy rules determine flow path

## How you could build this (your stack)

```
Email intake        → AWS SES
PDF extraction      → AWS Textract
Orchestrator        → LangGraph (manages parallel sub-agent dispatch)
Sub-agents          → FastAPI pods (each check = one agent)
HITL approval       → Slack API (send message + wait for response)
DB commit           → RDS / DynamoDB
Reminders           → Outlook / Google Calendar API
Gateway             → Spring Boot (auth + routing)
Deployment          → K8s (each sub-agent = scalable pod)
```

This is essentially the same architecture as Project 3 (swarm on K8s) applied to a concrete finance domain.

## Why this is a strong portfolio project

- Touches document AI, parallel agents, HITL, multi-system integration
- Finance ops is a high-value enterprise domain
- Clear before/after: manual invoice processing → automated pipeline
- Demonstrable ROI: time saved per invoice × volume

## Related notes
- [[Orchestrator-Worker Pattern]]
- [[Agent-to-Agent Handoff]]
- [[Tool Orchestration]]
- [[Memory Retrieval — BM25 vs Vector vs Hybrid]]
- [[Agent Framework Landscape 2026]]
- [[Hot Topics in Agentic AI]]
- [[Error Handling (Agents)]]
- [[Shared State Management]]
