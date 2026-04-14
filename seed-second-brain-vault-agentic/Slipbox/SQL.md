---
creation date: 2024-12-18 12:03
modification date: Wednesday 18th December 2024 12:03:36
tags:
  - slipbox/permaNotes/DalhousieInterview
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
# What is SQL?

**SQL (Structured Query Language)** is a standard programming language designed for managing and manipulating relational databases. It allows users to perform operations such as querying, inserting, updating, and deleting data, as well as managing database structures like tables and indexes.

---

## Key Features of SQL:

1. **Data Querying**:
   - Retrieve data using the `SELECT` statement.
2. **Data Manipulation**:
   - Perform `INSERT`, `UPDATE`, and `DELETE` operations.
3. **Data Definition**:
   - Create and modify database schemas using `CREATE`, `ALTER`, and `DROP`.
4. **Data Control**:
   - Manage user permissions with `GRANT` and `REVOKE`.
5. **Transaction Management**:
   - Ensure consistency using `BEGIN`, `COMMIT`, and `ROLLBACK`.

---

## Example SQL Statements:

- **Select Data**:
  ```sql
  SELECT * FROM employees WHERE department = 'Sales';
  ```

- **Insert Data**:
  ```sql
  INSERT INTO employees (id, name, department) VALUES (1, 'Alice', 'HR');
  ```

- **Update Data**:
  ```sql
  UPDATE employees SET department = 'Marketing' WHERE id = 1;
  ```

- **Delete Data**:
  ```sql
  DELETE FROM employees WHERE id = 1;
  ```

---

## Use Cases of SQL:

1. **Data Analysis**: Extract insights from large datasets.
2. **Database Management**: Organize and maintain relational data.
3. **Web and Application Development**: Backend data handling for dynamic websites and applications.

---

## Summary:

SQL is the backbone of relational database management, providing a powerful and standardized way to interact with structured data. It is widely used in fields such as data analysis, software development, and system administration.

---
# Related Topics
##

