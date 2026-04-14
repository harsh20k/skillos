# ALB vs Auto Scaling Group

## One-line summary
**ALB** distributes traffic across instances. **ASG** manages how many instances exist.

---

## Application Load Balancer (ALB)
- Operates at **Layer 7** (HTTP/HTTPS)
- Routes incoming requests across healthy targets
- Supports path-based routing, host-based routing, sticky sessions
- Performs health checks — stops sending traffic to unhealthy instances
- Lives in front of your compute fleet

## Auto Scaling Group (ASG)
- Manages the **count of EC2 instances**
- Scales out (adds instances) or scales in (removes instances) based on metrics
- Common triggers: CPU utilization, memory, request count, custom CloudWatch metrics
- Can follow schedules (e.g. scale up before peak hours)
- Ensures minimum and maximum instance boundaries are respected

---

## How they work together

![[image-192.png]]

```
Internet → ALB → [EC2, EC2, EC2, EC2*]  ← ASG manages this fleet
                                  * newly added instance
```

- The ALB has a **Target Group** that the ASG registers instances into automatically
- As ASG adds/removes instances → ALB starts/stops routing to them seamlessly
- You almost always deploy both together in production

---

## Key difference table

|                  | ALB                 | ASG                             |
| ---------------- | ------------------- | ------------------------------- |
| Purpose          | Distribute traffic  | Manage instance count           |
| Acts on          | Requests            | Instances                       |
| Responds to      | HTTP paths, headers | CPU, latency, schedules         |
| Can exist alone? | Yes (fixed fleet)   | Yes (but traffic is unbalanced) |

---
## Tags
#aws #cloud #networking #compute #system-design
