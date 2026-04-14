---
date: 2026-04-09
tags: [project-breakdown, agentic-ai, portfolio, data-quality, aws, bedrock]
parent: "[[Project Ideas — AI Agent (Industry Grounded)]]"
score: 9/10
---

# Data Quality Monitoring Agent

> Every company with a data warehouse needs this. No good autonomous solution exists yet.

**Original rating:** 9/10 — strongest fit with AWS/Bedrock stack, most differentiated for Agentic AI roles.

---

## What It Does

Watches incoming data pipelines (streaming or batch), detects anomalies in data quality (null spikes, schema drift, value distribution shifts), traces where bad data originated, and alerts the right team with a structured diagnosis — not just a raw error.

**Real-world precedent:** Used in production at Amazon, Uber, and any company running a data lakehouse. Great Plains Energy, TD, and RBC-scale orgs in Canada are actively building this.

---

## Agentic AI Concepts You'll Learn

| Concept | How It Applies Here |
|---|---|
| **Tool use** | Agent calls tools to query pipeline stats (CloudWatch metrics, Glue job logs, S3 data samples) |
| **Multi-step reasoning** | Detect anomaly → identify scope → trace upstream origin → classify severity → route alert |
| **Orchestrator-Worker pattern** | Orchestrator agent delegates to specialist sub-agents: one for schema validation, one for statistical drift, one for lineage tracing |
| **Memory (session + persistent)** | Store baseline data profiles to compare incoming data against over time |
| **RAG** | Retrieve historical anomaly records and past diagnoses to enrich current assessment |
| **Guardrails** | Prevent false positive alerts flooding teams — build confidence thresholds before escalating |
| **LLM-as-Judge** | Evaluate whether a generated diagnosis is accurate before sending to human reviewer |
| **Observability & evals** | Monitor agent turn latency, tool call success rates, alert precision vs recall |
| **Human-in-the-loop** | Agent escalates ambiguous anomalies to a data owner with a draft diagnosis for approval |
| **Event-driven / scheduled agents** | Agent triggered by Kinesis stream events or CloudWatch alarms, not just user prompts |

**Learning density: very high.** This single project touches nearly every core agentic pattern.

---

## How to Build It (Your Stack)

```
Trigger: CloudWatch Alarm / Kinesis Data Stream event
  → Lambda invokes Bedrock Agent
  → Agent calls tools:
      - get_pipeline_stats() → Glue job metrics, record counts
      - sample_data() → pull S3 sample, check null rates / schema
      - get_lineage() → trace upstream source system
      - get_historical_anomalies() → Bedrock KB query (RAG)
  → Agent generates structured diagnosis
  → LLM-as-Judge validates diagnosis quality
  → SNS alert to Slack / PagerDuty with diagnosis
```

This is a direct extension of GroundSense — swap hazard assessment for data assessment.

---

## Job Market Demand — Canada / Nova Scotia

**Keywords employers use:** `data quality engineer`, `data observability`, `MLOps engineer`, `data reliability engineer`, `AI agent`, `pipeline monitoring`, `Monte Carlo`, `Great Expectations`

| Market | Demand | Notes |
|---|---|---|
| Canada (national) | 🔴 Very High | Data engineering + AI is one of the top 5 fastest-growing tech roles in Canada (Robert Half 2026). Every org with a warehouse needs this. |
| Toronto / Vancouver | 🔴 Very High | Financial services, e-commerce, and SaaS companies actively hiring data quality engineers with AI/ML skills. |
| Nova Scotia / Halifax | 🟡 Medium | Smaller market but government data systems, Dalhousie research, and financial services branches (RBC, TD) all have data quality needs. Remote roles are abundant. |

**Salary range (Canada):** $110,000–$165,000 CAD for senior data/AI engineers with agentic skills.

---

## Employability Score for Harsh

**Score: 9 / 10**

| Factor | Assessment |
|---|---|
| Stack alignment | ✅ Direct — AWS Bedrock, Lambda, CloudWatch, Kinesis, S3 all apply |
| Builds on GroundSense | ✅ Straightforward extension of existing architecture |
| Differentiation | ✅ Very high — few candidates have built an autonomous data quality agent |
| Interview impact | ✅ High — easy to demo with synthetic pipeline data; maps to real enterprise pain |
| Nova Scotia relevance | 🟡 Moderate — most roles are remote or in larger centres, but fully accessible |
| Learning ROI | ✅ Covers the most agentic AI concepts per hour of build time |

**Why this is your best bet:** You can build a working demo in 2–3 weeks using your existing AWS/Bedrock knowledge. It's defensible in interviews ("I built an autonomous agent that detects data anomalies, traces their origin, and generates a structured diagnosis — all without human input"). No other junior candidate is pitching this.

---

## Related Notes
- [[Project Ideas — AI Agent (Industry Grounded)]]
- [[GroundSense Architecture]]
- [[Orchestrator-Worker Pattern]]
- [[LLM-as-Judge Evaluation]]
- [[Latency & Observability]]
