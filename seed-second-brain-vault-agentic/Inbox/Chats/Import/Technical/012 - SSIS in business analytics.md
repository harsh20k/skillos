---
title: SSIS in business analytics
category: Technical
priority: Medium
starred: None
created: 2025-11-20T19:16:35.020318
updated: 2025-11-20T19:20:41.587260
dg-publish: true
---
# SSIS in business analytics

**Priority:** Medium

## Conversation

### Assistant

**BigQuery is *not* a traditional relational database, but it *is* relational in how you query it.**

Here’s the clean breakdown:

### **1. Not a traditional relational database (like MySQL/Postgres)**
- It does **not** enforce primary keys, foreign keys, indexing, transactions, constraints, etc.  
- It is **not** meant for OLTP (apps with real-time inserts/updates/deletes).

### **2. But it *is* a relational *analytical* database**
- It stores data in **tables, columns, and rows** → relational structure.  
- It uses **SQL** for querying.  
- It supports **joins, group-bys, aggregations**, and relational logic.

### **3. Real definition**
BigQuery is a **columnar, distributed, relational data warehouse** built for analytics and large-scale processing (OLAP).

### **4. Simple comparison**

| System | Type | Used For |
|-------|------|----------|
| MySQL / PostgreSQL | Relational (OLTP) | App databases, transactions |
| MongoDB | NoSQL | Documents, flexible schema |
| BigQuery | Relational (OLAP) | Analytics on large datasets |
| Snowflake | Relational (OLAP) | Same category as BigQuery |

### **Bottom line**
**BigQuery = Relational OLAP data warehouse, not NoSQL and not a typical relational OLTP database.**

---

