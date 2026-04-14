---
title: Categorisation Table
category: Academic
priority: Medium
starred: None
created: 2025-12-27T10:48:01.114440
updated: 2025-12-27T11:23:58.529628
dg-publish: true
---
# Categorisation Table

**Priority:** Medium

## Conversation

### Assistant

Below is a **current, industry-relevant view** of orchestrators used in **cloud-native systems** and **ML / AI projects**, grouped by *what they orchestrate*.

image_group{"query":["kubernetes cloud native architecture","kubeflow ml pipeline architecture","apache airflow dag","ray distributed computing architecture"]}

---

## 1. Core cloud-native orchestrators (foundation layer)

These run **everything else**.

| Orchestrator | What it Orchestrates | Where it’s used |
|---|---|---|
| **entity["organization","Kubernetes","container orchestration platform"]** | Containers, services, networking, scaling | GKE, EKS, AKS, on-prem, startups → enterprises |
| **entity["organization","K3s","lightweight kubernetes distribution"]** | Lightweight Kubernetes clusters | Edge, IoT, dev, small ML clusters |
| **entity["organization","Nomad","hashicorp workload scheduler"]** | Containers, VMs, batch jobs | Mixed workloads, HashiCorp stacks |

**Key idea:**  
> Kubernetes is the **operating system of the cloud**.  
Almost all modern ML orchestrators *sit on top of it*.

---

## 2. Workflow & data orchestration (pipelines, DAGs)

Used heavily in **data engineering + ML pipelines**.

| Orchestrator | Best For | Typical Use |
|---|---|---|
| **entity["organization","Apache Airflow","workflow orchestration tool"]** | DAG-based workflows | ETL, feature pipelines, model training triggers |
| **entity["organization","Prefect","data workflow orchestration"]** | Modern Airflow alternative | Python-first pipelines, retries, observability |
| **entity["organization","Dagster","data orchestration platform"]** | Data-quality-aware pipelines | Analytics + ML feature engineering |

**Mental model:**  
These orchestrate **steps**, not machines.

---

## 3. ML / AI-specific orchestration platforms

Built *specifically* for ML lifecycles.

| Orchestrator | What it Handles | Used By |
|---|---|---|
| **entity["organization","Kubeflow","kubernetes ml platform"]** | End-to-end ML pipelines on Kubernetes | Enterprises, research teams |
| **entity["organization","MLflow","machine learning lifecycle platform"]** | Experiments, models, deployment | Training → serving lifecycle |
| **entity["organization","Flyte","workflow orchestration for ml"]** | Large-scale ML workflows | Production ML systems |

**Key insight:**  
> Kubeflow = Kubernetes-native ML platform  
> MLflow = lifecycle & tracking  
> Flyte = scalable ML workflow engine

---

## 4. Distributed compute orchestration (AI / LLM workloads)

Used for **training, inference, and parallel compute**.

| Orchestrator | Speciality | Common Use |
|---|---|---|
| **entity["organization","Ray","distributed computing framework"]** | Parallel Python workloads | LLM training, inference, reinforcement learning |
| **entity["organization","Dask","parallel computing library"]** | Data-parallel processing | Large-scale data + ML preprocessing |
| **entity["organization","Apache Spark","distributed data processing engine"]** | Big data + ML | Feature engineering, large datasets |

**Trend:**  
Ray is becoming **very popular for AI/LLM orchestration**.

---

## 5. Cloud-managed orchestration (what companies actually use)

Most teams **don’t self-host everything**.

| Cloud | Orchestrator Stack |
|---|---|
| AWS | EKS + Airflow (MWAA) + SageMaker |
| GCP | GKE + Vertex AI + Kubeflow |
| Azure | AKS + Azure ML |
| Startups | Kubernetes + Ray + MLflow |

---

## One clean hierarchy to remember

```
Infrastructure orchestration → Kubernetes
Workflow orchestration       → Airflow / Prefect / Dagster
ML lifecycle orchestration   → Kubeflow / MLflow / Flyte
Distributed AI compute       → Ray / Spark / Dask
```

---

## Industry reality (important)

> **Kubernetes is the non-negotiable base skill**  
> ML orchestration tools change faster than Kubernetes.

If you want, I can:
- Map these orchestrators to **real ML system architecture**
- Show **a minimal AI stack (K8s + Ray + MLflow)**
- Align this with **Halifax / Canada job postings**

---

