---
title: Explain view serializability
category: Projects
priority: Medium
starred: None
created: 2025-10-23T10:28:59.258819
updated: 2025-10-23T11:43:39.289909
dg-publish: true
---
# Explain view serializability

**Priority:** Medium

## Conversation

### Assistant

Here’s a **concise Markdown note** answering all five questions clearly — perfect for your Obsidian vault 👇  

---

```markdown
# 📘 Parallel and Distributed Database Systems — Self Assessment

---

### 1. Key Differences: Parallel DBMS vs Distributed DBMS
| Aspect | Parallel DBMS | Distributed DBMS |
|--------|----------------|------------------|
| **Architecture** | Multiple CPUs within the same system | Multiple systems connected over a network |
| **Data Distribution** | Data shared across local disks/processors | Data stored at geographically separate sites |
| **Goal** | Speed and efficiency for single large tasks | Data sharing and autonomy across locations |

---

### 2. Architectures of Parallel DBMS
| Type | Description | Scalability |
|------|--------------|-------------|
| **Shared Memory** | All processors share main memory and disks | Low scalability (bottlenecks) |
| **Shared Disk** | Each processor has its own memory but shared disk | Moderate scalability |
| **Shared Nothing** | Each processor has its own memory and disk | ✅ Best scalability — no contention, easy to expand |

---

### 3. Shared-Nothing Architecture
**Advantages:**
- High scalability  
- No resource contention  
- Fault isolation (failure in one node doesn’t affect others)

**Disadvantages:**
- Complex coordination and communication between nodes  
- Data redistribution overhead for queries involving multiple nodes  

---

### 4. Homogeneous vs Heterogeneous DDBMS
| Type | Description | Data Integration |
|------|--------------|------------------|
| **Homogeneous** | All sites use the same DBMS software | Easy — common schema and query language |
| **Heterogeneous** | Different DBMS software and data models | Harder — requires translation and integration layers |

---

### 5. Transparency Features in DDBMS
| Feature | Meaning | Why Important |
|----------|----------|----------------|
| **Location Transparency** | Users don’t need to know where data is stored | Simplifies access |
| **Replication Transparency** | System manages data copies automatically | Reliability & performance |
| **Fragmentation Transparency** | Data pieces appear as one logical unit | Easier queries |
| **Concurrency Transparency** | Multiple users can access data safely | Maintains consistency |
| **Failure Transparency** | System recovers from failures | Ensures continuous operation |

---

**Summary:**  
Parallel DBMS = faster performance using multiple CPUs.  
Distributed DBMS = data spread across sites for autonomy and sharing.
```

---

Would you like me to add a small **visual summary diagram** (like a 2x2 comparison chart) for Parallel vs Distributed DBMS to go with this note?

---

