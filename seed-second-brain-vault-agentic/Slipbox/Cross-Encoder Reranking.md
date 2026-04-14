# Cross-Encoder Reranking

A second-stage model that **re-scores retrieved chunks** by reading the query and chunk *together* — much more accurate than embedding similarity alone.

## The Problem with FAISS alone

FAISS uses **bi-encoders** — query and chunk are embedded *separately*, then compared. It never sees them together, so it can miss semantic matches where wording differs.

> Query: "What are the side effects?"
> Top FAISS result: a chunk that contains the heading "Side Effects" but no actual content
> Better answer: a chunk saying "Adverse reactions include nausea, headache, fatigue" — ranked lower by FAISS

## How Cross-Encoders Work

The query and chunk are **concatenated** and fed into the model together:

```
Input: [CLS] What are the side effects? [SEP] Adverse reactions include nausea... [SEP]
Output: relevance score (single float, e.g. 0.94)
```

The model reads both at once — attention flows between query tokens and chunk tokens. It understands *why* one is relevant to the other, not just surface similarity.

It's the **same BERT architecture** as a bi-encoder — the difference is training data. Cross-encoders are trained on (query, relevant chunk) pairs, so they learn to score relevance *between* two pieces of text, not just represent one piece of text as a vector.

## Two-Stage Pipeline (standard production pattern)

```
All chunks
    ↓
FAISS (bi-encoder) — retrieve top 50 fast       ← speed
    ↓
Cross-encoder — rerank top 50, return top 5     ← accuracy
    ↓
LLM context
```

Never run cross-encoder over all chunks — it's too slow. Use FAISS to shortlist, cross-encoder to reorder.

## Speed vs Accuracy

| | Bi-encoder (FAISS) | Cross-encoder |
|--|-------------------|---------------|
| Speed | Very fast (O log n) | Slow (reads pairs) |
| Accuracy | Good | Much better |
| Scales to | Millions of chunks | ~50–100 candidates |
| How it works | Separate embeddings compared | Joint reading of query+chunk |

## Common Model

```python
from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
scores = model.predict([
    ("What are side effects?", "Adverse reactions include nausea..."),
    ("What are side effects?", "Side Effects section heading only..."),
])
# scores: [0.94, 0.21] → rerank by these
```

## Related
- [[FAISS]] — stage 1, provides the candidate set
- [[Chunking Strategies]] — chunk quality still matters before reranking
- [[Precision@K & Retrieval Eval]] — how to measure if reranking actually helped
