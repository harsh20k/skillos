---
date: 2026-04-09
tags: [project-ideas, agentic-ai, portfolio, career]
source: Research from real enterprise deployments — Uber, LinkedIn, Shopify, Elastic, Klarna, BlackRock, Genentech, Amazon
---
# Project Ideas — AI Agent (Industry Grounded)

Generated from research into what real companies are actually deploying in production (April 2026). Not theoretical — each idea maps to a known enterprise deployment or validated market need.

---

## Developer Tooling

1. **PR Review Agent** — reads a pull request, checks for bugs, security issues, and style violations, writes review comments, flags risky changes before humans look at it. GitHub and GitLab building this internally.

2. **Incident Response Agent** — when a production alert fires (PagerDuty/CloudWatch), agent queries logs, traces root cause, suggests a fix, drafts incident report. Elastic does this for SecOps. Uber uses similar for on-call.

3. **API Documentation Agent** — reads a codebase, generates OpenAPI specs, keeps docs in sync with code changes. Universal pain point with clear ROI.

4. **Database Query Optimizer Agent** — natural language → SQL → execute → explain the query plan → suggest indexes. LinkedIn's SQL Bot is exactly this pattern.

---

## Content & Media

5. **Storyboard-to-Production Pipeline Agent** (*really interesting*) — takes a script or brief, generates storyboard outline, assigns shots, creates production schedule, drafts briefs for each asset. Disney Parks (Mitul's account at Avanade) operates this kind of pipeline.

6. **Multilingual Content Localization Agent** (*really interesting*) — takes content, translates, adapts cultural references, flags legal risks per region, routes for human review. Global media companies spend millions on this manually.

---

## Data & Analytics

7. **Natural Language BI Agent** — connects to a data warehouse, lets non-technical users ask business questions in plain English, returns charts and summaries with source citations. Morningstar built "Mo" exactly like this with LangChain.

8. **Competitive Intelligence Agent** — monitors competitors' websites, job postings, press releases, patent filings continuously. Surfaces weekly summaries and flags strategic signals. BlackRock-style research automation for any business.

9. **Data Quality Monitoring Agent** (*interesting*) — watches incoming data pipelines, flags anomalies, traces where bad data originated, alerts the right team with a diagnosis. Every company with a data warehouse needs this.

---

## Operations

10. **Meeting-to-Action Agent** — records a meeting, extracts decisions and action items, assigns owners, creates tasks in Jira/Linear/Asana, follows up if items go stale. One of the first enterprise agentic deployments per Deloitte 2026 report.

11. **Supply Chain Disruption Agent** (*mildly interesting*) — monitors supplier news, port delays, weather events, cross-references with inventory and order pipeline, proactively flags risks before they become stockouts. PepsiCo and manufacturers building this now.

12. **Employee Onboarding Agent** (*mildly interesting*)— answers HR policy questions, walks new hires through setup checklists, routes paperwork to the right people, flags when steps are blocked. Shopify and Uber built internal versions.

---

## Security & Compliance

13. **Threat Intelligence Agent** — ingests CVE feeds, internal vulnerability scans, dark web signals, correlates against your specific stack, prioritizes what to patch first. Elastic's production SecOps agent is this pattern.

14. **Compliance Audit Agent** — reads contracts, policies, regulatory filings, flags clauses that conflict with new regulations, generates remediation reports. Finance and insurance companies deploying this heavily.

---

## E-commerce & Retail

15. **Product Catalogue Agent** (*mildly interesting*)— takes raw supplier data (spreadsheets, PDFs, images), extracts structured attributes, enriches with SEO metadata, flags incomplete listings. Shopify built this with two specialized agents handling billions of products.

16. **Returns & Refunds Agent** (*mildly interesting*)— handles the full return workflow autonomously: validates eligibility, initiates refund, updates inventory, escalates only genuine edge cases. Klarna's support agent handles this at scale.

---

## Research & Knowledge

17. **Literature Review Agent** — given a research topic, searches academic databases, summarizes papers, identifies contradictions across studies, generates a structured review. Genentech built this for pharmaceutical R&D on AWS.

18. **Patent Landscape Agent** — scans patent filings in a technology domain, identifies whitespace, flags potential infringement risks, generates competitive landscape map. IP-heavy industries (pharma, semiconductors, defence) pay heavily for this.

---

## Personal Productivity at Enterprise Scale

19. **Job Description → Candidate Scorecard Agent** (*interesting*)— reads a JD, defines evaluation criteria, scores incoming resumes against them, produces ranked shortlists with reasoning. LinkedIn's hiring team built agent-assisted screening internally.

20. **Knowledge Base Decay Agent** (*interesting*)— monitors a company's internal wiki or Confluence, identifies outdated pages (based on code changes, org changes, date), flags owners, drafts updated versions for human review. Universal problem, no good solution exists yet.

---

## Related notes
- [[Agent Framework Landscape 2026]]
- [[AI Invoice Intake Approval and Reminder Workflow]]
- [[AI Meeting Intelligence — Multi-Agent n8n Workflow]]
- [[OWASP Top 10 for Agentic AI]]
- [[Orchestrator-Worker Pattern]]
- [[Hot Topics in Agentic AI]]

---

## Signal Rating — Agentic AI / AI Engineer Roles

*Rated only for projects marked interesting/mildly interesting/really interesting. Shortlisted projects link to individual breakdown notes.*

| #   | **Score /10** | Project                                                                          | Your Interest      | Agentic Complexity | Industry Signal                 | Buildability (your stack)             | Interview Impact             | 🇨🇦 NS Demand | Employability (Harsh) |
| --- | ------------- | -------------------------------------------------------------------------------- | ------------------ | ------------------ | ------------------------------- | ------------------------------------- | ---------------------------- | -------------- | --------------------- |
| 9   | **9**         | [[Data Quality Monitoring Agent]]                                                | interesting        | High               | Very High                       | High — AWS + Bedrock + Kinesis        | High                         | 🟡 Medium      | **9 / 10**            |
| 20  | **8.5**       | [[Knowledge Base Decay Agent]]                                                   | interesting        | High               | High                            | Medium — needs Confluence/GitHub APIs | Very High (differentiated)   | 🟡 Medium      | **7.5 / 10**          |
| 19  | **7**         | [[JD to Candidate Scorecard Agent\|Job Description → Candidate Scorecard Agent]] | interesting        | Medium             | High                            | High — straightforward Bedrock RAG    | Medium (saturated)           | 🔴 Low         | **5.5 / 10**          |
| 5   | **7**         | [[Storyboard-to-Production Pipeline Agent]]                                      | really interesting | Medium             | High — Disney/Avanade reference | Medium                                | High (Avanade talking point) | 🔴 Low         | **6 / 10**            |
| 6   | **6.5**       | Multilingual Content Localization Agent                                          | really interesting | Medium             | High                            | Medium                                | Medium                       | —              | —                     |
| 11  | **6.5**       | Supply Chain Disruption Agent                                                    | mildly interesting | High               | High                            | Medium — real data hard to mock       | Medium                       | —              | —                     |
| 12  | **5**         | Employee Onboarding Agent                                                        | mildly interesting | Low-Medium         | Medium                          | High                                  | Low (too common)             | —              | —                     |
| 15  | **5**         | Product Catalogue Agent                                                          | mildly interesting | Low                | High                            | High                                  | Low (not agent-forward)      | —              | —                     |
| 16  | **4.5**       | Returns & Refunds Agent                                                          | mildly interesting | Low-Medium         | High                            | High                                  | Low (too common)             | —              | —                     |

**Top pick: #9 (Data Quality Monitoring Agent)** — strongest fit with AWS/Bedrock stack, most differentiated for Agentic AI roles, directly extensible from GroundSense architecture.

> *Employability scores account for Harsh's stack (AWS/Bedrock/Lambda), Nova Scotia/Canada market demand, and portfolio differentiation. Detailed breakdowns with agentic AI concepts + job search data in linked notes.*
