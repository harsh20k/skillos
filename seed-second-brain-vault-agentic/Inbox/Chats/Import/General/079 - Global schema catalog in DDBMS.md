---
title: Global schema catalog in DDBMS
category: General
priority: Medium
starred: None
created: 2025-10-28T13:51:03.047653
updated: 2025-10-28T14:08:50.281982
dg-publish: true
---
# Global schema catalog in DDBMS

**Priority:** Medium

## Conversation

### Assistant

The correct answer is:  

✅ **Push replication ensures immediate synchronization, while pull replication allows updates on demand.**

### Explanation:
- **Push replication:** The source node (master) automatically *pushes* updates to replicas as soon as changes occur.  
  → Ensures near real-time synchronization.  
  → Higher network overhead.

- **Pull replication:** The replica nodes *pull* updates from the master when they choose (periodically or on request).  
  → Updates happen on demand.  
  → Less overhead, but data may be slightly outdated.

So the key difference lies in **who initiates the synchronization**:
- Push = source-initiated.  
- Pull = destination-initiated.

---

