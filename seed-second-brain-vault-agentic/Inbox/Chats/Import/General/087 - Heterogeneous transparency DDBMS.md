---
title: Heterogeneous transparency DDBMS
category: General
priority: Medium
starred: None
created: 2025-10-23T13:09:17.134598
updated: 2025-10-23T14:17:14.385783
dg-publish: true
---
# Heterogeneous transparency DDBMS

**Priority:** Medium

## Conversation

### Assistant

Here’s a **Mermaid sequence diagram** for the **Three-Phase Commit (3PC)** protocol — ready to paste into Obsidian:

```mermaid
sequenceDiagram
    participant C as Coordinator
    participant P1 as Participant 1
    participant P2 as Participant 2

    Note over C,P2: **Phase 1 – CanCommit**
    C->>P1: CAN_COMMIT?
    C->>P2: CAN_COMMIT?
    P1-->>C: YES
    P2-->>C: YES

    Note over C,P2: **Phase 2 – PreCommit**
    C->>P1: PRE_COMMIT (Prepare to commit)
    C->>P2: PRE_COMMIT (Prepare to commit)
    P1-->>C: ACK
    P2-->>C: ACK

    Note over C,P2: **Phase 3 – DoCommit**
    C->>P1: DO_COMMIT
    C->>P2: DO_COMMIT
    P1-->>C: ACK (Committed)
    P2-->>C: ACK (Committed)
    C-->>C: Transaction complete ✅
```

### 🔹 Key Difference from 2PC
3PC adds the **Pre-Commit phase** to reduce blocking:
- Participants are informed to prepare but not yet commit.  
- If the coordinator fails after pre-commit, participants can still reach a consistent decision without indefinite waiting.

---

