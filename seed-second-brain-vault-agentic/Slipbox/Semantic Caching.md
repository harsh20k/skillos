# Semantic Caching

**Tags:** #agentic-ai #prod-vs-local

**Related:** [[Hot Topics List in Agentic AI]] | [[Context Window Bloat]] | [[Token Budgeting]]

---

## What is it?
Caching LLM responses (or retrieved documents) based on **semantic similarity** rather than exact string match. If a new query is *similar enough* to a cached one, return the cached result.

## Vs. traditional caching
| | Traditional cache | Semantic cache |
|---|---|---|
| Match method | Exact key match | Embedding similarity |
| Hit rate | Low (queries vary slightly) | High (similar intent = same answer) |
| Storage | Key-value store | Vector store + key-value |

## How it works
1. Embed the incoming query
2. Search cache for nearest embedding
3. If similarity > threshold → return cached response
4. Else → call LLM, store result + embedding

## GroundSense analogy
"What is the soil moisture at Zone B?" and "Tell me Zone B's current moisture level" are different strings but the same intent. Semantic caching would serve the second query from cache.

## Benefits
- Reduces LLM API calls → lower latency + cost
- Especially valuable for repeated/similar user queries in prod
- Reduces context window pressure (cached answers skip retrieval)

## Pitfalls
- Stale cache — cached answer was correct yesterday but data changed
- Threshold tuning — too low = wrong cache hits; too high = no cache benefit
- Cache invalidation for time-sensitive data

## Tools
GPTCache, Redis + embeddings, custom vector DB layer
