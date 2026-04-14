---
title: Database setup locally
category: Technical
priority: Medium
starred: None
created: 2025-11-09T14:21:01.969276
updated: 2025-11-19T07:50:55.989919
dg-publish: true
---
# Database setup locally

**Priority:** Medium

## Conversation

### Assistant

To fetch **all valid flight numbers** along with their **associated ticket numbers**, use an inner join between `flights` and `tickets`:

### **Valid flight numbers with their ticket numbers**
```sql
SELECT
    f.flight_number,
    t.ticket_number,
    t.passenger_name
FROM flights f
JOIN tickets t
    ON f.flight_id = t.flight_id
ORDER BY f.flight_number, t.ticket_number;
```

### What this returns
- Only flights that **have at least one ticket**  
- Each row = one flight number + one ticket number  

### If you want flights even when no tickets exist (null tickets):
```sql
SELECT
    f.flight_number,
    t.ticket_number,
    t.passenger_name
FROM flights f
LEFT JOIN tickets t
    ON f.flight_id = t.flight_id
ORDER BY f.flight_number;
```

---

