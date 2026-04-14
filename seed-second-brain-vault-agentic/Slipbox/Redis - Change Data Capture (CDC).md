---
tags: [concept]
dg-publish: true
---
# Redis as an Event Store for CDC (Change Data Capture)

## 1. What is CDC?
**Change Data Capture (CDC)** means emitting an event whenever data changes, instead of making other services poll the database.

Example:
- A user edits a comment
- The system emits an event:
```json
{
  "event": "CommentUpdated",
  "comment_id": 123,
  "old_text": "...",
  "new_text": "...",
  "timestamp": "..."
}
```

Downstream services (search, notifications, moderation, analytics) consume this event to stay in sync.

---

## **2. Why CDC is Needed**
Without CDC:
- Services poll the database
- Changes can be missed
- State becomes inconsistent across systems
With CDC:
- Every change is captured
- Updates are propagated reliably
- Systems remain loosely coupled but consistent
---

## **3. Redis Used as an Event Store**
Redis is **not used as a cache** here.
It acts as:
- An **append-only event log**
- A **message broker with persistence**
Typically implemented using:
- **Redis Streams**
- **Append-Only File (AOF)** persistence
- **Consumer Groups**
---

## **4. What is an Event Store?**
An **event store**:
- Stores every change as an immutable event
- Events are written once and never modified
- Consumers read events in order
- Events remain until acknowledged or explicitly trimmed
This is similar to a database WAL, but exposed at the application level.
---

## **5. Guaranteed (100%) Event Delivery**
CDC events are **critical infrastructure**.
If an event is missed:
- A service may never update its state
- Features break silently (search, moderation, recommendations)
Redis Streams provide:
- Persistent storage of events
- Consumer acknowledgements
- Replay of unprocessed events after crashes
Delivery model:
- **At-least-once delivery**
- Idempotent consumers prevent duplicates
---

## **6. What Happens When a Comment Changes?**
Flow:
1. Comment is updated in the database
2. CDC event is written to Redis Stream
3. Multiple services consume the event
4. Each service updates its own state
5. Event is acknowledged after successful processing
---
## **7. Why Redis Instead of Kafka?**
Common reasons:
- Lower operational complexity
- Very low latency
- Built-in persistence (AOF)
- Consumer groups with ACKs
- Easier to run at smaller scale
Redis becomes a **lightweight Kafka-style event backbone**.
---

## **8. Failure Handling & Recovery**
- If a consumer crashes, its unacked events remain pending
- On restart, the consumer resumes from last acknowledged ID
- No events are lost
- Backpressure is handled naturally via pending lists
---

## **9. Relation to WAL & Distributed Databases**
This pattern mirrors database internals:

| **Database Concept**  | **CDC System Equivalent** |
| --------------------- | ------------------------- |
| Write-Ahead Log (WAL) | CDC Event Log             |
| Replication log       | Redis Stream              |
| Replica catch-up      | Consumer replay           |
| Durability guarantee  | AOF persistence           |
| Replica divergence    | Missed CDC event          |

---

## **10. One-Line Mental Model**
> Redis stores every data change as an immutable event, and all dependent services must consume it reliably—missing an event is not allowed.