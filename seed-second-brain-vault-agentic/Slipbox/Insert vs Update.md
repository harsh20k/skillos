---
creation date: 2024-12-18 11:42
modification date: Wednesday 18th December 2024 11:42:22
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
# INSERT vs UPDATE in SQL

## 1. **INSERT**

The `INSERT` statement is used to **add new rows** to a table.

### Syntax
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### Key Points:
- Adds new data to the table.
- Requires specifying values for the columns (or relies on defaults).
- If a primary key or unique constraint is violated, the operation will fail.

Example:

```sql
INSERT INTO employees (id, name, salary)
VALUES (1, 'Alice', 50000);
```

---
## 2. **UPDATE**

The UPDATE statement is used to modify existing rows in a table.

Syntax

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### Key Points:
- Updates existing data based on the condition in the WHERE clause.
- If the WHERE clause is omitted, all rows in the table will be updated.
- Without a condition, it can lead to unintended changes.

Example:

```sql 
UPDATE employees
SET salary = 55000
WHERE id = 1;
```

---
## Key Differences

| Aspect              | INSERT                                      | UPDATE                                   |
| ------------------- | ------------------------------------------- | ---------------------------------------- |
| Purpose             | Adds new rows to a table.                   | Modifies existing rows in a table.       |
| Operation           | Creates new records.                        | Alters existing records.                 |
| Syntax              | INSERT INTO ... VALUES (...)                | UPDATE ... SET ... WHERE ...             |
| Condition           | Not applicable.                             | Requires a WHERE clause for specificity. |
| Constraint Handling | May fail due to primary/unique constraints. | May fail due to foreign key constraints. |
|                     |                                             |                                          |

---
## When to Use

1.	**INSERT:**
	- Adding new data to a table.
	- Populating tables during initial setup or data migrations.
2.	**UPDATE:**
	- Correcting or modifying existing data.
	- Incremental changes based on business logic (e.g., updating a user’s subscription status).

---
### Example Comparison

**INSERT Example:**

```sql
INSERT INTO products (id, name, price)
VALUES (101, 'Laptop', 750);
```

	•	Adds a new product with ID 101.

**UPDATE Example:**

```sql
UPDATE products
SET price = 800
WHERE id = 101;
```

	•	Updates the price of the product with ID 101 to 800.

# Summary
- Use **INSERT** to add new rows to a table.
- Use **UPDATE** to modify existing rows in a table.
Both are essential SQL operations for managing and manipulating database records effectively.



---
# Related Topics
### [[Joins in SQL]]
### [[SQL]]


