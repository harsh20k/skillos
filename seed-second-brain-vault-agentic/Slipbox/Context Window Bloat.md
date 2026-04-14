# Context Window Bloat

**Tags:** #agentic-ai #prod-vs-local

**Related:** [[Hot Topics List in Agentic AI]] | [[Token Budgeting]] | [[Semantic Caching]] | [[State Design (Scratchpad)]]

---

## What is it?
The gradual accumulation of too much content in the context window — tool outputs, conversation history, retrieved docs, reasoning traces — until the window is full or performance degrades.

## Why it's a problem
- **Hard limit** — models have fixed context windows (8K–200K tokens). Hit the limit → request fails.
- **Soft degradation** — models perform worse with very long contexts (attention dilution, "lost in the middle" effect)
- **Cost** — every token in context = tokens billed

## Common bloat sources
- Full tool outputs pasted verbatim into context
- Entire conversation history carried forward every turn
- Retrieved RAG chunks that are too large
- Verbose reasoning traces from ReAct loops

## GroundSense analogy
If GroundSense retrieved 20 sensor log documents and stuffed all of them raw into the prompt, the context would bloat fast. Better to summarize or extract only relevant fields.

## Mitigation strategies

| Strategy | How |
|---|---|
| **Summarization** | Compress old turns into a rolling summary |
| **Selective retrieval** | Only pass the top-K most relevant chunks |
| **Tool output pruning** | Extract key fields, discard verbose boilerplate |
| **Windowing** | Keep only the last N messages in context |
| **Semantic caching** | Avoid re-retrieving the same content repeatedly |

## Rule of thumb
Design prompts assuming your context will be 70% full at peak. Leave headroom for tool outputs and model responses.
