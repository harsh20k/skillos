---
title: ER diagram suggestion
category: Projects
priority: Medium
starred: None
created: 2025-10-04T14:20:33.992283
updated: 2025-10-05T15:19:37.825101
dg-publish: true
---
# ER diagram suggestion

**Priority:** Medium

## Conversation

### Assistant

That’s **really close!** 👏  
You’re 95% there — you just need a **tiny syntax adjustment** to make it valid SQL.  

Let’s walk through it carefully 👇  

---

### 🔍 Your intention
You’re saying:
> “Find movie names where the movie ID appears in the list of top 2 movies that have the most doctor roles.”

That’s absolutely correct logic ✅

---

### ⚠️ What’s slightly off
Inside a subquery, you can’t use both `GROUP BY` and `ORDER BY` unless you wrap it properly (because PostgreSQL expects the subquery to return only the column(s) being selected).

So you just need to make your subquery **return the movie_id** cleanly *after aggregation*.  

---

### ✅ Correct version
```sql
SELECT name
FROM movies
WHERE id IN (
    SELECT movie_id
    FROM roles
    WHERE role ILIKE '%doctor%'
       OR role ILIKE 'dr.%'
    GROUP BY movie_id
    ORDER BY COUNT(*) DESC
    LIMIT 2
);
```

This works perfectly in **PostgreSQL** 💪

---

### 🧠 Optional improvement (regex-based, safer from “Director”)
If you want to avoid catching “Director” in the data:
```sql
SELECT name
FROM movies
WHERE id IN (
    SELECT movie_id
    FROM roles
    WHERE role ~* '\b(dr\.?|doctor)\b'
    GROUP BY movie_id
    ORDER BY COUNT(*) DESC
    LIMIT 2
);
```

---

### 💬 Summary
✅ Logic — correct  
✅ Structure — correct  
⚠️ Just ensure parentheses and GROUP BY syntax are proper  

Your query will now return **the top 2 movies that have the most doctor roles**, listed by `name`.  

---

Would you like me to show how to **also display the doctor count next to each movie name** (so you see which one had more)?

---

