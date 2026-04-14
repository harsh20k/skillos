---
creation date: 2024-12-18 18:37
modification date: Wednesday 18th December 2024 18:37:30
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/databaseconcepts
  - slipbox/permaNotes/sql
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
# UPDATE vs MODIFY in SQL

In SQL, **`UPDATE`** and **`MODIFY`** serve different purposes, and their usage depends on the specific operation you need to perform. Here's a detailed comparison:

---

## 1. **UPDATE**

The `UPDATE` statement is used to **modify existing data** in the rows of a table.

### Syntax

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, …
WHERE condition;
```

### Key Points
- Used to **change the values** of one or more columns in existing rows.
- Requires a `WHERE` clause to specify which rows to update.
- If no `WHERE` clause is provided, all rows in the table will be updated.

### Example

```sql
UPDATE employees
SET salary = 60000
WHERE id = 101;
```

- Updates the `salary` column of the employee with ID `101` to `60000`.

---

## 2. **MODIFY**

The `MODIFY` keyword is used to **alter the structure** of a table, specifically to change the **data type** or other properties of existing columns. It is a part of the `ALTER TABLE` command.

### Syntax

```sql
ALTER TABLE table_name
MODIFY column_name new_data_type;
```

### Key Points
- Used to **change column properties** (e.g., data type, constraints).
- Does **not alter the data** in the rows.
- Supported by certain databases like MySQL.

### Example

ALTER TABLE employees
MODIFY salary DECIMAL(10, 2);

- Changes the data type of the `salary` column to `DECIMAL(10, 2)`.

---

## Key Differences

| **Aspect**           | **UPDATE**                              | **MODIFY**                              |
|-----------------------|------------------------------------------|------------------------------------------|
| **Purpose**           | Changes the data in existing rows.      | Alters the structure of the table.       |
| **Operation**         | Works on table data (row level).         | Works on table schema (column level).    |
| **Impact on Data**    | Changes the values of columns.           | Does not change the existing data.       |
| **Syntax**            | `UPDATE ... SET ... WHERE ...`           | `ALTER TABLE ... MODIFY ...`             |
| **Use Case**          | Updating records based on conditions.    | Changing column data types or constraints. |

---

## Summary

| **Command** | **Purpose**                     | **Example Use Case**                       |
|-------------|---------------------------------|--------------------------------------------|
| **UPDATE**  | Modify data in table rows.      | Update an employee's salary.               |
| **MODIFY**  | Alter table column properties.  | Change a column's data type to `DECIMAL`.  |

---

## Conclusion

- Use **`UPDATE`** to change the **data** stored in the rows of a table.
- Use **`MODIFY`** to adjust the **structure** or **properties** of table columns.


---
# Related Topics
### [[Update vs Modify in SQL]]
### [[Joins in SQL]]
### [[Query complexity]]
### [[Database design]]

