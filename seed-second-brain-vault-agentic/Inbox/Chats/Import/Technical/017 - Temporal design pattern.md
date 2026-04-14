---
title: Temporal design pattern
category: Technical
priority: Medium
starred: None
created: 2025-11-06T21:40:41.249872
updated: 2025-11-06T21:40:51.140650
dg-publish: true
---
# Temporal design pattern

**Priority:** Medium

## Conversation

### Assistant

Temporal design pattern in databases means designing tables to **store and query data as it changes over time** rather than only keeping the current state.  

### Core idea
Each record includes **time dimensions** (usually *valid time* and/or *transaction time*) that show **when** the data was true or stored.

### Types
1. **Valid-time tables**  
   Track *when the data is valid in the real world*.  
   Example: employee’s department assignment valid from `2022-01-01` to `2023-06-30`.

2. **Transaction-time tables**  
   Track *when the data was stored in the database*.  
   Useful for auditing or rollback.

3. **Bitemporal tables**  
   Combine both valid and transaction times.  
   Useful when you need to know “what we thought was true at a past moment.”

### Typical schema design
| employee_id | department | valid_from | valid_to | transaction_from | transaction_to |
|--------------|-------------|-------------|-----------|------------------|----------------|
| 101 | Sales | 2022-01-01 | 2023-06-30 | 2022-01-01 | 9999-12-31 |

### Benefits
- Supports **historical queries** (“what was the department on Jan 10, 2023?”).  
- Enables **auditing** and **versioning**.  
- Simplifies **slowly changing dimensions (SCD Type 2)** in data warehousing.

### Example query
```sql
SELECT *
FROM employee_department
WHERE employee_id = 101
  AND DATE '2023-03-01' BETWEEN valid_from AND valid_to;
```

In short: temporal design pattern lets the database **understand time** as part of the data model, enabling historical and point-in-time analysis.

---

