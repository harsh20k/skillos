---
title: Delete commit from main
category: Academic
priority: Medium
starred: None
created: 2025-10-24T16:35:06.470870
updated: 2025-10-24T17:39:30.245476
dg-publish: true
---
# Delete commit from main

**Priority:** Medium

## Conversation

### Assistant

If you omit `SERIAL`, PostgreSQL won’t auto-generate values for that column.  
You’ll need to insert them manually or define another sequence.  

Example without `SERIAL`:
```sql
CREATE TABLE users (
  user_id INT PRIMARY KEY,
  full_name VARCHAR
);
```
Then you must supply the ID yourself:
```sql
INSERT INTO users (user_id, full_name) VALUES (1, 'Harsh');
```

With `SERIAL`:
```sql
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  full_name VARCHAR
);
```
PostgreSQL auto-increments `user_id`:
```sql
INSERT INTO users (full_name) VALUES ('Harsh');
```

Summary:  
- `SERIAL` = integer + auto-increment sequence.  
- Without it, IDs don’t auto-increment.

---

