# FAISS (Facebook AI Similarity Search)

A library by Meta for **fast similarity search over large sets of vectors**. Used as the vector store in RAG pipelines.

## The Problem It Solves

Comparing a query against 1M embeddings one-by-one is O(n) — too slow for production. FAISS uses indexing tricks to do **approximate nearest neighbor (ANN)** search in O(log n).

## The Trade-off

FAISS finds vectors that are *close enough* — not always the mathematically exact top-K. In practice, results are 95%+ as good, and nobody notices in a search system.

> Exactness sacrificed → speed gained. Acceptable trade-off.

## How It Works (conceptually)

FAISS clusters your vectors into groups at index time. At query time, it only searches the most relevant clusters — skipping most of the data entirely.

```
Index time:  [1M vectors] → grouped into clusters → stored
Query time:  query vector → find nearest clusters → search only those
```

## Basic Usage

```python
import faiss
import numpy as np

d = 384  # embedding dimensions
index = faiss.IndexFlatL2(d)  # exact search (L2 distance)

# Add vectors
vectors = np.random.rand(1000, d).astype("float32")
index.add(vectors)

# Search
query = np.random.rand(1, d).astype("float32")
distances, indices = index.search(query, k=5)  # top 5
```

## Index Types

| Index | Speed | Accuracy | Use when |
|-------|-------|----------|----------|
| `IndexFlatL2` | Slow | Exact | Small datasets, testing |
| `IndexFlatIP` | Slow | Exact | Cosine similarity (inner product) |
| `IndexIVFFlat` | Fast | Approximate | Production, large datasets |
| `IndexHNSW` | Very fast | Near-exact | Best quality/speed trade-off |

## In a RAG Pipeline

```
Documents → Embeddings → FAISS index
Query → Embedding → FAISS.search(k=10) → Top chunks → LLM context
```

FAISS sits between your embeddings and your LLM. AWS Bedrock KB manages this internally — FAISS is the open-source equivalent you control directly.

## Related
- [[BERT Embeddings]] — what gets stored in FAISS
- [[Cosine Similarity]] — the similarity metric used
- Cross-encoder reranking — improves the results FAISS returns
