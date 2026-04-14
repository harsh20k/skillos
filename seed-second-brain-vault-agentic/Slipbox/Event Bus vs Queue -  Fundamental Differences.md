---
creation date: 2026-03-16 18:44
tags: [concept]
---
### **Queue** (e.g., SQS, RabbitMQ)
**Model**: Point-to-point, single consumer

- **One message → One consumer**: Each message is processed by exactly one consumer
- **Consumption removes message**: Once read, the message is gone (or moved to dead-letter queue)
- **Use case**: Task distribution, work queues, job processing
- **Pattern**: Producer → Queue → Consumer (1:1)
- **Example**: Upload queue where each image needs to be processed once by a worker

```
Producer → [Queue] → Consumer A (gets msg 1)
                  → Consumer B (gets msg 2)
                  → Consumer C (gets msg 3)
```

---

### **Event Bus** (e.g., EventBridge, Kinesis, SNS, Kafka)
**Model**: Pub/Sub, multiple consumers

- **One event → Many consumers**: Each event can be processed by multiple subscribers independently
- **Event persistence**: Events remain available for replay (especially in streams like Kinesis/Kafka)
- **Use case**: Event-driven architectures, fan-out patterns, real-time analytics
- **Pattern**: Publisher → Event Bus → Subscriber 1, Subscriber 2, Subscriber 3... (1:N)
- **Example**: Order placed event that triggers inventory update, email notification, analytics logging, and recommendation engine

```
Producer → [Event Bus] → Consumer A (all msgs)
                      → Consumer B (all msgs)
                      → Consumer C (filtered msgs)
```

---

### Key Differences Table

| Aspect | Queue | Event Bus |
|--------|-------|-----------|
| **Consumers** | Single (competing consumers) | Multiple (independent subscribers) |
| **Message lifecycle** | Deleted after processing | Retained (for replay/audit) |
| **Delivery** | One consumer per message | Broadcast to all subscribers |
| **Filtering** | No (consumer gets all) | Yes (topic/pattern filtering) |
| **Ordering** | FIFO available | Typically ordered by partition/shard |
| **Decoupling** | Producer knows queue exists | Producer doesn't know subscribers |

---

### In Your GroundSense Context

**Why Kinesis is better as an Event Bus here:**
- **Seismic events** need to go to 3+ consumers: DynamoDB writer, S3 archiver, Alert checker, potentially analytics
- **Document uploads** need to trigger: S3 storage, Bedrock KB sync, maybe audit logging
- **Replay capability**: If Bedrock KB sync fails, you can replay document events
- **Audit trail**: All system events in one place for debugging

**If you used SQS instead:**
- Each message goes to one consumer only
- Would need multiple queues (one per consumer) with SNS fan-out
- No replay capability
- More complex architecture

The unified Kinesis stream gives you the event bus pattern: one stream, multiple independent consumers processing the same events for different purposes.