---
creation date: 2024-12-16 10:42
modification date: Monday 16th December 2024 10:42:28
tags:
  - slipbox/permaNotes/DalhousieInterview
  - "#slipbox/permaNotes/databaseconcepts"
description: Atomicity, Consistency, Isolation and Durability
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
# ACID in Database Design

## **What is ACID?**
ACID stands for **Atomicity, Consistency, Isolation, and Durability**. These are a set of properties that ensure reliable processing of database transactions. ACID ensures that the database remains in a valid state, even in the event of power outages, crashes, or other unexpected failures.

---

## **ACID Properties Explained**

### 1. **Atomicity**
- **Definition**: A transaction is an **all-or-nothing** operation. Either all the changes made during a transaction are committed, or none of them are.  
- **Example**:  
  - Suppose you're transferring money from **Account A** to **Account B**. The transaction involves two operations:
    1. Subtracting the amount from **Account A**.
    2. Adding the amount to **Account B**.
  - If the system crashes after subtracting from **Account A** but before adding to **Account B**, **Atomicity** ensures that the transaction is rolled back and no partial data is committed.

### 2. **Consistency**
- **Definition**: A transaction takes the database from one **valid state** to another valid state. It ensures that data integrity constraints (such as **primary keys**, **foreign keys**, and **check constraints**) are always respected.
- **Example**:  
  - If you have a table of employees, and a transaction attempts to insert an employee with a duplicate **EmployeeID**, it will violate the **primary key** constraint. If the transaction fails, the database is left in a consistent state, and no invalid data is saved.

### 3. **Isolation**
- **Definition**: Ensures that the operations of one transaction are isolated from the operations of other transactions, meaning no transaction can interfere with another. Transactions should behave as if they are executed sequentially, even if they are actually processed concurrently.
- **Example**:  
  - If two users try to withdraw money from the same account at the same time, **Isolation** ensures that each transaction sees a consistent state of the database. If one user is withdrawing money, the other user cannot see the updated balance until the first transaction is complete.

### 4. **Durability**
- **Definition**: Once a transaction has been committed, its effects are permanent, even in the event of a system crash or power failure. The data changes are saved to disk and will not be lost.
- **Example**:  
  - After transferring money from **Account A** to **Account B**, if the system crashes immediately after the transaction is committed, **Durability** ensures that the transaction is not lost. When the system is back online, the changes to both accounts will still be present in the database.

---

## **Why ACID is Important**
- **Reliability**: ACID properties ensure that transactions are reliable, maintaining the integrity and consistency of the database.
- **Error Handling**: If a failure occurs during a transaction, ACID ensures that the database returns to a valid state without partial updates.
- **Concurrency**: ACID ensures that multiple transactions can occur at the same time without leading to conflicts or inconsistent data.

---

## **Conclusion**
ACID properties are essential for ensuring that database transactions are processed reliably, maintaining [[Data integrity]], and preventing data corruption. They form the foundation of transaction management in database systems.