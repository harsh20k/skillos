---
title: WAL persistence requirement
category: General
priority: Medium
starred: None
created: 2025-12-10T17:11:28.416307
updated: 2025-12-10T17:11:46.824510
dg-publish: true
---
# WAL persistence requirement

**Priority:** Medium

## Conversation

### Assistant

**Yes. In a proper Write-Ahead Log (WAL), the log is always written to *persistent storage* before the actual data pages are written.**  
That is the core rule. Otherwise, the mechanism would not guarantee durability or crash recovery.

## Why WAL must be on persistent storage
WAL ensures two guarantees:

1. **Durability**  
   After a transaction commits, its changes must survive a crash.  
   If the WAL entry is only in memory and the server crashes, all unflushed logs are lost → no recovery possible.

2. **Redo/Undo Recovery**  
   During crash recovery, the DBMS reads the WAL to redo committed transactions and undo incomplete ones.  
   This is only possible if the WAL survived on disk.

## What actually happens internally
- When you call **COMMIT**, the DBMS:
  1. Writes the log record(s) to the WAL buffer.
  2. **Forces** the WAL buffer to durable storage (`fsync` or equivalent).
  3. Acknowledges commit.
  4. Later, asynchronously writes the modified data pages to disk.

### Sequence (must always hold)
```
WAL (persistent) <- written before -> Data Pages
```

## Is the WAL *always* written to persistent storage?
**For every commit: Yes.**  
**For every individual log record: Not necessarily.**

There are two cases:

### 1. **Strict durability mode (default in databases like PostgreSQL)**
- On COMMIT, WAL is forced to disk.
- Guarantees ACID.

### 2. **Relaxed durability mode (optional)**  
(Some DBMSs allow performance optimization where durability can be sacrificed.)

Examples:
- PostgreSQL `synchronous_commit = off`
- MySQL InnoDB `innodb_flush_log_at_trx_commit = 2`

In these modes:
- WAL may sit in OS cache for a moment before being flushed.
- A crash can lose a few milliseconds of committed transactions.

But **even then** the WAL *will eventually* be written to persistent storage.  
It is never “RAM only.”

## Summary
- **True WAL = always written to persistent storage before data pages.**
- Some DBMS allow *delayed* or *batched* fsync for higher performance.
- Without persistence of WAL, crash recovery is impossible and WAL loses meaning.

If you want, I can also explain **how fsync, group commit, WAL buffers, and checkpoints** work in real DBMS implementations.

---

