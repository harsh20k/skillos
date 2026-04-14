---
title: Service Exposure Models
category: General
priority: Medium
starred: None
created: 2025-12-24T17:19:30.509070
updated: 2025-12-24T17:19:48.038612
dg-publish: true
---
# Service Exposure Models

**Priority:** Medium

## Conversation

### Assistant

Below is a concise taxonomy of **service exposure / communication models**, grouped by interaction style and transport.

---

## 1) Request–Response (Synchronous)
Client sends a request, waits for a response.

- **REST (HTTP/HTTPS)**  
  Resource-based, stateless, JSON/XML.
- **GraphQL (HTTP)**  
  Client-defined queries; single endpoint.
- **RPC (Remote Procedure Call)**  
  - **gRPC** (HTTP/2, Protobuf)  
  - Thrift, Avro RPC  
- **SOAP**  
  XML-based, strict contracts (WSDL).

**Use when:** simple CRUD, low-latency request/response, strong contracts.

---

## 2) Bidirectional / Streaming
Both sides can send data independently.

- **WebSockets** (over TCP)  
  Full-duplex, long-lived connection.
- **gRPC Streaming**  
  Client, server, or bidirectional streams.
- **TCP Sockets**  
  Custom protocols on raw TCP.

**Use when:** real-time updates, chat, live dashboards.

---

## 3) Connectionless / Datagram
No persistent connection; best-effort delivery.

- **UDP**  
  Low latency, no guarantees.
- **QUIC**  
  UDP-based, reliable + encrypted at transport.
- **Custom Datagram Protocols**  
  Game telemetry, real-time media control.

**Use when:** ultra-low latency, tolerate loss (media, telemetry).

---

## 4) Event-Driven / Asynchronous
Producers emit events; consumers react.

- **Message Queues**  
  Point-to-point (e.g., task queues).
- **Publish–Subscribe**  
  Topics, fan-out delivery.
- **Event Streams**  
  Ordered logs with replay (e.g., Kafka-style).
- **Cloud Events / Event Grid**

**Use when:** decoupling, scalability, resilience, workflows.

---

## 5) Data-Centric Access
Expose data rather than actions.

- **Database APIs**  
  SQL/NoSQL over network.
- **Change Data Capture (CDC)**  
  Stream changes from logs.
- **Object Storage APIs**  
  S3-compatible access.
- **File Transfer**  
  SFTP/FTPS.

**Use when:** analytics, batch processing, integrations.

---

## 6) Service Discovery & Mesh (Infra-Level)
Communication mediated by infrastructure.

- **Service Mesh (Sidecars)**  
  mTLS, retries, traffic shaping.
- **Internal Load Balancers / Proxies**
- **DNS-based Discovery**

**Use when:** large microservice estates.

---

## 7) Real-Time Media & Specialized
Optimized for audio/video or constrained devices.

- **WebRTC**  
  Peer-to-peer media + data channels.
- **RTSP / RTP**
- **MQTT**  
  Lightweight pub/sub for IoT.
- **CoAP**  
  REST-like over UDP for constrained devices.

**Use when:** media, IoT, low-power networks.

---

## 8) Server-Push Variants
Server initiates updates.

- **Server-Sent Events (SSE)**  
  One-way push over HTTP.
- **Long Polling**
- **Webhooks**  
  HTTP callbacks to clients.

**Use when:** notifications, simple push without full duplex.

---

## 9) Batch / Offline
Not interactive.

- **Scheduled Jobs / Cron**
- **ETL Pipelines**
- **File Drops**

**Use when:** periodic processing, large datasets.

---

### Quick Selection Guide
- **CRUD APIs:** REST / GraphQL  
- **Strong contracts + performance:** gRPC  
- **Real-time bidirectional:** WebSockets / gRPC streaming  
- **High throughput async:** Event streams / pub-sub  
- **Ultra-low latency:** UDP / QUIC  
- **IoT:** MQTT / CoAP  
- **Media:** WebRTC  

If needed, this can be mapped to **OSI layers**, **latency/throughput trade-offs**, or **example architectures** (e.g., REST + events + WebSockets in one system).

---

