---
title: Concise answers summary
category: General
priority: Medium
starred: None
created: 2025-10-02T14:01:07.023058
updated: 2025-10-02T14:08:45.861200
dg-publish: true
---
# Concise answers summary

**Priority:** Medium

## Conversation

### Assistant

Here are concise answers to the **Content Self-Assessment** from your screenshot:  

---

**1. Entity relationships (1:1, 1:N, M:N) and design decisions**  
- **1:1** → Rare, used for splitting sensitive/optional data.  
- **1:N** → Most common, e.g., one customer → many orders.  
- **M:N** → Needs a junction/bridge table to avoid redundancy.  
👉 Choice affects normalization, query complexity, and performance.  

---

**2. Example with fan trap / chasm trap**  
- **Entities:** Department, Manager, Project.  
- **Attributes:** Dept_ID, Dept_Name, Mgr_ID, Proj_ID, Proj_Budget.  
- **Fan trap:** A manager oversees multiple departments but relationship is unclear.  
- **Chasm trap:** Department linked to projects only via optional manager, leaving gaps.  
- **Resolution:** Add proper direct relationships or associative entities to clarify links.  

---

**3. Time-variant data & temporal modeling**  
- **Helps:** Tracks history (e.g., salary changes, inventory levels) for analysis and auditing.  
- **Modeling:** Add time attributes (start_date, end_date, timestamp) or maintain history tables (slowly changing dimensions).  

---

**4. Conceptual design phase impact**  
- Ensures database aligns with **business requirements** before implementation.  
- Aids in avoiding redundancy, anomalies, and missing relationships.  
- Good conceptual models → smoother logical/physical design and better long-term scalability.  

---

**5. Alternative way to store time-series in RDBMS**  
- **Method:** Use specialized time-series schema (e.g., partitioned tables, JSON columns, array types) or separate fact table with timestamps.  
- **Impact:** May reduce strict normalization but improves query performance for sequential data while still leveraging ACID properties.  

---

Would you like me to also create **short “exam-ready” 2–3 line answers** for these (so you can write directly in tests)?

---

