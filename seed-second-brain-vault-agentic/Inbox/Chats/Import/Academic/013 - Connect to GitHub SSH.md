---
title: Connect to GitHub SSH
category: Academic
priority: Medium
starred: None
created: 2025-12-19T20:54:57.849627
updated: 2025-12-19T23:15:08.423157
dg-publish: true
---
# Connect to GitHub SSH

**Priority:** Medium

## Conversation

### Assistant

Below is a clean **CI maturity ladder**, from “lightweight” to “enterprise”, in **plain language**.

---

## Level 1 — Lightweight CI (what we discussed)
**Example:** GitHub Actions self-hosted runner on one machine

### What it looks like
- 1–2 machines
- Jobs run directly on host OS
- Minimal isolation
- Manual scaling

### Used by
- Solo devs
- Small teams
- Side projects
- Early-stage startups

### Limits
- One bad job can break the runner
- Scaling = buy another machine
- Weak isolation

---

## Level 2 — **Standard / Intermediate CI (most companies)**
This is what people usually mean by a “proper CI system”.

image_group{"query":["CI pipeline architecture diagram","Docker based CI runner architecture","Kubernetes CI runners architecture diagram"]}

### Core idea
> **Jobs run in isolated, disposable environments** managed automatically.

---

### Typical architecture
```
GitHub / GitLab
   ↓
CI Orchestrator
   ↓
Ephemeral Workers (Docker containers or VMs)
```

---

### Key characteristics

#### 1. Isolation by default
- Each job runs in:
  - Docker container **or**
  - Short-lived VM
- Clean environment every run

#### 2. Elastic scaling
- Runners start **on demand**
- Destroyed after job finishes
- Scale from 1 → 100s automatically

#### 3. Centralized control
- Logs
- Artifacts
- Caching
- Secrets management
- Retry logic

---

### Common implementations

#### Docker-based CI
- GitHub Actions + Docker
- GitLab Runner (Docker executor)
- Jenkins + Docker agents

Jobs:
```yaml
runs-on: ubuntu-latest
container: python:3.12
```

---

#### VM-based CI
- GitHub-hosted runners
- GitLab SaaS runners
- Jenkins with cloud agents (AWS/GCP/Azure)

Better isolation, slower startup.

---

### What problems this level solves
| Problem | Solved |
|------|------|
| Host pollution | Yes |
| Dependency conflicts | Yes |
| Security | Better |
| Parallel jobs | Yes |
| Reproducibility | High |

---

### Who uses this level
- 10–200 engineer teams
- Most SaaS companies
- University research labs
- Regulated startups

This is the **industry default**.

---

## Level 3 — Advanced CI (platform teams)
Now CI becomes **infrastructure**, not tooling.

image_group{"query":["Kubernetes CI/CD platform architecture","Tekton CI pipeline architecture","Argo Workflows CI architecture"]}

### Architecture
- Kubernetes cluster
- CI runs as pods
- Custom schedulers
- Policy enforcement

### Tools
- Tekton
- Argo Workflows
- Jenkins on Kubernetes
- Buildkite + K8s

---

### Capabilities
- Multi-tenant isolation
- Cost-aware scheduling
- Custom resource types (GPU, TPU)
- Compliance controls
- Self-service pipelines

---

### Used by
- Large tech companies
- Cloud providers
- Fintech, defense, healthcare
- Teams with platform engineers

---

## Level 4 — Enterprise CI (Google / Meta scale)
CI is indistinguishable from compute fabric.

image_group{"query":["large scale CI infrastructure diagram","Bazel build farm architecture","Google build system CI architecture"]}

### Characteristics
- Build farms
- Remote execution
- Hermetic builds
- Massive caching layers
- Custom schedulers

---

## Simple comparison table

| Level | Isolation | Scale | Ops cost | Typical tools |
|----|----|----|----|----|
| Lightweight | ❌ | Manual | Low | Self-hosted GHA |
| **Intermediate** | ✅ | Auto | Medium | GitHub/GitLab CI |
| Advanced | ✅✅ | Elastic | High | K8s-based CI |
| Enterprise | ✅✅✅ | Massive | Very high | Bazel, custom |

---

## One-line summary
> **Lightweight CI** = a machine running jobs  
> **Intermediate CI** = disposable workers with orchestration  
> **Advanced CI** = CI as a platform  
> **Enterprise CI** = CI as compute infrastructure

---

If you want, I can:
- Map **your current setup** to this ladder
- Suggest **the next upgrade step**
- Draw a **before/after diagram**
- Explain **which level Dal / most startups use**

Just say which one.

---

