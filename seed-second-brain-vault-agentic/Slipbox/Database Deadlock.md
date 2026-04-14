---
creation date: 2024-12-17 18:53
modification date: Tuesday 17th December 2024 18:53:01
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/databaseconcepts
  - slipbox/permaNotes/OS
description:
dg-publish: true
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# What are Database Deadlocks?

A **database [[Deadlock]]** occurs when two or more database transactions hold locks on certain resources and wait for each other to release locks, creating a **circular dependency**. As a result, the transactions cannot proceed, and the system reaches a state of indefinite waiting.

---

## How Database Deadlocks Occur

1. **Transaction A** locks Resource 1 and waits for Resource 2.
2. **Transaction B** locks Resource 2 and waits for Resource 1.
3. Both transactions are now waiting on each other to release the resources, causing a **[[Deadlock]]**.

---

## Example of Database Deadlock

### Scenario:
Two transactions trying to update the same set of resources in reverse order:

| **Transaction A**       | **Transaction B**       |
|-------------------------|-------------------------|
| Locks `Row 1`           | Locks `Row 2`           |
| Waits for `Row 2`       | Waits for `Row 1`       |

### Outcome:
Both transactions are stuck in a **deadlock** because each is waiting for a resource locked by the other.

---

## Deadlock Detection and Resolution

1. **Deadlock Detection**:
   - Most modern databases (e.g., MySQL, [[SQL]] Server, Oracle) use algorithms to detect deadlocks.
   - When detected, the database chooses one transaction as a **victim**, rolls it back, and releases its locks.

2. **Deadlock Resolution**:
   - After choosing the victim transaction, the locks are released, allowing other transactions to proceed.

---

## How to Prevent Database Deadlocks?

1. **Acquire Locks in a Consistent Order**:
	- Ensure that all transactions acquire locks on resources in the **same sequence**.

2. **Minimize Transaction Time**:
	- Keep transactions **short and fast** to reduce the chance of deadlocks.

3. **Use Lock Timeouts**:
	- Set a **timeout** for acquiring locks to avoid indefinite waiting.

### Example in [[SQL]] Server:
   ```sql
   SET LOCK_TIMEOUT 5000; -- Timeout in milliseconds
   ```

4.	**Avoid Exclusive Locks:**
	- Use row-level locks or optimistic concurrency when possible, instead of locking entire tables.
5.	**Break Large Transactions:**
	- Split long-running transactions into smaller transactions to minimize lock contention.
6.	**Deadlock Retry Logic:**
	- Implement retry mechanisms for transactions that are rolled back due to deadlocks.

Example in [[SQL]]

```sql
Transaction 1:

BEGIN TRANSACTION;
UPDATE table1 SET column1 = 'A' WHERE id = 1;
UPDATE table2 SET column2 = 'B' WHERE id = 2;
COMMIT;

Transaction 2:

BEGIN TRANSACTION;
UPDATE table2 SET column2 = 'C' WHERE id = 2;
UPDATE table1 SET column1 = 'D' WHERE id = 1;
COMMIT;
```

- Issue:
- Transaction 1 locks table1 → waits for table2.
- Transaction 2 locks table2 → waits for table1.
- Result: Deadlock occurs.

# Summary

A database deadlock occurs when two or more transactions are waiting on each other’s locked resources, leading to circular dependency and indefinite waiting. Deadlocks can be prevented or resolved through:
- Acquiring locks in a consistent order.
- Keeping transactions short.
- Setting lock timeouts.
- Using deadlock detection and retry logic.

Proper design and careful management of transactions can significantly reduce the chances of database deadlocks.


---
# Related Topics
### [[Deadlock]]
### [[Database design]]

