---
date: 2026-04-09
tags: [project-breakdown, agentic-ai, portfolio, knowledge-management, rag]
parent: "[[Project Ideas — AI Agent (Industry Grounded)]]"
score: 8.5/10
---

# Knowledge Base Decay Agent

> Universal problem. No good automated solution exists yet — that's the opportunity.

**Original rating:** 8.5/10 — very high differentiation, novel idea, strong interview impact.

---

## What It Does

Monitors a company's internal knowledge base (Confluence, Notion, internal wikis) and continuously identifies pages that have gone stale — because the underlying code changed, the team reorganized, or the information is simply months out of date. The agent flags owners, drafts updated versions, and routes them for human review. It doesn't delete or overwrite; it acts as a first-pass editor.

**Real-world precedent:** Atlassian is actively building AI agents on top of Confluence (announced April 2026 — Lovable, Replit, and Gamma agents launching). This validates the market. No off-the-shelf "decay detection" agent exists yet — that's the gap you'd fill.

---

## Agentic AI Concepts You'll Learn

| Concept                         | How It Applies Here                                                                                                                  |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Tool use**                    | Agent reads Confluence pages via API, checks GitHub commit history, compares doc dates vs code change dates                          |
| **RAG**                         | Index the entire knowledge base into a vector store; retrieve relevant docs to compare against current source-of-truth code/policies |
| **LLM-as-Judge**                | Evaluate whether a page's content is still accurate relative to current code or org structure                                        |
| **Multi-agent**                 | Staleness detector agent + Draft writer agent (one identifies decay, other rewrites)                                                 |
| **Orchestrator-Worker pattern** | Orchestrator schedules scans; workers process individual pages in parallel                                                           |
| **Memory (persistent)**         | Track each page's "last verified" timestamp, decay score history, owner assignments                                                  |
| **Human-in-the-loop**           | Draft updated content → route to page owner for approval before publishing                                                           |
| **Scheduled agents**            | Nightly or weekly cron-style runs across entire wiki                                                                                 |
| **Structured output**           | Generate decay report with page URL, reason for staleness, suggested update, confidence score                                        |
| **Evals**                       | Measure: did the agent correctly identify stale content? Did drafts get accepted by humans?                                          |

**Learning density: very high.** Strong on RAG, LLM-as-judge, and multi-agent orchestration.

---

## How to Build It (Your Stack)

```
Scheduled trigger (EventBridge cron)
  → Lambda invokes Bedrock Agent (orchestrator)
  → Agent calls tools:
      - list_pages() → Confluence API, return all pages with last-modified date
      - get_page_content() → fetch full markdown of each page
      - get_related_commits() → GitHub API, find commits touching related code files
      - query_kb() → Bedrock Knowledge Base (RAG), retrieve current reference docs
  → LLM compares page content vs current state → generates decay score + draft update
  → LLM-as-Judge validates draft quality
  → Human-in-the-loop: SNS notification to page owner with draft for review
```

**Stack note:** You'd be adding Confluence API and GitHub API as new tool integrations — moderate learning lift, but well-documented APIs.

---

## Job Market Demand — Canada / Nova Scotia

**Keywords employers use:** `knowledge management`, `documentation automation`, `AI content management`, `internal tools engineer`, `developer experience`, `Confluence`, `wiki automation`, `AI-powered search`

| Market | Demand | Notes |
|---|---|---|
| Canada (national) | 🟠 High | Every tech company has the problem. Atlassian's April 2026 agent launch validates enterprise demand. "Internal tools" and "developer experience" roles are growing. |
| Toronto / Vancouver | 🟠 High | Large SaaS companies (Shopify, Hootsuite, Wealthsimple) all run Confluence-heavy knowledge systems. |
| Nova Scotia / Halifax | 🟡 Medium-Low | Smaller tech ecosystem, but Dalhousie, government departments, and financial service branches have this problem. Remote roles accessible. |

**Salary range (Canada):** $100,000–$145,000 CAD for AI/internal tools engineers in this space.

---

## Employability Score for Harsh

**Score: 7.5 / 10**

| Factor | Assessment |
|---|---|
| Stack alignment | 🟡 Partial — AWS/Bedrock for orchestration, but needs Confluence + GitHub API integration (new) |
| Differentiation | ✅ Very high — this is a genuinely novel project; no obvious competitor portfolio piece |
| Interview impact | ✅ Very high — "I built an agent that reads your wiki, finds stale content, and drafts fixes" is immediately relatable to every engineering manager |
| Nova Scotia relevance | 🟡 Moderate — problem is universal but local companies are smaller |
| Learning ROI | ✅ High on RAG, LLM-as-judge, multi-agent, and eval patterns |
| Build complexity | 🟡 Medium-high — requires API integrations you haven't built yet, but docs are excellent |

**The pitch:** "I built an agent that monitors a company's internal knowledge base, identifies pages that are out of sync with current code and org structure, drafts updated versions, and routes them to owners for review — reducing documentation rot without requiring humans to babysit the process." Every eng manager has experienced this pain firsthand.

---

## Related Notes
- [[Project Ideas — AI Agent (Industry Grounded)]]
- [[LLM-as-Judge Evaluation]]
- [[Chunking Strategies]]
- [[FAISS]]
- [[Orchestrator-Worker Pattern]]
- [[Multi-Agent with CrewAI]]
