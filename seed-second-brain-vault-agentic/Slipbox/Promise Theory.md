---
creation date: 2025-12-30 17:10
tags: [concept]
dg-publish: true
---
Promise Theory in Kubernetes is a way of thinking about the cluster as a set of autonomous components that each **declare** what they will do (their “promises”), instead of being centrally commanded step‑by‑step. It explains why K8s is declarative, eventually consistent, and resilient in the face of failure.

## Core idea of Promise Theory

- Promise Theory models a system as autonomous agents that voluntarily publish their intentions to each other as promises (e.g., “I will provide X service”). These promises are about the agent’s own behaviour, not about forcing others to act. [4][6]
- The overall system behaviour emerges from these local promises and their verification (other agents observe whether promises are kept), rather than from a single controller issuing obligations. [4][8]

## How this maps to Kubernetes

- In Kubernetes, each major component can be seen as an agent making promises: a Pod promises to run a container, a Deployment promises to maintain N replicas, and the control plane promises to reconcile actual state toward the declared state. [5][11]
- Kubernetes users declare desired state (YAML manifests), and the system is responsible for “keeping the promise” that the actual cluster will converge to that state over time, despite node failures, pod crashes, and dynamic scaling. This is a practical application of an intent‑driven, promise‑based model. [1][5]

## Why this matters conceptually

- Because each component is autonomous, the system tolerates partial failure: when a node dies, the scheduler and controllers still keep their promises by rescheduling pods elsewhere, rather than being blocked by a central imperative script that failed mid‑run. [1][11]
- Thinking in Promise Theory terms leads to designs where interfaces are “I will provide X” contracts (e.g., a Service promising stable access to pods) and where coordination is about trust and verification of promises, not about tightly coupled imperative orchestration. [4][6]

## Contrast with imperative/obligation models

- In an obligation model (e.g., a big imperative deployment script), a central actor issues commands like “create VM, then install package, then start process,” and correctness depends on that sequence running successfully in a specific environment. [1][8]
- In the promise‑based Kubernetes model, agents only promise their own behaviour in the conditions they actually observe (e.g., kubelet on a node promises to run the assigned pods if resources permit), which tends to produce more predictable and assessable outcomes in distributed, unreliable environments. [4][8]

## How to use this mental model as an engineer

- When designing workloads on K8s, frame resources as promises: “This Deployment promises at least 3 replicas,” “This HPA promises to adjust replicas in response to load,” “This operator promises to reconcile a CRD into underlying infrastructure.” [10][11]
- For system design and team design, Promise Theory plus Kubernetes suggests: define clear, local responsibilities (what each component/team promises), minimize assumptions about others’ internal behaviour, and rely on observable outcomes and feedback to verify promises. [2][6]

Sources
[1] Promise Theory & it's relevance in Kubernetes! - FAUN.dev() https://faun.pub/promise-theory-its-relevance-in-kubernetes-a9c78c16d858
[2] Promise Theory and the Tight-Loose-Tight Model https://www.cowork.no/blogg/promise-theory-and-the-tight-loose-tight-model-leadership-lessons-from-kubernetes
[3] 0.2 - Learn Kubernetes: Conway's Law, Promise Theory ... https://www.youtube.com/watch?v=uRdp1zbbq4s
[4] Promise theory https://en.wikipedia.org/wiki/Promise_theory
[5] Kubernetes Promise Theory: How K8s Keeps Its Promises - LinkedIn https://www.linkedin.com/posts/v-chaudhary_kubernetes-promises-me-every-day-and-every-activity-7370703239769571328-xcse
[6] Promise Theory https://lab.abilian.com/Tech/Theory/Promise%20Theory/
[7] SOME NOTES ABOUT PROMISE THEORY - Mark Burgess http://markburgess.org/PromiseMethod.pdf
[8] Promise Theory—What Is It? https://www.linuxjournal.com/content/promise-theory%E2%80%94what-it
[9] Promise Theory - Salt Labs Documentation https://docs.saltlabs.tech/frameworks/promise-theory/
[10] What is Promise Theory? - Steve Cavallo https://static.sched.com/hosted_files/crossplanedayeu21/16/CrossplanePromiseTheory_SteveCavallo_4May_v1.pdf
[11] Celebrating 10 Years of Kubernetes - What Comes Next? https://devm.io/kubernetes/kubernetes-celebrating-10-years
[12] Promise Theory & it’s relevance in Kubernetes! https://faun.pub/promise-theory-its-relevance-in-kubernetes-a9c78c16d858?gi=70065f3d1c1d
[13] The design of Kubernetes is based on Promise Theory https://news.ycombinator.com/item?id=39236814
