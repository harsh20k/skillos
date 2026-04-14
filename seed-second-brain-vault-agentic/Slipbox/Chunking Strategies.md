# Chunking Strategies

Before embedding documents into a vector store, you must split them into chunks. Chunk quality directly determines retrieval quality — no model can fix bad chunking.

## The Three Main Strategies

| Strategy | How | Pros | Cons |
|----------|-----|------|------|
| **Fixed-size** | Every chunk = N words, X% overlap | Simple, fast, good default | Ignores sentence/topic boundaries |
| **Sentence-based** | Split on punctuation/sentence boundaries | Cleaner semantics | Variable length, harder to control |
| **Semantic chunking** | Embed each sentence, split where cosine similarity drops | Best quality | Slow, expensive |

## Fixed-Size with Overlap (recommended starting point)

- **Chunk size:** 100–200 words
- **Overlap:** ~20% (20–40 words repeated between adjacent chunks)

**Why overlap?** A sentence split across chunk 3 and chunk 4 would be retrieved by neither without overlap. With overlap, both chunks contain that context — at least one gets retrieved.

```
[  chunk 1  ][  chunk 2  ][  chunk 3  ]
          [overlap]    [overlap]
```

## Edge Cases to Watch

- **Tables in PDFs** — rows split mid-cell under fixed-size chunking. Need special parsing first (see Document Parsing note)
- **Headers/titles** — should stay attached to the content below, not isolated in their own chunk
- **Very short chunks** (<50 words) — tend to retrieve as noise, too little context
- **Very long chunks** (>500 words) — embedding loses specificity, everything starts looking similar

## Chunk Size Trade-off

| Smaller chunks | Larger chunks |
|----------------|---------------|
| More precise retrieval | More context per chunk |
| May miss surrounding context | Embedding loses specificity |
| More chunks to store/search | Fewer chunks, faster indexing |

## In a RAG Pipeline

```
PDF → parse → split into chunks → embed each chunk → store in FAISS
Query → embed → FAISS.search(k=10) → top chunks → LLM context
```

Bad chunking = relevant content split across boundaries = never retrieved = wrong answer from LLM.

## Related
- [[FAISS]] — where chunks get stored after embedding
- [[BERT Embeddings]] — how each chunk becomes a vector
- Document Parsing — must parse cleanly before chunking (tables, headers)
- Cross-encoder reranking — improves ordering of retrieved chunks
