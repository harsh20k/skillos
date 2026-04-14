---
title: HoL Blocking TCP vs UDP
category: Projects
priority: Medium
starred: None
created: 2025-12-23T10:18:45.899911
updated: 2025-12-23T10:19:05.577523
dg-publish: true
---
# HoL Blocking TCP vs UDP

**Priority:** Medium

## Conversation

### Assistant

## Head-of-Line (HoL) Blocking — TCP vs UDP

### What it is
**Head-of-line blocking** occurs when a delay or loss of an earlier packet prevents later packets from being delivered to the application, even if those later packets have already arrived.

---

## TCP (Transmission Control Protocol)

image_group{"query":["TCP head of line blocking diagram","TCP ordered delivery packet loss diagram","TCP retransmission blocking illustration"]}

**Behavior**
- TCP guarantees **reliable, ordered delivery**.
- If packet *N* is lost, packets *N+1, N+2…* are **held back** until *N* is retransmitted and received.

**Result**
- HoL blocking **does occur**.
- A single lost packet stalls the byte stream.

**Implications**
- Higher latency during loss.
- Can hurt real-time apps (audio/video, live updates) even if only one segment drops.

---

## UDP (User Datagram Protocol)

image_group{"query":["UDP packet delivery diagram","UDP no head of line blocking illustration","UDP out of order packets diagram"]}

**Behavior**
- UDP is **connectionless** and **unordered**.
- Each datagram is delivered independently.
- If a packet is lost, later packets are still delivered immediately.

**Result**
- HoL blocking **does not occur at the protocol level**.

**Implications**
- Lower latency.
- Packet loss is visible to the application, which must handle it (or ignore it).

---

## Key Comparison

| Aspect | TCP | UDP |
|---|---|---|
| Ordered delivery | Yes | No |
| Retransmissions | Yes | No |
| HoL blocking | Yes | No |
| Latency under loss | Higher | Lower |
| App responsibility | Minimal | High |

---

## Important nuance
HoL blocking is **not exclusive to TCP**. It can also appear:
- **At the application layer** (e.g., custom protocols built on UDP).
- **Within multiplexed streams** if a single stream enforces ordering (historically HTTP/1.1 over TCP).

Modern designs mitigate this by:
- Using UDP with smarter protocols (e.g., independent streams, selective reliability).
- Avoiding global ordering where it is unnecessary.

---

### One-line summary
- **TCP:** Reliable and ordered → **Head-of-line blocking exists**.  
- **UDP:** Unordered and unreliable → **No head-of-line blocking at the transport layer**.

---

