---
creation date: 2024-12-16 10:20
modification date: Monday 16th December 2024 10:20:29
tags:
  - slipbox/permaNotes/DalhousieInterview
  - "#slipbox/permaNotes/databaseconcepts"
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
# Data Integrity

## **What is Data Integrity?**
Data integrity refers to the **accuracy, consistency, and reliability** of data stored in a database over its lifecycle. It ensures that data remains unchanged and valid unless modified intentionally through authorized means.

---

## **Types of Data Integrity**

1. **Entity Integrity**  
   - Ensures that each table has a unique and valid primary key, and no part of the primary key is null.  
   - Example: Every student in a `Students` table must have a unique `StudentID`.

2. **Referential Integrity**  
   - Ensures that foreign keys correctly reference valid primary keys in another table, maintaining relationships between tables.  
   - Example: An `Orders` table cannot reference a non-existent `ProductID` in a `Products` table.

3. **Domain Integrity**  
   - Ensures data entered in a column adheres to a defined data type, format, or range.  
   - Example: A `DateOfBirth` field should only accept valid date values.

4. **User-Defined Integrity**  
   - Enforces business-specific rules through constraints like `CHECK` or application-level validations.  
   - Example: Salary of an employee cannot be less than the minimum wage.

---

## **Why Do We Need Data Integrity?**

1. **Prevent Data Corruption**  
   - Ensures that data is stored and retrieved accurately without unintended modifications.

2. **Support Decision-Making**  
   - Reliable and consistent data enables better analytics and informed decision-making.

3. **Ensure Data Consistency**  
   - Prevents issues like duplicate records, mismatched data, or invalid references across tables.

4. **Maintain Security and Compliance**  
   - Helps meet regulatory requirements by ensuring data accuracy and validity.

5. **Improve Database Performance**  
   - Structured, consistent, and accurate data makes querying and updates more efficient.

6. **Preserve Business Reputation**  
   - Inaccurate or corrupted data can lead to errors in operations and loss of trust.

---

## **Conclusion**
Data integrity is crucial for creating reliable and trustworthy database systems. By enforcing rules and constraints, it ensures that the stored data is accurate, consistent, and meaningful, safeguarding the database's utility for users and applications.
