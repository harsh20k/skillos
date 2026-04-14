---
title: Database migration explained
category: Technical
priority: Medium
starred: None
created: 2025-12-19T10:57:09.453091
updated: 2025-12-19T10:57:58.156175
dg-publish: true
---
# Database migration explained

**Priority:** Medium

## Conversation

### Assistant

Yes.

Adding a column to a table **is a database migration**.

Specifically:
- It is a **schema migration** (a change to the database structure).
- It is typically recorded as a **versioned migration step** (e.g., `ADD COLUMN`).

Example:
```sql
ALTER TABLE users ADD COLUMN last_login TIMESTAMP;
```

This change would be applied through a migration so it can be:
- Tracked
- Reproduced across environments (dev, test, prod)
- Rolled back if needed

In short: **any structural change to the database = database (schema) migration**.

---

