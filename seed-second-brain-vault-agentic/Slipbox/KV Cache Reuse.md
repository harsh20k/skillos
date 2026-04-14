# KV Cache Reuse

**Tags:** #agentic-ai #rag #emerging

**Related:** [[Hot Topics in Agentic AI]] | [[Page Index vs RAG]] | [[Token Budgeting]] | [[Semantic Caching]]

---

## What is it?
A transformer optimization where the **Key-Value (KV) attention matrices** computed for a prompt prefix are saved and reused across multiple requests — avoiding redundant computation for repeated context.

---

## Why it matters
Every time you call an LLM, it computes KV vectors for every token in the prompt. If your system prompt + large document is 50K tokens and you send 100 requests, you're computing those same 50K tokens' KV vectors 100 times.

**KV cache reuse** saves those computed vectors after the first call and reuses them — slashing latency and cost for subsequent requests with the same prefix.

---

## How it works
```
Request 1: [System prompt 5K tokens] + [User query]
           → KV vectors computed and CACHED for system prompt

Request 2: [Same system prompt] + [Different query]
           → System prompt KV vectors loaded from cache (skip recomputation)
           → Only new query tokens are computed
```

## Requirements
- The **prefix must be identical** across requests (even a one-token change busts the cache)
- Cache must be stored server-side (handled by the model provider or inference framework)
- Providers that support it: Anthropic (prompt caching), OpenAI, Google (context caching)

---

## Cost & latency impact
- Cache hits: **~90% cost reduction** on cached tokens (Anthropic charges ~10% of normal for cached input tokens)
- Latency: first request pays full cost; subsequent requests are significantly faster

---

## GroundSense analogy
If GroundSense's system prompt includes a large static knowledge base (soil science docs, field manuals), KV cache reuse means that knowledge is computed once and reused across all agent invocations — only the sensor data and user query change each time.

---

## Vs. Semantic Caching

| | KV Cache Reuse | Semantic Caching |
|---|---|---|
| What's cached | Attention computation (KV vectors) | Full LLM responses |
| Match method | Exact prefix match | Embedding similarity |
| Who controls it | Model provider / inference layer | Application layer |
| Granularity | Token-level | Query-level |

---

## Best practice
- Put your **static content first** (system prompt, knowledge base, instructions) — this becomes the cacheable prefix
- Put **dynamic content last** (user query, sensor data, current context)
- Structure: `[Static instructions] → [Static docs] → [Dynamic query]`

## Emerging significance
As long-context models become standard, KV cache reuse is becoming a primary cost-control lever for prod agentic systems — especially those with large, repeated system prompts or document contexts.
