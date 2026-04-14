---
title: Replication strategy in DDBMS
category: General
priority: Medium
starred: None
created: 2025-12-03T23:57:38.605964
updated: 2025-12-04T10:25:50.217748
dg-publish: true
---
# Replication strategy in DDBMS

**Priority:** Medium

## Conversation

### Assistant

Yes — in **vertical fragmentation**, an `UPDATE` on the logical table must be **split into multiple sub-updates**, each sent to the fragment that owns the affected columns.

This process has a formal name and a standard architectural pattern.

---

# 1. What is this operation called?

### **“Update Decomposition”**  
or  
### **“Operation Decomposition for Vertical Fragmentation”**

Academic term: **Vertical Fragment Recomposición / Decomposition**  
Industry term: **Update routing** or **fragment-aware update splitting**.

In distributed DBMS literature, this is part of:

### **“Query decomposition and data localization”**

Specifically, the part that handles **modification statements**.

---

# 2. Why do we need decomposition?
Because in vertical fragmentation:

- Column groups live in **different physical fragments**
- A single logical row spans **multiple tables/nodes**
- Updates touch only the fragments containing those specific columns

Example:  
Table User(id, name, email, address, preferences)

Fragments:
- F1: (id, name, email)
- F2: (id, address)
- F3: (id, preferences)

Logical command:
```
UPDATE User SET address='X', email='Y' WHERE id=101;
```

Must be decomposed into:

```
UPDATE F1 SET email='Y' WHERE id=101;
UPDATE F2 SET address='X' WHERE id=101;
```

F3 is untouched, so no query sent.

---

# 3. How is this usually performed?

Below is the architect-level view of the normal workflow.

---

## **Step 1. Parse the UPDATE statement**
Master/coordinator extracts:
- Columns being updated  
- WHERE clause  
- Target table / logical entity  

---

## **Step 2. Consult Fragmentation Metadata**
The metadata store contains information like:

| Fragment | Columns |
|---------|----------|
| F1 | id, name, email |
| F2 | id, address |
| F3 | id, preferences |

Coordinator determines **which fragments are impacted**.

---

## **Step 3. Decompose UPDATE into Sub-operations**
The coordinator generates one sub-update per fragment:

- For F1 → updates related columns  
- For F2 → related columns  
- For F3 → nothing  

This is done by the **query decomposition engine** (or “rewrite stage”).

---

## **Step 4. Route Each Sub-update to the Right Node**
Each fragment usually resides on a different node.

Coordinator sends:
- F1 update to Node A  
- F2 update to Node B  

If fragments are replicated → both primary and replica get updates via WAL.

---

## **Step 5. Ensure Atomicity Across Fragments**
Because updates refer to one logical row, the system must ensure they succeed together.

Three common techniques:

### **1. Two-Phase Commit (2PC)**
Coordinator:
- PREPARE each fragment  
- COMMIT when all agree  
- Ensures atomicity  
Used in distributed SQL systems.

### **2. Mini-Transactions / Write-Batches**
Raft/Paxos-based DBs batch changes across fragments using a single consensus log entry.

### **3. Eventual Consistency (AP systems)**
Some NoSQL systems accept per-fragment updates without an atomic guarantee.

---

## **Step 6. Log the Operation (WAL)**
Each fragment’s node writes *its own WAL entry* for the part of the update it handles.

The master may also log the logical update.

---

# 4. What is this entire process called in DBMS literature?

Formally it is part of:

### **“Distributed Query Processing: Query Decomposition + Data Localization”**

Modification-specific name:

### **“Update Decomposition & Localization in Vertically Fragmented Databases”**

Industry/non-academic equivalents:

### **“Update routing”**  
### **“Fragment-aware update execution”**  
### **“Column-group dispatching”** (cloud DBs)

---

# 5. Short senior-architect summary

When a logical UPDATE affects a vertically fragmented table, the coordinator:  
1. Identifies which fragments own the updated columns  
2. Splits the update into fragment-level statements  
3. Routes each to the correct fragment node  
4. Ensures atomicity (2PC or consensus)  
5. Relies on fragment-level WAL for recovery  
6. Ensures correctness via LSN coordination and anti-entropy if needed

This is what enables vertical sharding to function as a single logical table.

---

If you want, I can also produce:

- A **small diagram showing update decomposition**  
- A **Java class design** (`FragmentMapper`, `UpdateDecomposer`, `FragmentExecutor`)  
- An **Obsidian note** summarizing this process  
- Sample pseudocode for your DDBMS project

---

