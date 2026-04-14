# Embeddings — Tokens to Vector Space

**Core idea:** Any input (text, image, audio) → list of numbers (a vector). Similar meaning = closer in space.

## How it works

1. Input is tokenized
2. Embedding model (e.g. `gemini-embedding-2-preview`) converts it to a high-dimensional vector (3072 numbers)
3. Vectors are stored in a vector DB (Pinecone, pgvector, FAISS)
4. At query time: embed the query → find nearest vectors → retrieve those chunks

The **3D visualizations** you see in slides are projections (via PCA/t-SNE) — the real space is thousands of dimensions. Humans can't see 3072D, so it's compressed for illustration.

## Classic example
```
King − Man + Woman ≈ Queen
```
The math works because meaning is encoded geometrically.

## Gemini's multimodal shared space (`gemini-embedding-2-preview`)
- Text, image, video, audio, and PDFs are embedded into the **same vector space**
- A text query can retrieve an image result — and vice versa
- Embeddings can be shortened (truncated) for storage/speed trade-offs
- Task-aware: retrieval, classification, clustering, and similarity can be optimized differently

## Why it matters for agents
Agents use embeddings before reasoning:

| Use case | How embeddings help |
|---|---|
| RAG | Find relevant document chunks semantically |
| Agent memory | Retrieve the right past context |
| Routing | Classify which agent should handle a query |
| Multimodal search | Search across text + images with one query |
| Clustering | Group similar tasks or documents |

## Relation to your projects
- **GroundSense** already uses embeddings for RAG retrieval
- **Project 3 (Multi-Agent Swarm):** the RAG agent pod uses embeddings to find the right context before passing it to the LLM
- Gemini multimodal embeddings become relevant if you add screenshot/image inputs to GroundSense

## Related notes
- [[BERT Embeddings]]
- [[Cosine Similarity]]
- [[FAISS]]
- [[Chunking Strategies]]
- [[Cross-Encoder Reranking]]
- [[Semantic Caching]]
