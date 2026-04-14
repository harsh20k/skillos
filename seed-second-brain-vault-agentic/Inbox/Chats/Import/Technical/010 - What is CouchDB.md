---
title: What is CouchDB
category: Technical
priority: Medium
starred: None
created: 2025-11-24T11:52:19.043064
updated: 2025-11-24T11:52:36.980047
dg-publish: true
---
# What is CouchDB

**Priority:** Medium

## Conversation

### Assistant

CouchDB is a **NoSQL, document-oriented database** designed around the idea of storing data as **JSON documents**, accessed via a **RESTful HTTP API**.

### Key points  
**1. Document database (JSON-based)**  
Data is stored as independent JSON documents rather than rows and tables.

**2. Uses MVCC (Multi-Version Concurrency Control)**  
Every update creates a new version of the document. This gives:
- No locking  
- Safe concurrent writes  

**3. REST/HTTP interface**  
You interact with CouchDB using standard HTTP verbs:
- `GET /db/doc`
- `PUT /db/doc`
- `POST /db`
- `DELETE /db/doc`

**4. Built-in replication**  
CouchDB is known for its **easy, robust replication**:
- Master–master replication supported  
- Offline-first sync (great for mobile apps)  
- Used in PouchDB (browser/mobile) to sync with the server

**5. Map-Reduce views**  
Instead of SQL queries, it uses map/reduce functions (JavaScript) to create indexed views.

**6. Fault-tolerant**  
CouchDB focuses on full durability, crash-safety, and staying available even during network failures.

### Where it’s used  
- Offline-first apps  
- Mobile/web apps needing sync  
- Distributed systems  
- Logging, sessions, simple data stores  
- Projects using PouchDB + CouchDB sync

### Not to confuse with  
- **Couchbase** → same origin, but now completely different product (high-performance KV + document DB).

If you want, I can explain CouchDB vs MongoDB or CouchDB vs PostgreSQL.

---

