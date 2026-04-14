# BERT Embeddings

An **embedding** is a single vector (list of floats) representing the *meaning* of a piece of text. BERT produces one per token — you collapse them into one per sentence for RAG.

## From Tokens → Sentence Embedding

BERT outputs shape: `[1, num_tokens, 768]` — one 768-dim vector per token.

To get one vector per sentence, two common approaches:

| Method | How | When to use |
|--------|-----|-------------|
| **[CLS] token** | Take the first token's vector | Quick, standard BERT |
| **Mean pooling** | Average all token vectors | Often better quality |
| **sentence-transformers** | Model trained end-to-end for this | Best for RAG (recommended) |

## sentence-transformers in practice

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode("The cat sat on the mat")
# shape: (384,) — 384-dim vector
```

This is what most production RAG systems use, including AWS Bedrock KB under the hood.

## What makes a good embedding?

Similar meanings → vectors point in same direction (high cosine similarity)

- "car" and "automobile" → cosine ≈ 0.92
- "car" and "banana" → cosine ≈ 0.11
- Same sentence, different words → still close if semantically equivalent

## Why 768 (or 384)?

It's a design choice — higher dimensions = more expressive but slower to compare. Common sizes:

| Model | Dimensions |
|-------|-----------|
| BERT-base | 768 |
| all-MiniLM-L6-v2 | 384 |
| OpenAI text-embedding-3-large | 3072 |

## Related
- [[Transformers Overview]] — the model that produces these
- [[Cosine Similarity]] — how embeddings are compared
- [[FAISS]] — how embeddings are stored and searched at scale
