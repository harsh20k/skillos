---
title: Code typo fix
category: Technical
priority: Medium
starred: None
created: 2025-10-10T10:40:55.777185
updated: 2025-10-12T08:16:59.961664
dg-publish: true
---
# Code typo fix

**Priority:** Medium

## Conversation

### Assistant

Excellent — this is the **Foreign Key constraint configuration window** in **pgModeler** (used when linking two tables).  
Let’s break down exactly what each option in that screenshot means 👇  

---

## 🧱 1. **Name**
This is simply the **name of your foreign key constraint**.  
You can name it anything, but by convention:

```text
<referencing_table>_<referenced_column>_fk
```

For example:
```text
product_categoryid_fk
```

✅ *Tip:* Avoid spaces like in `Categoryid _fk`; it should be `categoryid_fk`.

---

## 🔗 2. **Type**
This defines what kind of constraint it is.  
Here it’s set to **FOREIGN KEY**, which means it enforces a relationship between two tables.

A **foreign key** ensures that the value in one table’s column must already exist in another table’s **primary key** column.

Example:
```sql
FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
```

---

## 🧩 3. **Match**
This determines how PostgreSQL validates multi-column foreign keys (rare in simple models).

| Option | Meaning |
|---------|----------|
| **MATCH SIMPLE** | Default. Each column is checked independently. |
| **MATCH FULL** | All columns must match or all must be null. |
| **MATCH PARTIAL** | (Not supported in PostgreSQL). |

✅ In your case, leave it as **MATCH SIMPLE**.

---

## ⏳ 4. **Options → Deferrable**
If checked, it allows the foreign key constraint to be temporarily deferred — i.e., PostgreSQL won’t enforce it immediately during a transaction.

| Option | Meaning |
|---------|----------|
| **Deferrable unchecked** | FK checked immediately after each statement. |
| **Deferrable checked** | You can delay checking until the end of the transaction (`DEFERRABLE INITIALLY DEFERRED`). |

✅ Usually **unchecked** (default).  
But if you do complex inserts (like circular dependencies), you can check it.

---

## 🕒 5. **Deferral**
This becomes active only when “Deferrable” is checked.  
You can choose:
- **INITIALLY IMMEDIATE** → constraint checked immediately (default)
- **INITIALLY DEFERRED** → checked at end of transaction

---

## 🔄 6. **ON DELETE / ON UPDATE**
Defines **what happens when the referenced record is deleted or updated** in the parent table.

| Option | Behavior |
|---------|-----------|
| **NO ACTION** | Prevents delete/update if child exists. (default) |
| **CASCADE** | Automatically deletes/updates child records. |
| **SET NULL** | Sets the FK field to NULL in child records. |
| **SET DEFAULT** | Sets FK to a default value. |
| **RESTRICT** | Similar to NO ACTION, but checked immediately. |

✅ Typical use cases:
- `ON DELETE CASCADE` (for child tables like cart_items)
- `ON UPDATE NO ACTION`

---

## 🧩 7. **Columns / Referenced Columns Tabs**
These two tabs let you define **which columns** in your table and **which columns in the referenced table** are connected.

For example:
| Tab | Meaning |
|-----|----------|
| **Columns** | Column(s) in the current table (e.g., `ProductID`) |
| **Referenced Columns** | Column(s) in the target table (e.g., `ProductID` in `Products`) |

You must make sure both columns have the same data type (e.g., `bigint → bigint`).

---

## 🪄 Example Configuration Summary

If you were linking `Products` → `Categories`, a typical FK setup would be:

| Setting | Value |
|----------|--------|
| **Name** | categoryid_fk |
| **Type** | FOREIGN KEY |
| **Match** | MATCH SIMPLE |
| **Deferrable** | ❌ |
| **ON DELETE** | SET NULL (optional) |
| **ON UPDATE** | CASCADE |
| **Columns** | CategoryID |
| **Referenced Columns** | CategoryID (from Categories table) |

---

✅ **In summary:**

| Section | Purpose |
|----------|----------|
| **Name** | Label for the FK constraint |
| **Type** | Always “FOREIGN KEY” |
| **Match** | Column-matching rule |
| **Deferrable/Deferral** | When FK checks occur |
| **ON DELETE / ON UPDATE** | What happens to child rows on parent change |
| **Columns Tabs** | Link child & parent table columns |

---

Would you like me to give you **the best recommended configuration** (with example values) for a typical `Product → Category` relationship in pgModeler?

---

