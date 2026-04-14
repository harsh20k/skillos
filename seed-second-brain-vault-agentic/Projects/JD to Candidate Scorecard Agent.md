---
date: 2026-04-09
tags: [project-breakdown, agentic-ai, portfolio, hr-tech, rag, bedrock]
parent: "[[Project Ideas — AI Agent (Industry Grounded)]]"
score: 7/10
---

# Job Description → Candidate Scorecard Agent

> Good learning project. Saturated market — differentiate through evaluation rigor, not the core idea.

**Original rating:** 7/10 — high industry signal, but the idea is well-known. Build it to learn, not to stand alone in a portfolio.

---

## What It Does

Reads a job description, extracts structured evaluation criteria (skills, experience levels, must-haves vs nice-to-haves), then scores incoming resumes against those criteria. Produces a ranked shortlist with per-candidate reasoning — not just a score, but an explanation of why. Routes ambiguous or borderline candidates to a human recruiter for review.

**Real-world precedent:** LinkedIn's hiring team built agent-assisted screening internally. Workday, Greenhouse, and Lever all have AI resume screening. The market is real — but also crowded with products.

---

## Agentic AI Concepts You'll Learn

| Concept | How It Applies Here |
|---|---|
| **RAG** | Index the JD as a reference document; retrieve relevant criteria when scoring each resume |
| **Structured output** | Generate a consistent scorecard: skill match %, experience gap, recommended action, reasoning |
| **Tool use** | Parse PDF resumes (tool call), extract structured data, query a criteria store |
| **LLM-as-Judge** | Use a second LLM call to evaluate whether the scoring is consistent and unbiased |
| **Orchestrator-Worker pattern** | Orchestrator reads JD → defines rubric; worker agents score each resume independently |
| **Prompt engineering** | Critical here — inconsistent prompts produce inconsistent scoring; structured prompts matter |
| **Evals** | Bias testing (does the agent score equally across equivalent candidates?), consistency testing |
| **Human-in-the-loop** | Borderline candidates routed to recruiter with full reasoning for final decision |
| **Multi-step reasoning** | Agent doesn't just match keywords — it reasons about whether experience is transferable |

**Learning density: medium-high.** Strongest for RAG, structured output, evals, and prompt engineering. Less novel on orchestration.

---

## How to Build It (Your Stack)

```
Input: Job Description (text/PDF) + batch of resumes (PDFs)
  → Lambda: parse JD → extract structured criteria via Bedrock (Claude)
  → Store criteria in Bedrock KB or DynamoDB
  → For each resume:
      - Lambda: parse PDF → extract candidate profile
      - Bedrock Agent: retrieve JD criteria → score candidate → generate scorecard
      - LLM-as-Judge: validate scoring consistency
  → Aggregate: rank candidates → produce shortlist report
  → Human-in-the-loop: flag borderline candidates via SNS/email
```

Fully buildable with your existing stack. Straightforward Bedrock RAG pattern — probably a 1–2 week build.

---

## Job Market Demand — Canada / Nova Scotia

**Keywords employers use:** `AI recruiting`, `talent intelligence`, `resume parsing`, `HR automation`, `candidate screening AI`, `ATS integration`, `talent acquisition engineer`

| Market | Demand | Notes |
|---|---|---|
| Canada (national) | 🟠 High | AI in recruiting is one of the fastest-growing HR tech segments. 27% of real-world AI HR applications are in recruiting (SHRM 2026 report). |
| Toronto | 🟠 High | Fintech, SaaS, and consulting firms all building AI-assisted hiring pipelines. |
| Nova Scotia / Halifax | 🔴 Low-Medium | Very limited HR tech companies locally. This is primarily a remote-opportunity play. |

**Caution:** The space is saturated with *products* (Workday AI, Greenhouse, Lever, Phenom). Your project competes with these in perception. Frame it as "I built this to learn RAG + evals rigor" not as "I built a recruiting tool."

**Salary range (Canada):** $95,000–$140,000 CAD for AI/ML engineers in HR tech.

---

## Employability Score for Harsh

**Score: 5.5 / 10**

| Factor | Assessment |
|---|---|
| Stack alignment | ✅ Good — straightforward Bedrock RAG; fully within your current skills |
| Differentiation | 🔴 Low — many similar projects exist in GitHub portfolios; hiring managers have seen this before |
| Interview impact | 🟡 Medium — good for demonstrating RAG + evals, but won't generate "wow" reaction alone |
| Nova Scotia relevance | 🔴 Low — minimal HR tech employers locally; remote-only viable path |
| Learning ROI | 🟡 Medium — good for RAG, structured output, and evals practice |
| Build risk | ✅ Low — well-understood pattern, achievable quickly |

**When to build this:** Use it as a *learning exercise* before tackling a harder project, or pair it with a genuinely novel angle (e.g., bias detection and explanation as a core feature, not an afterthought). Don't lead your portfolio with this.

**The honest framing in interviews:** "I built a resume scoring agent to practice structured RAG and LLM-as-judge evaluation patterns — then applied those same patterns to [harder project]."

---

## Related Notes
- [[Project Ideas — AI Agent (Industry Grounded)]]
- [[LLM-as-Judge Evaluation]]
- [[Document Parsing (PDF to JSON)]]
- [[Cross-Encoder Reranking]]
- [[Precision@K & Retrieval Eval]]
