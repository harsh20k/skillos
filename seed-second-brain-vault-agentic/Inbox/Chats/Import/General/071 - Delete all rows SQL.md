---
title: Delete all rows SQL
category: General
priority: Medium
starred: None
created: 2025-11-06T03:32:17.119540
updated: 2025-11-06T03:32:20.600020
dg-publish: true
---
# Delete all rows SQL

**Priority:** Medium

## Conversation

### Assistant

Use either of these:  

1. To delete all rows but keep the table structure:  
```sql
DELETE FROM table_name;
```

2. To delete all rows faster (resets identity counters too):  
```sql
TRUNCATE TABLE table_name;
```

**Difference:**  
- `DELETE` can have a `WHERE` clause and logs each row.  
- `TRUNCATE` cannot use `WHERE` and is faster but cannot be rolled back in some databases without a transaction.

---

