---
title: MQTT in Python
category: General
priority: Medium
starred: None
created: 2025-12-25T10:51:12.524745
updated: 2025-12-25T10:51:29.744878
dg-publish: true
---
# MQTT in Python

**Priority:** Medium

## Conversation

### Assistant

### MQTT (in Python)

image_group{"query":["MQTT publish subscribe diagram","MQTT broker architecture","IoT MQTT sensors publisher subscriber"],"num_per_query":1}

**MQTT (Message Queuing Telemetry Transport)** is a **lightweight, publish–subscribe messaging protocol** designed for **low-bandwidth, high-latency, or unreliable networks**. It is widely used in **IoT**, real-time telemetry, and event-driven systems.

When people say **“MQTT in Python”**, they usually mean **using a Python client library to publish and subscribe to MQTT topics via an MQTT broker**.

---

## Core concepts (quick)

- **Broker**  
  Central server that routes messages (e.g., Mosquitto, EMQX).

- **Publisher**  
  Sends messages to a *topic*.

- **Subscriber**  
  Receives messages from a *topic*.

- **Topic**  
  Hierarchical string like `sensors/temperature/room1`.

- **QoS (Quality of Service)**  
  - `0` – at most once (fire-and-forget)  
  - `1` – at least once  
  - `2` – exactly once

---

## Why MQTT instead of HTTP/REST

| Aspect | MQTT | HTTP/REST |
|------|------|-----------|
| Connection | Persistent | Request/response |
| Overhead | Very low | Higher |
| Pattern | Pub/Sub | Client–server |
| Real-time push | Native | Needs polling/WebSockets |
| IoT suitability | Excellent | Moderate |

---

## MQTT in Python (typical stack)

- **Broker**: Mosquitto / EMQX / HiveMQ  
- **Python client**: `paho-mqtt` (most common)

---

## Minimal Python example

### Subscribe
```python
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("sensors/temperature")
client.loop_forever()
```

### Publish
```python
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883)

client.publish("sensors/temperature", "22.5")
client.disconnect()
```

---

## Typical real-world uses

- IoT sensors (temperature, humidity, GPS)
- Mobile → backend real-time updates
- Event streams between microservices
- Smart home systems
- Live dashboards (with WebSocket bridge)

---

## When MQTT is a good choice

- Many devices sending small messages frequently  
- Unreliable or slow networks  
- Need push-based updates  
- Battery-powered devices  

If you want, the next step can be:
- MQTT vs Kafka vs WebSockets (architectural comparison)
- MQTT QoS and message persistence internals
- A small IoT or microservice demo with Docker and Python

---

