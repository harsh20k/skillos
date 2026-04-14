---
title: Practice questions session
category: General
priority: Medium
starred: None
created: 2025-10-30T10:57:03.702700
updated: 2025-11-04T10:36:48.253145
dg-publish: true
---
# Practice questions session

**Priority:** Medium

## Conversation

### Assistant

Good question — and yes, **to some extent it does**, but not entirely.  

Here’s the clear picture:  

---

### 🔹 2PL doesn’t eliminate parallelism — it *controls* it.  

- Multiple transactions **can still run in parallel** as long as they **don’t need the same data item**.  
- 2PL **only blocks** when two transactions **conflict** on the same item (one wants to write or both want to write).  

So parallel execution still happens — it’s just **safe parallelism**.  

---

### 🔹 What actually slows down
- If transactions access overlapping data, 2PL introduces **waiting** (one transaction holds the lock, others queue).  
- In workloads with **lots of contention** (many transactions hitting the same records), performance drops.  
- But with **independent data**, transactions still proceed concurrently.  

---

### 🔹 Example
```
T1 → updates Account#1
T2 → updates Account#2
```
No conflict → both proceed in parallel. ✅  

But:
```
T1 → updates Account#1
T2 → reads Account#1
```
Conflict → T2 must **wait** until T1 releases its lock. ⏳  

---

### 🔹 Summary
| Property | Effect |
|-----------|---------|
| **Safety** | Guarantees serializability (no inconsistent results) |
| **Parallelism** | Allowed between non-conflicting transactions |
| **Trade-off** | Some blocking, but ensures correctness |

---

So yes — 2PL **reduces** parallelism where data overlaps,  
but it **preserves** as much concurrency as possible **without breaking consistency**.

---

