---
title: Calgary vs Halifax Population
category: Projects
priority: Medium
starred: None
created: 2025-12-23T16:04:17.775968
updated: 2025-12-24T09:20:59.032589
dg-publish: true
---
# Calgary vs Halifax Population

**Priority:** Medium

## Conversation

### Assistant

Yes — there are **self-hosted alternatives to AWS Lambda** that you can run locally (including on your MacBook). These let you build a **serverless-style system** without AWS.

Below are the most practical options, with pros/cons and typical use cases.

---

## 1) **OpenFaaS**

image_group{"query":["OpenFaaS architecture diagram","OpenFaaS function UI","OpenFaaS flow with Docker","OpenFaaS on Kubernetes"]}

**What it is**  
OpenFaaS (“Functions as a Service”) — serverless functions running on your infrastructure.

**How it runs locally**  
- Docker
- Kubernetes (optional for scale)

**Deploy:**  
```bash
brew install faas-cli   # CLI
```

**Use case**
- Event-driven jobs
- HTTP/webhook functions
- Local testing + cluster

**Pros**
- Simple
- Works with Docker
- UI dashboard
- Supports many languages

**Cons**
- Not bound to cloud events by default
- You manage scaling yourself

---

## 2) **Knative (on Kubernetes)**

image_group{"query":["Knative serverless on Kubernetes","Knative architecture diagram","Kubernetes serverless with Knative","Knative eventing"]}

**What it is**  
Serverless layer on Kubernetes (scales to zero, event triggers).

**Run locally**
- Kind (Kubernetes in Docker)
- Minikube
- Docker Desktop’s Kubernetes

**Use case**
- Production-like serverless
- Auto-scaling workloads
- Cloud-native events (Kafka, HTTP, cron)

**Pros**
- True K8s serverless
- Scale to zero
- Powerful triggers

**Cons**
- Requires Kubernetes
- More complex to set up

---

## 3) **Apache OpenWhisk**

image_group{"query":["Apache OpenWhisk architecture","OpenWhisk with Docker","Apache OpenWhisk functions"]}

**What it is**  
Open source serverless platform (foundation of IBM Cloud Functions).

**Run locally**
- Docker Compose
- Vagrant

**Use case**
- Event-driven pipelines
- Cron jobs
- Pub/Sub

**Pros**
- Mature
- Multiple trigger types

**Cons**
- Setup heavier than Faas

---

## 4) **Riff (Project by VMware)**

**What it is**  
FaaS built on Knative.

**Run locally**
- Kubernetes + Knative underneath

**Pros**
- Integrates with Spring, Kafka
- Event triggers

**Cons**
- Same K8s complexity

---

## 5) **LocalStack (for AWS emulation)**

**What it is**  
Local AWS stack (Lambda, S3, DynamoDB, etc.) in Docker.

**Use case**
- **AWS Lambda emulation**
- Dev/test for AWS workflows

**Pros**
- AWS-like locally
- Good for CI

**Cons**
- Not a production serverless engine

---

## 6) **faasd (lightweight OpenFaaS)**

**What it is**  
OpenFaaS but **without Kubernetes**, runs on Docker only.

**Very good for local**
```bash
curl -sSL https://get.openfaas.com | sudo sh
```

**Pros**
- Minimal
- Fast
- Great for local dev

**Cons**
- Fewer enterprise features

---

## 7) **Kubeless**

**What it is**  
Serverless layer built on Kubernetes, similar to Knative.

**Pros**
- Simple if you know K8s

**Cons**
- K8s dependency

---

# Quick comparison

| Platform | Needs Kubernetes? | Local friendly | Scale to zero | Event triggers |
|---|---|---|---|---|
| **OpenFaaS** | Optional | ✔️ | Yes (with faasd) | HTTP + custom |
| **faasd** | ❌ | ✔️ | Yes | HTTP |
| **Knative** | ✔️ | ✔️ | ✔️ | Kafka, HTTP, cron |
| **OpenWhisk** | Optional | ✔️ | Yes | Multiple |
| **LocalStack** | ❌ | ✔️ (AWS API) | No | AWS events |

---

## How a self-hosted “Lambda” fits your Kafka + Python + PostgreSQL

Without AWS:

```
Kafka → Self-hosted FaaS → PostgreSQL
```

You can make:
- **Producer** → push to Kafka via HTTP
- **FaaS function** → trigger on Kafka events → write to Postgres

Examples:
- **OpenFaaS function** triggered by HTTP or custom event
- **Knative function** triggered by Kafka topic
- **OpenWhisk action** triggered by Kafka or cron

---

## Which one to choose on your MacBook

| Your need | Best fit |
|---|---|
| Simple, few functions | **faasd / OpenFaaS** |
| Want AWS-like locally | **LocalStack** |
| Production-like serverless | **Knative** |
| Many trigger types | **OpenWhisk** |

---

## Minimal setup on MacBook (example)

### Using **OpenFaaS (faasd)**
1. Install faas CLI  
   ```bash
   brew install faas-cli
   ```
2. Install faasd  
   ```bash
   curl -sSL https://get.openfaas.com | sh
   ```
3. Create a Python function
   ```bash
   faas-cli new hello-python --lang python3
   ```
4. Deploy
   ```bash
   faas-cli up -f hello-python.yml
   ```
5. Invoke
   ```bash
   curl http://localhost:8080/function/hello-python
   ```

---

## When self-hosted makes sense

✔ You want **serverless locally**  
✔ No cloud vendor lock-in  
✔ Testing and prototyping  
✔ Event workflows

---

## When to avoid self-hosted serverless

✘ You need **auto maintenance**  
✘ You need **global scale**  
✘ You need **managed SLA support**

---

If you want, I can provide:
- a **step-by-step lab** with **Kafka + OpenFaaS + PostgreSQL**
- a **docker-compose.yml** for local serverless + Kafka pipeline
- code samples for **Python functions** for each option

Tell me which one you want.

---

