---
title: SQL comment usage
category: General
priority: Medium
starred: None
created: 2025-10-24T18:31:52.032861
updated: 2025-10-24T18:31:58.260838
dg-publish: true
---
# SQL comment usage

**Priority:** Medium

## Conversation

### Assistant

Use two kinds of SQL comments:

1. **Single-line comment:**  
   ```sql
   -- This is a single-line comment
   SELECT * FROM customers;
   ```

2. **Multi-line (block) comment:**  
   ```sql
   /* This is a
      multi-line comment */
   SELECT * FROM orders;
   ```

Anything after `--` on a line or between `/* ... */` is ignored by the SQL engine.

---

