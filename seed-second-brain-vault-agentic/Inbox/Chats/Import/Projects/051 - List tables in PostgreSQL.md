---
title: List tables in PostgreSQL
category: Projects
priority: Medium
starred: None
created: 2025-10-03T10:13:12.148364
updated: 2025-10-03T15:32:37.640562
dg-publish: true
---
# List tables in PostgreSQL

**Priority:** Medium

## Conversation

### Assistant

Yes 👍 you can list all **column names** for all tables in your PostgreSQL `imdb` database using the system catalog views.  

Here are a few handy ways:

---

### 1. Using `information_schema.columns` (most common)
```sql
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
ORDER BY table_name, ordinal_position;
```

👉 This will show **table name, column name, and column type** for every table in the `public` schema (which is where your IMDb tables likely are).  

---

### 2. Using `\d` in `psql` (manual, one table at a time)
Inside the `psql` shell:
```sql
\d actors
```
👉 Shows all columns for `actors`.  
If you want **all tables**:
```sql
\dt
```
Then pick a table and run `\d table_name`.

---

### 3. For all tables in one shot (PostgreSQL catalog query)
```sql
SELECT c.table_name, c.column_name, c.data_type
FROM information_schema.columns c
JOIN information_schema.tables t
  ON c.table_name = t.table_name
WHERE t.table_type = 'BASE TABLE'
  AND c.table_schema = 'public'
ORDER BY c.table_name, c.ordinal_position;
```

---

⚡Tip: If you want to see **just the list of columns per table grouped together**, you can aggregate them:
```sql
SELECT table_name,
       string_agg(column_name, ', ' ORDER BY ordinal_position) AS columns
FROM information_schema.columns
WHERE table_schema = 'public'
GROUP BY table_name
ORDER BY table_name;
```

👉 This will give you something like:
```
actors   | id, first_name, last_name, birth_year
movies   | id, title, year
roles    | actor_id, movie_id, role
...
```

---

Do you want me to write a query that **lists only the IMDb-style tables** (`actors`, `movies`, `roles`, etc.) with their columns formatted neatly so you can see the schema at a glance?

---

