---
creation date: 2024-12-17 19:18
modification date: Tuesday 17th December 2024 19:18:53
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
# Polling vs WebSockets

## 1. **Polling**
Polling is a technique where the client repeatedly sends HTTP requests to the server at regular intervals to check for updates.

### Characteristics:
- **Request-Response**: Client requests, server responds.
- **Inefficient**: Many requests even when no updates are available.
- **Latency**: Updates are delayed until the next poll.
- **Resource-Intensive**: High server load due to frequent requests.

### Example Use Case:
- Simple applications where real-time updates are not critical.

---

## 2. **WebSockets**
WebSockets provide a persistent, full-duplex connection between the client and server, allowing continuous two-way communication.

### Characteristics:
- **Real-Time**: Instant updates without repeated requests.
- **Efficient**: Low overhead after initial connection.
- **Persistent Connection**: Single connection for bi-directional communication.
- **Low Latency**: Faster response times.

### Example Use Case:
- Real-time chat, stock price updates, and online gaming.

---

## Comparison Table

| **Feature**         | **Polling**                   | **WebSockets**              |
| ------------------- | ----------------------------- | --------------------------- |
| **Connection Type** | Repeated HTTP requests        | Persistent TCP connection   |
| **Latency**         | Higher (depends on interval)  | Low (real-time updates)     |
| **Efficiency**      | Inefficient (redundant polls) | Efficient (continuous data) |
| **Server Load**     | High (many requests)          | Low (single connection)     |
| **Data Flow**       | Client-to-server only         | Bi-directional              |

---

## Summary

- **Polling**: Suitable for non-critical, periodic updates but inefficient for real-time applications.
- **WebSockets**: Ideal for real-time, low-latency communication with bi-directional data flow.


---
# Related Topics
### [[Web socket]]
### [[Polling vs WebSockets]]
### [[Web Socket vs HTTP]]
### [[Web Sockets Technologies]]

