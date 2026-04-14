# AI Meeting Intelligence — Multi-Agent n8n Workflow

From Pavan's lecture — Project shown as two n8n screenshots. A meeting transcript enters and multiple structured outputs (summary, action items, quality report, versioned documents) come out automatically.

## What it is

An AI-powered meeting intelligence pipeline that normalizes transcript input, runs parallel specialized agents, verifies quality, and commits structured outputs to DynamoDB and Notion.

**Orchestration tool:** n8n (visual workflow, not LangGraph)
**LLM:** AWS Bedrock Claude (multiple model instances)

## Two workflows shown

### Image 1 — Simple pipeline (starter version)
```
Webhook → Parse VTT → LLM Call (Bedrock Claude) → Extract Summary → Create Notion Page → Respond to Webhook
```
Single LLM call. No agents. A meeting transcript (VTT format) comes in, Claude summarizes it, summary saved to Notion. Good starting point before adding agents.

![[image-194.png]]

### Image 2 — Full multi-agent system (main project)

![[image-195.png]]

```
Webhook
  → Agent 1: Normalizer
  → Check Context Pack
  → IF: Needs Rebuild?
      TRUE  → Build Context Pack
                ├── Agent 2: Summarizer (Bedrock Model 1) → Parse Response
                └── Agent 3: Action Items + Risks (Bedrock Model 2) → Parse Response → Agent 4: Composer
      FALSE → Use Cached Pack  ← (KV cache reuse — skips redundant LLM calls)
  → Agent 5: Verifier → Parse Response
  → IF: Quality Check
      PASS → Prepare Final Output
               ├── Prep + Upload Summary MD
               ├── Prep + Upload Extraction JSON
               ├── Prep + Upload Evidence Map
               ├── Prep + Upload Quality Report
               ├── Prep + Upload CP Latest
               └── Prep + Upload CP Versioned
           → Restore All Fields
           → Update DynamoDB ProjectMapping
           → Build Notion Body
           → Create Notion Page
           → Respond to Webhook
```

## Agentic AI concepts demonstrated

| Concept | Where it appears |
|---|---|
| Conditional branching | IF: Needs Rebuild, IF: Quality Check |
| Parallel agents | Agent 2 (summarizer) + Agent 3 (action items) run in parallel |
| Role-based agents | Each agent has a distinct job — normalizer, summarizer, extractor, composer, verifier |
| KV cache reuse | "Use Cached Pack" branch skips rebuild if context unchanged — cost + latency saving |
| Quality gate (HITL-lite) | Verifier agent + IF quality check before committing outputs |
| Multiple output formats | MD, JSON, versioned docs all produced from one pipeline |
| Stateful storage | DynamoDB for project mapping, Notion for human-readable output |

## Why n8n instead of LangGraph here

- n8n's visual graph maps directly to the agent flow — no code needed for Notion, DynamoDB, webhook nodes
- Built-in connectors eliminate custom integration work
- Good fit when the workflow is mostly deterministic with LLM steps inserted
- Trade-off: less fine-grained control over state and branching vs LangGraph
- This pattern (n8n orchestration + Bedrock LLM) is a strong alternative to LangGraph for ops-heavy pipelines

## How you could build this (your stack)

```
Webhook trigger         → n8n webhook node (or FastAPI)
Transcript parsing      → custom n8n function node (VTT parser)
Context cache check     → DynamoDB lookup
Parallel agents         → n8n parallel branches OR LangGraph parallel nodes
LLM calls               → AWS Bedrock Claude (already in GroundSense)
Quality verification    → LLM-as-judge agent
File outputs            → S3 + n8n binary upload nodes
Database               → DynamoDB (already in GroundSense)
Notion integration      → Notion API node (built into n8n)
```

## Relation to your projects

- **GroundSense** already uses Bedrock Claude + DynamoDB — same infra, different workflow shape
- The "Check Context Pack → Use Cached Pack" pattern is exactly the KV cache reuse optimization you analyzed for GroundSense latency
- **Project 3 (K8s swarm):** same multi-agent pattern, but LangGraph + FastAPI pods instead of n8n nodes
- This project shows that n8n is a valid orchestrator for production agentic workflows — not just prototyping

## Key takeaway

Two versions of the same idea: Image 1 is a single-agent pipeline, Image 2 is the production multi-agent evolution. The jump between them illustrates how agentic complexity grows — parallel roles, caching, quality gates, versioned outputs. The n8n visual graph makes the agent topology immediately readable, which is a portfolio presentation advantage.

