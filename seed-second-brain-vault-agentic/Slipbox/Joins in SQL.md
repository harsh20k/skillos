---
creation date: 2024-12-16 11:59
modification date: Monday 16th December 2024 11:59:49
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
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
# Joins in [[SQL]]

**Joins** in [[SQL]] are used to combine rows from two or more tables based on a related column.

---

## Types of Joins

### 1. **INNER JOIN**
- Returns rows where there is a **match** in both tables.
- Excludes rows without matches.

**Syntax**:

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```
**Example**:
Fetch employees and their department names:

```sql
SELECT employees.name, departments.name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;
```

---

### 2. **LEFT JOIN** (LEFT OUTER JOIN)
- Returns all rows from the **left table** and matching rows from the right table.
- Rows in the left table without matches show `NULL` for right table columns.

**Syntax**:

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

**Example**:
Fetch all employees, even if they don't belong to a department:

```sql
SELECT employees.name, departments.name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.id;
```

---

### 3. **RIGHT JOIN** (RIGHT OUTER JOIN)
- Returns all rows from the **right table** and matching rows from the left table.
- Rows in the right table without matches show `NULL` for left table columns.

**Syntax**:

```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

**Example**:
Fetch all departments, even if they have no employees:

```sql
SELECT employees.name, departments.name
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.id;
```

---

### 4. **FULL JOIN** (FULL OUTER JOIN)
- Returns all rows where there is a match in either table.
- Rows without matches show `NULL` for columns of the table without a match.

**Syntax**:

```sql
SELECT columns
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```

**Example**:
Fetch all employees and departments, showing `NULL` where no match exists:

```sql
SELECT employees.name, departments.name
FROM employees
FULL JOIN departments
ON employees.department_id = departments.id;
```
---

### 5. **CROSS JOIN**
- Produces the **Cartesian product** of two tables (all possible combinations of rows).

**Syntax**:

```sql
SELECT columns
FROM table1
CROSS JOIN table2;
```

**Example**:
Combine all employees with all departments:

SELECT employees.name, departments.name
FROM employees
CROSS JOIN departments;

---

## Comparison Table

| **Join Type**   | **Description**                                    | **Output**                               |
|------------------|----------------------------------------------------|------------------------------------------|
| **INNER JOIN**   | Only matching rows in both tables.                | Matched rows only.                       |
| **LEFT JOIN**    | All rows from the left table, matched rows from right. | Left rows + matches.                     |
| **RIGHT JOIN**   | All rows from the right table, matched rows from left. | Right rows + matches.                    |
| **FULL JOIN**    | All rows from both tables, with `NULL` for non-matches. | All rows with `NULL` for non-matches.    |
| **CROSS JOIN**   | Cartesian product of both tables.                 | All possible combinations.               |

---

## Summary
- **Joins** combine data from multiple tables based on relationships.
- Use **INNER JOIN** for matches, **LEFT/RIGHT JOIN** to include unmatched rows, and **FULL JOIN** for all rows.
- **CROSS JOIN** generates combinations, typically used with caution.


---
# Related Topics
### [[Query complexity]]
### [[SQL]]

