---
creation date: 2024-12-17 19:13
modification date: Tuesday 17th December 2024 19:13:42
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
# HTTP vs WebSockets

## 1. **HTTP (HyperText Transfer Protocol)**
- **Request-Response Model**: The client sends a request, and the server responds.  
- **Stateless**: Each connection is independent; no persistent connection.  
- **Half-Duplex**: Communication flows in one direction at a time.  
- **Use Case**: Static content delivery, RESTful APIs.

---

## 2. **WebSockets**
- **Full-Duplex**: Allows bi-directional, real-time communication between client and server.  
- **Persistent Connection**: A single TCP connection remains open for continuous data transfer.  
- **Low Overhead**: Avoids repeated connection handshakes.  
- **Use Case**: Real-time chat, live updates, multiplayer games.

---

## Key Differences

| **Feature**       | **HTTP**                     | **WebSockets**                |
| ----------------- | ---------------------------- | ----------------------------- |
| **Communication** | Half-Duplex                  | Full-Duplex                   |
| **Connection**    | Short-lived                  | Long-lived (Persistent)       |
| **Latency**       | Higher (frequent handshakes) | Low (single handshake)        |
| **Overhead**      | High (headers per request)   | Low (after initial handshake) |
| **Protocol**      | Stateless                    | Stateful                      |
| **Use Cases**     | APIs, static content         | Real-time apps, live updates  |

---

## Summary

- **HTTP** is ideal for **request-response** use cases like APIs or web pages.
- **WebSockets** excel in **real-time**, continuous communication scenarios like chat applications or live feeds.


---
# Related Topics
### [[Polling vs WebSockets]]
### [[Web socket]]
### [[Web Sockets Technologies]]

