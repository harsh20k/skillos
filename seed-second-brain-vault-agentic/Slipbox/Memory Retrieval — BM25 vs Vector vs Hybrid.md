# Memory Retrieval — BM25 vs Vector vs Hybrid

From Pavan's lecture. Core concept for RAG pipelines and agent memory systems.

## The three approaches

| | BM25 (Sparse) | Vector (Dense) | Hybrid ★ |
|---|---|---|---|
| **Method** | Exact keyword matching | Embedding similarity | BM25 + Vector merged |
| **Best for** | Invoice IDs, error codes, order numbers, legal clause names, exact rare terms | Paraphrases, natural language, synonyms, long-form knowledge | Enterprise RAG, support search, policy retrieval, document-heavy agents |
| **Strengths** | Fast, interpretable, no embedding needed | Understands meaning, synonyms, related concepts | Strong recall + exact term matching together |
| **Weaknesses** | Misses semantic similarity and paraphrases | Slower, needs embeddings, can miss exact rare terms | More infra, merging logic, and tuning complexity |
| **Production use** | Specialised / legacy search | Semantic search | **Default production choice** |

## Concrete example

**Query:** "show invoices that are overdue and need payment reminder"

| Retriever | What it finds |
|---|---|
| BM25 | Documents containing "invoice", "overdue", "payment" — exact matches |
| Vector | "past due receivables", "unpaid vendor bills", "follow-up on pending invoices" — semantic matches |
| Hybrid | Both — exact overdue invoice records + semantically related payment-due items = strongest recall |

## How agents use retrieval

Agents rarely answer from memory alone. The pattern is:

```
User query
  → embed query
  → retrieve relevant chunks (BM25 / Vector / Hybrid)
  → place chunks into context window
  → LLM reasons over retrieved context
  → answer
```

This is the RAG loop. The retrieval step determines quality ceiling — bad retrieval = bad answers, regardless of LLM quality.

## When to use what

- **BM25 alone** — structured data, exact IDs, error codes, legal/compliance search where exact term matters
- **Vector alone** — conversational search, paraphrase-heavy queries, knowledge bases
- **Hybrid** — production default for enterprise RAG. Use RRF (Reciprocal Rank Fusion) or a cross-encoder reranker to merge results

## Relation to your projects

- **GroundSense:** currently uses vector retrieval (Bedrock embeddings). Adding BM25 → Hybrid is a concrete upgrade that improves retrieval recall — good latency analysis follow-up
- **Project 3 (Multi-Agent Swarm):** the RAG agent pod should implement Hybrid search as the default
- Hybrid + [[Cross-Encoder Reranking]] is the strongest production RAG retrieval stack

## Related notes
- [[Embeddings — Tokens to Vector Space]]
- [[FAISS]]
- [[Cosine Similarity]]
- [[Cross-Encoder Reranking]]
- [[Chunking Strategies]]
- [[Semantic Caching]]
- [[Precision@K & Retrieval Eval]]
- [[Page Index vs RAG]]
