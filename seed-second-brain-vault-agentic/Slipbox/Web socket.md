---
creation date: 2024-12-17 19:02
modification date: Tuesday 17th December 2024 19:02:24
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - "#slipbox/permaNotes/webtech"
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
# What are WebSockets?

**WebSockets** are a communication protocol that provides **full-duplex**, real-time communication between a client (e.g., a browser) and a server over a single, long-lived TCP connection. Unlike HTTP, which is request-response based, WebSockets allow continuous bi-directional data flow.

---

## Key Characteristics:
1. **Full-Duplex**: Both client and server can send and receive messages simultaneously.
2. **Persistent Connection**: Reduces the overhead of repeatedly establishing connections.
3. **Low Latency**: Ideal for real-time applications like chats, games, or live updates.

---

## Example Use Cases:
- **Real-Time Chat Applications**: Send and receive messages instantly.
- **Live Data Feeds**: Stock prices, sports scores.
- **Online Multiplayer Games**: Low-latency interaction.
- **Collaborative Tools**: Live document editing.

---

## Example WebSocket Lifecycle (Simplified)

1. **Handshake**: WebSocket connection starts as an HTTP request and upgrades to WebSocket.
2. **Communication**: Continuous two-way data flow occurs.
3. **Closing Connection**: Either client or server can terminate the connection.

---

## Related Interview Topics:

1. **[[Web Socket vs HTTP|HTTP vs WebSockets]]**:
   - Difference between request-response (HTTP) and full-duplex (WebSocket).

2. **[[Polling vs WebSockets]]**:
   - Comparison of techniques like long polling, short polling, and WebSockets.

3. **Event-Driven Communication**:
   - Understanding how real-time events are handled in WebSockets.

4. **WebSocket Libraries**:
   - Knowledge of libraries like `Socket.IO` (Node.js), `Spring WebSocket` (Java).

5. **WebSocket Security**:
   - Use of WSS (WebSocket Secure) for encrypted connections.
   - Authentication and handling DoS attacks.

6. **Protocols & Alternatives**:
   - **MQTT**: Lightweight protocol for IoT communication.
   - **gRPC**: Modern, efficient remote procedure call system.
   - **Server-Sent Events (SSE)**: Unidirectional real-time communication.

---

## Summary:

WebSockets enable **real-time, bi-directional communication** over a single connection, making them ideal for applications requiring low-latency and persistent communication. Related interview topics include HTTP vs WebSockets, event-driven architecture, and security considerations.


---
# Related Topics
### [[Web Sockets Technologies]]
### [[Web Socket vs HTTP]]
### [[Polling vs WebSockets]]