## Related notes
- [[AI Invoice Intake Approval and Reminder Workflow]]
- [[Agent Framework Landscape 2026]]
- [[Orchestrator-Worker Pattern]]
- [[KV Cache Reuse]]
- [[LLM-as-Judge Evaluation]]
- [[Shared State Management]]
- [[Tool Orchestration]]
- [[Hot Topics in Agentic AI]]

## S3 Directory Structure

The recommended S3 bucket layout for this system (`s3://agai-meeting-processing/`):

```
s3://agai-meeting-processing/
|-- index.md                          # Org overview, project list, links
|-- tools.md                          # MCP tool registry / API reference
|-- company/
|   |-- index.md                      # Company details and guidelines
|   |-- guidelines/
|   |   |-- company_policies.pdf
|   |   |-- company_procedures.pdf
|   |   `-- company_handbook.pdf
|   |-- assets/
|   |   `-- logo.png
|   `-- services/
|       |-- service1.pdf
|       `-- service2.pdf
|-- projects/
|   |-- index.md
|   `-- {project_id}/
|       |-- metadata.json
|       |-- meetings_vtt/
|       |-- meeting_summary/
|       |-- context_pack/
|       |-- evidence_bundles/
|       `-- logs/
```

### Why this structure matters

- **`index.md` at root** — gives the agent a single entry point to understand the org and navigate to projects. Acts like a sitemap for the LLM.
- **`tools.md`** — MCP tool registry. Agents read this to know what tools are available, matching the MCP "USB-C" pattern.
- **`company/`** — static context (policies, handbook, services) that agents load into the context pack. Changes infrequently — good candidate for caching.
- **`projects/{project_id}/`** — per-project isolation. Each folder contains:
  - `meetings_vtt/` — raw transcript input
  - `meeting_summary/` — Agent 2 output
  - `context_pack/` — built or cached context (the "Check Context Pack" step)
  - `evidence_bundles/` — structured extraction output (Agent 3 output)
  - `logs/` — audit trail per run
- **`metadata.json`** — project-level config the agents read before processing (project name, participants, date range, etc.)

### Connection to the workflow

The "Check Context Pack → IF: Needs Rebuild" decision in the n8n workflow maps directly to:
```
S3: projects/{project_id}/context_pack/ → exists + fresh? → Use Cached Pack
                                         → stale or missing? → Build Context Pack from company/ + meetings_vtt/
```

This is KV cache reuse at the file system level — same concept, different layer.

## S3 Directory Structure

Recommended S3 bucket layout for this system (`s3://agai-meeting-processing/`):

```
s3://agai-meeting-processing/
|-- index.md                          # Org overview, project list, links
|-- tools.md                          # MCP tool registry / API reference
|-- company/
|   |-- index.md                      # Company details and guidelines
|   |-- guidelines/
|   |   |-- company_policies.pdf
|   |   |-- company_procedures.pdf
|   |   `-- company_handbook.pdf
|   |-- assets/
|   |   `-- logo.png
|   `-- services/
|       |-- service1.pdf
|       `-- service2.pdf
|-- projects/
|   |-- index.md
|   `-- {project_id}/
|       |-- metadata.json
|       |-- meetings_vtt/
|       |-- meeting_summary/
|       |-- context_pack/
|       |-- evidence_bundles/
|       `-- logs/
```

### Why this structure matters

- **`index.md` at root** — gives the agent a single entry point to understand the org and navigate to projects. Acts like a sitemap for the LLM.
- **`tools.md`** — MCP tool registry. Agents read this to know what tools are available — matches the MCP "USB-C" pattern from the framework landscape note.
- **`company/`** — static context (policies, handbook, services) loaded into the context pack. Changes infrequently → good candidate for caching.
- **`projects/{project_id}/`** — per-project isolation. Each folder contains:
  - `meetings_vtt/` — raw transcript input
  - `meeting_summary/` — Agent 2 (Summarizer) output
  - `context_pack/` — built or cached context (the "Check Context Pack" decision node)
  - `evidence_bundles/` — structured extraction output (Agent 3 output)
  - `logs/` — audit trail per run
- **`metadata.json`** — project-level config agents read before processing (name, participants, date range, etc.)

### Connection to the n8n workflow

The "Check Context Pack → IF: Needs Rebuild" branch maps directly to:

```
S3: projects/{project_id}/context_pack/
  → exists + fresh?  → Use Cached Pack  (skip LLM rebuild)
  → stale/missing?   → Build Context Pack from company/ + meetings_vtt/
```

This is KV cache reuse at the file system level — same concept as GroundSense latency optimization, different layer.
