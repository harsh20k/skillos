---
title: Python diagrams animation options
category: Technical
priority: Medium
starred: None
created: 2025-12-11T23:24:31.195492
updated: 2025-12-12T08:09:25.367116
dg-publish: true
---
# Python diagrams animation options

**Priority:** Medium

## Conversation

### Assistant

**Short answer:**  
**HTTP is the industry standard. WebSockets are not.**

---

## What industry actually uses

### 1. **HTTP-based communication (standard)**
Used in:
- Database clients ↔ coordinators
- Coordinators ↔ replicas
- Control-plane APIs
- Metadata services

Common forms:
- **HTTP/REST**
- **HTTP/2**
- **gRPC (over HTTP/2)**

Why:
- Stateless by default
- Easy retry semantics
- Load-balancer friendly
- Works well with failures and partitions

---

### 2. **WebSockets (rare in DB internals)**
Used mainly for:
- Client-facing real-time applications
- Dashboards / monitoring
- Change feeds to UI

**Almost never used** for:
- Replication
- Consensus
- Write propagation
- Internal DB coordination

Reason:
- Long-lived connections are fragile
- Harder failure detection
- Poor fit for retry/timeout semantics
- Backpressure handling is complex

---

## What real systems do

| System | Internal communication |
|-----|-----------------------|
| PostgreSQL | Custom TCP protocol |
| MySQL | Custom TCP protocol |
| MongoDB | Custom binary protocol over TCP |
| Cassandra | Custom protocol over TCP |
| CockroachDB | gRPC / HTTP2 |
| Spanner | gRPC |
| Etcd | gRPC |
| Kafka | Custom TCP protocol |

**None use WebSockets internally.**

---

## Why HTTP / gRPC is preferred

### Failure handling
- Explicit timeouts
- Easy retries
- Idempotent requests

### Observability
- Works with tracing (OpenTelemetry)
- Easy logging, metrics, auditing

### Infrastructure compatibility
- Load balancers
- Service meshes
- TLS termination
- Firewalls

---

## Where WebSockets *do* make sense
- Admin dashboards
- Live replication status views
- Real-time query progress updates
- CDC streams to UIs

Even then:
> WebSockets are **edge-facing**, not **core DB internals**.

---

## Clear recommendation for your project
For a **distributed DBMS project**:

### Use:
- **HTTP / REST** for simplicity  
or  
- **gRPC** if you want to look industry-grade

### Avoid:
- WebSockets for node-to-node DB communication

---

## Simple decision rule
- **System-to-system DB communication** → HTTP / gRPC / TCP  
- **Human-facing real-time updates** → WebSockets  

---

If you want, I can:
- Recommend **HTTP vs gRPC** for your exact project scope
- Help design a **clean replication API**
- Show how retries, timeouts, and idempotency are handled

Just say which direction you want to go.

---

