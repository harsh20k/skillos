---
title: Email draft request
category: Health
priority: Medium
starred: None
created: 2025-12-16T10:13:20.047326
updated: 2025-12-16T11:15:40.036707
dg-publish: true
---
# Email draft request

**Priority:** Medium

## Conversation

### Assistant

```markdown
## What is SRE (Site Reliability Engineering)

**SRE = applying software engineering to operations.**  
It is an engineering role focused on **reliability, scalability, and resilience** of production systems.

Originally defined by **Google**.

---

## Core Idea (One Sentence)

> **SREs write code to keep systems reliable, instead of manually operating them.**

---

## What SREs Actually Do

### 1. Reliability Engineering
- Define **SLIs, SLOs, SLAs**
- Decide how reliable is *reliable enough*
- Balance reliability vs feature velocity

Example:
- 99.9% uptime = ~43 minutes downtime/month
- 99.99% uptime = ~4 minutes downtime/month

---

### 2. Automation (Key Difference from Ops)

SREs **automate themselves out of repetitive work**:
- Auto-scaling
- Self-healing systems
- Automated rollbacks
- Chaos testing

If it requires a manual runbook → SRE tries to eliminate it.

---

### 3. Production Ownership
- On-call rotations
- Incident response
- Root Cause Analysis (RCA)
- Postmortems (blameless)

Failure is expected — **unpreparedness is not**.

---

### 4. Performance & Capacity Planning
- Load testing
- Latency analysis
- Capacity forecasting
- Cost vs reliability trade-offs

---

## SRE vs DevOps vs Ops (Clear Comparison)

| Aspect | Ops | DevOps | SRE |
|---|---|---|---|
| Nature | Operations | Culture / practice | Engineering role |
| Code-heavy | Low | Medium | **High** |
| Automation | Manual + scripts | CI/CD focused | **Systemic automation** |
| On-call | Yes | Sometimes | **Yes (engineering-grade)** |
| Metrics | Uptime | Deployment speed | **SLOs, error budgets** |

---

## Error Budget (SRE-Specific Concept)

Error Budget =  
`100% − SLO`

Example:
- SLO = 99.9%
- Error budget = 0.1%

If the error budget is exhausted:
- 🚫 Feature launches pause
- 🛠 Focus shifts to reliability

This is how SRE **forces business–engineering alignment**.

---

## Skills Expected in SRE (2026–2027)

**Strong**
- Linux internals
- Networking basics
- Distributed systems
- Monitoring & alerting

**Programming**
- Python / Go / Java
- Writing tools, not just scripts

**Cloud**
- AWS / GCP
- Kubernetes
- Terraform

**Data**
- Metrics (Prometheus)
- Logs
- Traces

---

## SRE vs Software Engineer

| Software Engineer | SRE |
|---|---|
| Builds features | Builds reliability |
| Writes product code | Writes infra & tooling code |
| Feature metrics | Reliability metrics |
| Few outages affect them | All outages involve them |

---

## When Companies Hire SREs

- Scale > few hundred services
- High uptime requirements
- Revenue tied to availability
- Microservices + cloud complexity

Startups rarely hire SREs early.  
Mid-to-large companies do.

---

## Why SRE Fits Your Profile

Given your focus on:
- WAL & replication
- Distributed DBs
- Cloud & data pipelines

**SRE is a natural extension**, especially:
- Platform SRE
- Data Platform SRE
- Cloud Infrastructure SRE

---

## One-Line Definition (Interview-Ready)

> **SRE is an engineering role that uses software, automation, and metrics to ensure systems are reliable, scalable, and sustainable in production.**

---

