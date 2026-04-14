---
title: CQRS vs CRUD
category: General
priority: Medium
starred: None
created: 2025-12-28T14:40:04.886443
updated: 2025-12-28T14:40:21.074939
dg-publish: true
---
# CQRS vs CRUD

**Priority:** Medium

## Conversation

### Assistant

## CQRS vs CRUD

image_group{"query":["CQRS architecture diagram","CRUD architecture REST diagram","CQRS read write separation diagram","traditional CRUD service architecture"]}

### CRUD (Create, Read, Update, Delete)
**What it is**
- A single model and interface handles **reads and writes**.
- Common in REST APIs and simple services.

**Characteristics**
- One data model for both read/write.
- Simple mental model and implementation.
- Strong consistency is straightforward.
- Scales vertically first; horizontal scaling can be harder under read-heavy loads.

**When it fits**
- Small to medium systems.
- Low to moderate traffic.
- Minimal domain complexity.

---

### CQRS (Command Query Responsibility Segregation)
**What it is**
- **Commands** (writes) and **Queries** (reads) are **separate paths**, often with different models and even different databases.

**Characteristics**
- Write model optimized for invariants and business rules.
- Read model optimized for fast queries (denormalized, cached).
- Enables independent scaling of reads vs writes.
- Often paired with **event sourcing**, but not required.
- Introduces eventual consistency between write and read sides.

**When it fits**
- Read-heavy systems.
- Complex domains with many business rules.
- High scalability or performance requirements.
- Systems benefiting from multiple read views (dashboards, analytics).

---

### Side-by-side comparison

| Aspect | CRUD | CQRS |
|---|---|---|
| Data model | Single | Separate read & write models |
| Complexity | Low | Medium–High |
| Consistency | Typically strong | Often eventual |
| Scalability | Limited | High (independent scaling) |
| Read optimization | Limited | Excellent |
| Learning/ops cost | Low | Higher |

---

### Rule of thumb
- **Start with CRUD**.  
- Move to **CQRS only when**:
  - Reads dominate writes **and** performance matters, or
  - Domain complexity is hurting a single-model design, or
  - You need multiple optimized read projections.

If you want, I can map this to a concrete example (e.g., flight booking, order system, or a distributed DB project) or show how CQRS would look using REST + Kafka.

---

