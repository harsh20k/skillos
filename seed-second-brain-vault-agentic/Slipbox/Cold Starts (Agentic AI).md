# Cold Starts (Agentic AI)

**Tags:** #agentic-ai #prod-vs-local

**Related:** [[Hot Topics List in Agentic AI]] | [[Concurrency Issues (Agents)]] | [[Token Budgeting]]

---

## What is it?
The latency spike that occurs when an agent or its underlying infrastructure (Lambda, container, model endpoint) starts from a fully idle state.

## Sources of cold start latency

| Layer | Cold start cause |
|---|---|
| **Lambda / container** | Provisioning + runtime init |
| **LLM endpoint** | Model loading into GPU memory |
| **Vector DB** | Index loading, connection pool setup |
| **Agent framework** | Tool registration, prompt compilation |

## Prod impact
- First request after idle period is slow (2–15s extra latency is common)
- Can cause cascading timeouts if downstream services have tight SLAs
- Users experience inconsistent response times

## GroundSense analogy
GroundSense Lambdas behind Bedrock action groups cold-start if not invoked recently. A burst of sensor alerts after a quiet night could spike latency on the first few calls.

## Mitigation strategies
- **Provisioned concurrency** (Lambda) — keeps N instances warm at all times
- **Scheduled pings** — dummy invocations every few minutes to keep alive
- **Container pre-warming** — deploy always-on sidecars
- **Async queue** — accept requests immediately, process when warm

## Local vs Prod difference
Locally, "cold starts" don't exist — your process is always running. In prod, any serverless component can go cold.
