---
title: GDC update coordination
category: Projects
priority: Medium
starred: None
created: 2025-11-29T12:27:22.425896
updated: 2025-11-29T12:43:20.204786
dg-publish: true
---
# GDC update coordination

**Priority:** Medium

## Conversation

### Assistant

```markdown
# How GDC Handles Updates in Replicated Tables (Distributed DBMS)

## 1. GDC Tracks Replica Metadata
The Global Directory/Coordinator (GDC) maintains:
- Locations of all replicas  
- Mapping of tables/fragments → nodes  
- Which replicas must receive updates  

This lets the GDC know where every update should be propagated.

---

## 2. Update Coordination Workflow

### **Step A — Client Issues an UPDATE**
The request goes to a designated **primary replica** or **transaction coordinator**.

### **Step B — GDC/Coordinator Starts a Distributed Transaction**
It identifies all participating replica nodes.

### **Step C — Concurrency Control to Prevent Conflicts**
Two approaches:

#### **1. Primary-Copy Protocol**
- One node = update master  
- All updates go through the master  
- Other replicas pull changes  
- No conflicts (only one writer)

#### **2. Distributed Concurrency Control**
If any replica can accept writes:
- **Two-Phase Locking (2PL)** → distributed locks  
- **Timestamp Ordering** → older timestamps win  
Ensures a consistent global order of updates.

---

## 3. Propagation Using Atomic Commit

### **Two-Phase Commit (2PC)**
1. **Prepare Phase:** replicas check if they can commit  
2. **Commit Phase:** all commit or all rollback  

Or modern systems may use:
- **Three-Phase Commit**  
- **Raft / Paxos consensus**

Guarantees *all* replicas update together.

---

## 4. Handling Conflicting Updates
If multiple nodes try to write the same row:
- GDC enforces locks or timestamps  
- Only one valid order of writes is accepted  
- Replicas apply changes using that global order  

Thus, conflicts never appear across replicas.

---

## 5. Failure and Recovery
When a replica is down:
- Coordinator may use majority quorum  
- Missed updates stored in logs  
- Replica catches up via:
  - **Version vectors**
  - **Log Sequence Numbers (LSNs)**
  - **Replay of commit log**

No conflict because every update has a **global version/timestamp**.

---

## Summary Table

| Step | Description |
|------|-------------|
| 1 | GDC knows all replica locations |
| 2 | Coordinator selects update node |
| 3 | Locks/timestamps ensure ordered updates |
| 4 | 2PC/consensus propagates updates |
| 5 | All replicas commit consistently |
| 6 | Failed nodes sync using logs |

**Result:** All nodes always converge on the same data with no conflicts.
```

---

