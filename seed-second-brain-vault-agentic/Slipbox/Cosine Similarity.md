# Cosine Similarity

Measures the **angle** between two vectors, not their distance. Used to compare embeddings in ML/RAG systems.

## Formula

```
cosine_similarity(a, b) = dot(a, b) / (||a|| * ||b||)
```

- Result ranges from **-1 to 1**
- **1** = same direction (very similar)
- **0** = perpendicular (unrelated)
- **-1** = opposite direction

## Why not Euclidean distance?

Euclidean penalises vector **magnitude**. A long sentence produces a larger vector than a short one, even if they mean the same thing. Cosine ignores magnitude — only the angle matters.

| Metric | Sensitive to length? | Use case |
|--------|----------------------|----------|
| Euclidean | Yes | Geometry, image pixels |
| Cosine | No | Text similarity, embeddings |

## In Python

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

## Related
- [[Transformers Overview]] — where the vectors (embeddings) come from
- TF-IDF vectors can also be compared with cosine similarity, but BERT embeddings understand context and synonyms
