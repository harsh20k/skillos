---
title: Mesh-based DBMS architecture
category: General
priority: Medium
starred: None
created: 2025-12-05T15:22:27.819047
updated: 2025-12-05T15:25:50.571648
dg-publish: true
---
# Mesh-based DBMS architecture

**Priority:** Medium

## Conversation

### Assistant

## Short Answer

**Paxos does *not* use a master–slave architecture.**  
It is a **peer-based consensus model** where **all nodes are logically equal**. Any node can act as a **proposer, acceptor, and learner** at different times.

There is **no permanent leader** in *basic Paxos*. Leadership, if used, is **temporary and optional** (called *leader-based Paxos* or *Multi-Paxos*).

---

## How Communication Actually Works

- **All nodes can talk to each other**
- Consensus is achieved by:
  - **Proposers → Acceptors**
  - **Acceptors → Learners**
- Decision is made when a **majority (quorum)** of acceptors agree

This is **peer-to-peer quorum-based coordination**, not command-and-control.

---

## Logical Architecture View

image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Paxos consensus diagram roles proposer acceptor learner","Paxos peer to peer architecture diagram","Paxos quorum communication diagram","Multi-Paxos leader optimization diagram"],"num_per_query":1}

**What the diagram represents:**
- Every node is equal
- Any node may initiate a proposal
- Majority voting decides the value
- No fixed master exists

---

## Paxos vs Master–Slave

| Feature | Paxos | Master–Slave |
|--------|--------|--------------|
| Permanent leader | ❌ No | ✅ Yes |
| All nodes equal | ✅ Yes | ❌ No |
| Who can propose | Any node | Only master |
| Failure tolerance | ✅ High | ⚠ Master is critical |
| Consensus | ✅ Quorum-based | ❌ Not true consensus |

---

## Important Clarification: Multi-Paxos

In **Multi-Paxos** (used in real systems):

- A **temporary leader is elected**
- But:
  - It can change at any time
  - If it fails → another node takes over automatically
- Still **not master–slave**, because authority is **not permanent**

---

## Final One-Line Summary

> **Paxos is a fully peer-based consensus system with no permanent master; all nodes are logically equal and coordinate using quorum voting.**

---

If you want, I can also:
- Compare **Paxos vs Raft visually**
- Show **how Paxos fits inside a distributed DB write path**
- Provide an **Obsidian-ready diagram + note** for your project.

---

