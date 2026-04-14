---
creation date: 2025-12-29 12:18
tags:
  - chat
description:
dg-publish: true
---
# CSCI 5408 – Data Management, Warehousing & Analytics  
## **Comprehensive Exam Study Summary**

This document consolidates **all exam-relevant material** from lectures, notes, and #review highlights for **CSCI 5408**.  
Focus is on **definitions + scenario-based understanding**, as emphasized in the course.

---

## 1. Database Design & Modeling

### 1.1 Three-Schema Architecture ⭐ (#review)
**Purpose:** Separation of concerns and data abstraction.

1. **External Schema**
   - User views (apps, dashboards, reports)
   - Different views for different users

2. **Conceptual Schema**
   - Global logical structure
   - ER/EER models
   - Independent of physical storage

3. **Internal (Physical) Schema**
   - How data is actually stored
   - Indexes, files, partitions

➡️ **Why important:** Enables data independence and scalability.

---

### 1.2 ER & Enhanced ER (EER) Modeling ⭐ (#review)

#### Entity Types
- **Strong Entity**: Has its own primary key
- **Weak Entity**: Depends on another entity
  - Has **partial key**
  - Requires **total participation**

#### Attributes
- Simple vs Composite
- Single-valued vs **Multivalued**
- **Derived** attributes

#### Constraints
- **Cardinality**
- **Participation**
  - Total participation (mandatory)
  - Partial participation (optional)

#### Traps ⭐
- **Fan Trap**: Incorrect relationship ordering
- **Chasm Trap**: Implied relationship that may not exist

---

### 1.3 Specialization & Generalization ⭐ (#review)

- **Generalization**: Bottom-up (combine entities)
- **Specialization**: Top-down (split entities)

#### Constraints
| Type | Meaning |
|---|---|
| Total | Every superclass entity must belong to a subclass |
| Partial | Some entities may not belong to any subclass |
| Exclusive (Disjoint) | Entity can belong to only one subclass |
| Non-Exclusive (Overlapping) | Entity may belong to multiple subclasses |

---

### 1.4 Aggregation ⭐ (#review)
- Treats a **relationship as a higher-level entity**
- Used when relationships have attributes or need relationships themselves
- Avoids redundancy

---

## 2. ER-to-Relational Mapping Algorithm ⭐

1. **Regular Entity → Table**
2. **Weak Entity → Table**
   - PK = Owner PK + Partial Key
3. **Binary 1:1**
   - FK, Merge, or Separate relation
4. **Binary 1:N**
   - FK on N-side
5. **Binary M:N**
   - New table with combined PK
6. **Multivalued Attributes**
   - Separate table
7. **N-ary Relationships**
   - Separate relation
8. **Specialization Mapping**
   - Superclass + Subclasses
   - Subclass-only
   - Single table with type attribute(s)

---

## 3. Normalization ⭐

### Functional Dependencies
- **Partial Dependency**
- **Transitive Dependency**

### Normal Forms
- **1NF**: Atomic values only
- **2NF**: No partial dependency
- **3NF**: No transitive dependency

### Denormalization
- Used when **reads >> writes**
- Improves performance at cost of redundancy

---

## 4. Transactions & Concurrency

### 4.1 Transactions & ACID ⭐ (#review)
- **Atomicity**
- **Consistency**
- **Isolation**
- **Durability**

Transaction States:
- Active → Partially Committed → Committed
- Failed → Aborted

---

### 4.2 Schedules & Serializability ⭐

- **Schedule**: Execution order of transactions
- **Serial Schedule**
- **Non-Serial Schedule**

#### Conflict Serializability
- Uses **precedence graph**
- Serializable if graph is **acyclic**

#### View Serializability
- Same read-from & final writes
- More general but **NP-complete**
- Often impractical

---

### 4.3 Recoverability ⭐
- **Recoverable schedules**
- **Cascading rollbacks**
- **Cascadeless schedules** (preferred)

---

## 5. Concurrency Control

### Lock-Based
- Shared (S) vs Exclusive (X)
- Lock granularity: DB, Table, Page, Row

#### Two-Phase Locking (2PL)
- Growing phase
- Shrinking phase
- Guarantees serializability

### Deadlocks
- Prevention
- Detection
- Avoidance

#### Wait-Die vs Wound-Wait ⭐
- Wait-Die: Older waits, younger aborts
- Wound-Wait: Older aborts younger

### Timestamp-Based Control
- Global timestamps
- Higher overhead

### Optimistic Concurrency
- Read → Validate → Write
- Assumes low conflicts

---

## 6. Distributed Database Systems (DDBMS) ⭐

### Architectures
| Type | Memory | Disk | Scalability |
|---|---|---|---|
| Shared Memory | Shared | Shared | Low |
| Shared Disk | Private | Shared | Medium |
| Shared Nothing | Private | Private | High ⭐ |

---

### Transparency ⭐ (#review)
- Distribution
- Fragmentation
- Location
- Transaction
- Failure
- Performance
- Heterogeneity

#### Key Components
- **DGS** (Distributed Global Schema)
- **DDC** (Distributed Data Catalog)

---

### Distributed Transactions
- Remote Request
- Remote Transaction
- **Distributed Transaction**

#### Commit Protocols
- **2PC**: Blocking possible
- **3PC**: Reduces blocking

---

### Data Distribution
- **Replication**
  - Full / Partial
  - Push vs Pull
- **Fragmentation**
  - Horizontal
  - Vertical
  - Hybrid

---

## 7. Big Data Systems ⭐

### Why Big Data?
- Volume, Velocity, Variety, Veracity, Value

### Hadoop
- **HDFS**
  - NameNode
  - DataNode
  - Client

### MapReduce
- Map → Shuffle → Reduce
- Deterministic Map
- Commutative & Associative Reduce

### Spark
- In-memory processing
- **RDDs**
- Transformations vs Actions

---

## 8. Non-Relational Databases (NoSQL)

### Types
- Key-Value
- Document (MongoDB)
- Column-Oriented
- Graph

### MongoDB
- JSON documents
- Flexible schema
- Embed vs Link decision

---

## 9. Data Warehousing & BI ⭐

### Data Warehouse vs OLTP
- Historical
- Aggregated
- Read-optimized

### Dimensional Modeling
- Fact tables
- Dimension tables
- Star vs Snowflake schema

### BI Architecture
- ETL
- Data Warehouse / Data Mart
- Query & Reporting
- Visualization
- Analytics

---

## 10. Data Analysis Overview

### No Free Lunch Theorem
- No universally best algorithm

### Techniques
- Classification
- Clustering
- Regression
- Association Rules
- Time Series

### Evaluation
- Confusion Matrix
- Precision, Recall
- RMSE, R²

---

## Final Exam Strategy
- Expect **scenario-based MCQs**
- Identify:
  - Type of transaction
  - Serializability
  - Correct architecture
  - Correct mapping rule
- Pay special attention to **#review topics**

---

**End of Study Summary**
