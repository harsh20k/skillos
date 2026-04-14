---
title: Plain English changes
category: Technical
priority: Medium
starred: None
created: 2025-11-20T11:31:41.852026
updated: 2025-11-20T11:38:30.455945
dg-publish: true
---
# Plain English changes

**Priority:** Medium

## Conversation

### Assistant

1. **No automatic notifications**  
   Flight updates (delay, gate change, etc.) don’t trigger any notifications. Backend needs code to detect changes and send alerts.

2. **Wrong token field name**  
   Database uses **expo_token**, but it actually stores an **FCM token**. The column name should be corrected.

3. **No notification service**  
   There’s no backend function to find all subscribers of a flight and send them notifications. This function needs to be added.

4. **Firebase not loaded**  
   The Firebase setup in `__init__.py` may not be imported in `app.py`, so Firebase never initializes. This must be fixed.

---

