---
creation date: 2024-12-18 19:16
modification date: Wednesday 18th December 2024 19:16:14
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/webtech
description:
dg-publish: true
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
---
# Sliding Window Protocol

## What is the Sliding Window Protocol?

The **Sliding Window Protocol** is a method used in network communication to manage **flow control** and ensure reliable data transmission between sender and receiver. It allows multiple packets to be sent before needing an acknowledgment (ACK) for the first packet, improving efficiency and throughput.

---

## Key Concepts

### 1. **Window Size**
- Defines the maximum number of packets that can be sent without receiving an acknowledgment.
- The "window" slides forward as acknowledgments are received.

### 2. **Sender Window**
- Represents the range of packets the sender can transmit without waiting for an acknowledgment.

### 3. **Receiver Window**
- Represents the range of packets the receiver is ready to accept.

---

## Working of the Sliding Window Protocol

1. **Transmission**:
   - The sender transmits packets up to the size of the **window**.
   
2. **Acknowledgment**:
   - The receiver acknowledges the receipt of packets (cumulative ACK for all received packets).
   
3. **Sliding**:
   - Once an acknowledgment is received, the window "slides forward," allowing the sender to send the next set of packets.

---

## Modes of Sliding Window Protocol

### 1. **Stop-and-Wait Protocol**
- Simplest version: The sender sends one packet and waits for its acknowledgment before sending the next packet.
- **Inefficient** for high-latency networks.

### 2. **Go-Back-N Protocol**
- The sender can send `N` packets without waiting for an acknowledgment.
- If a packet is lost, the sender retransmits the lost packet and all subsequent packets.

### 3. **Selective Repeat Protocol**
- The sender retransmits only the lost or corrupted packets, not the entire batch.
- More efficient than Go-Back-N but requires additional complexity in implementation.

---
## Example

### Parameters:
- **Window Size**: 4 packets
- **Total Packets to Send**: 10 packets

### Transmission:
1. Sender transmits packets: `[1, 2, 3, 4]`.
2. Receiver sends acknowledgment for packets 1 and 2: `[ACK 2]`.
3. The sender slides the window forward: `[3, 4, 5, 6]` and sends packets 5 and 6.
4. If packet 4 is lost, the sender retransmits packet 4 and moves forward.

---

## Advantages of Sliding Window Protocol

1. **Improved Throughput**:
   - Allows multiple packets to be in transit, reducing idle time.
   
2. **Efficient Flow Control**:
   - Adjusts transmission rates based on acknowledgment and window size.

3. **Error Handling**:
   - Mechanisms like Go-Back-N and Selective Repeat handle packet loss efficiently.

---

## Disadvantages of Sliding Window Protocol

1. **Complexity**:
   - Implementation of Selective Repeat is more complex.
   
2. **Buffering**:
   - Requires buffers at both sender and receiver for managing unacknowledged packets.

---

## Use Cases

1. **TCP (Transmission Control Protocol)**:
   - Uses the sliding window mechanism for flow and congestion control.
   
2. **Data Link Layer Protocols**:
   - Used in protocols like HDLC (High-Level Data Link Control).

3. **Reliable Communication**:
   - Ensures reliable delivery over lossy or high-latency networks.

---

## Summary

| **Aspect**               | **Sliding Window Protocol**                              |
|--------------------------|---------------------------------------------------------|
| **Purpose**              | Flow control and reliable data transmission.            |
| **Efficiency**           | Improves throughput by sending multiple packets at once.|
| **Modes**                | Stop-and-Wait, Go-Back-N, Selective Repeat.             |
| **Used In**              | TCP, data link protocols, reliable communication.       |

The Sliding Window Protocol enhances the efficiency and reliability of data transmission, making it a core mechanism in modern networking.



---
# Related Topics
### [[Web socket]]
### [[Web Sockets Technologies]]
### [[Web Socket vs HTTP]]
### [[Polling vs WebSockets]]
