---
creation date: 2024-12-16 10:41
modification date: Monday 16th December 2024 10:41:07
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
# Pillars of Database Design

The design of a database is guided by foundational principles that ensure the system is efficient, scalable, and reliable. These pillars form the backbone of effective database architecture.

---

## **1. Data Integrity**
- Ensures the **accuracy, consistency, and reliability** of data.  
- Types of data integrity include:
  - **Entity Integrity**: Ensures unique identification of records (e.g., Primary Key).  
  - **Referential Integrity**: Maintains valid relationships between tables (e.g., Foreign Key).  
  - **Domain Integrity**: Ensures data falls within predefined rules (e.g., data type, constraints).  

---

## **2. Data Normalization**
- Aims to reduce **data redundancy** and eliminate **anomalies** by organizing data into related tables.
- Involves breaking data into multiple tables and defining relationships:
  - **First Normal Form (1NF)**: Eliminate repeating groups.
  - **Second Normal Form (2NF)**: Eliminate partial dependencies.
  - **Third Normal Form (3NF)**: Eliminate transitive dependencies.

---

## **3. Scalability and Performance**
- Ensures the database can handle increasing data volumes and user requests efficiently.  
- Strategies include:
  - **Indexing**: Speeds up query performance.  
  - **Partitioning**: Splits large tables into smaller segments for faster access.  
  - **Denormalization**: Improves read-heavy operations by reducing joins.

---

## **4. Security**
- Protects data from unauthorized access or corruption.  
- Techniques include:
  - **Authentication and Authorization**: User roles and permissions.  
  - **Data Encryption**: Secures sensitive information.  
  - **Auditing and Logging**: Tracks changes and access attempts.

---

## **5. Usability and Flexibility**
- The database should be easy to use and adaptable to changes in requirements.  
- Best practices:
  - Design for **future requirements** by anticipating potential changes.
  - Use **clear naming conventions** for tables and columns.
  - Ensure **efficient relationships** between entities for usability.

---

## **6. Backup and Recovery**
- Protects against data loss by ensuring:
  - Regular **backups** of the database.  
  - **Recovery plans** for restoring data after failures.

---

## **7. Consistency**
- Maintains the database's state so that all users see the same data at any given time.
- Implemented using:
  - **[[ACID]] Properties** (Atomicity, Consistency, Isolation, Durability).  

---

## **8. Query Optimization**
- Focuses on ensuring efficient data retrieval.
- Techniques:
  - **Optimized [[SQL]] queries**.
  - **Proper indexing** of frequently queried columns.
  - **Avoiding unnecessary joins and subqueries**.

---

## **Conclusion**
A well-designed database balances **integrity**, **performance**, **scalability**, and **security** to meet both current and future needs effectively. These pillars form the foundation for reliable and robust database systems.

# Related Topics

## [[ACID]]