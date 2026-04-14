# Precision@K & Retrieval Eval

How to measure whether your RAG retrieval pipeline is actually working.

## The Core Idea

You need a **test set** — a list of queries where you already know the correct chunk for each. Then you run your pipeline and check: of the top-K results returned, how many were actually correct?

## Precision@K Formula

```
P@K = (number of relevant chunks in top K) / K
```

### Example

```
Query: "What is the return policy?"
Correct chunk: chunk_42

Top 3 returned: [chunk_42 ✓, chunk_17 ✗, chunk_89 ✓ (also relevant)]
P@3 = 2/3 = 0.67
```

Average P@K across all test queries → your pipeline score.

## Eval Loop (pseudocode)

```python
scores = []
for query, correct_chunk_id in test_set:
    results = pipeline.retrieve(query, k=5)
    retrieved_ids = [r.id for r in results]
    hits = sum(1 for id in retrieved_ids if id == correct_chunk_id)
    scores.append(hits / 5)

print(f"P@5 = {sum(scores) / len(scores):.2f}")
```

## Using It to Measure Improvement

Run the eval before and after a change:

| Pipeline                        | P@5  |
| ------------------------------- | ---- |
| FAISS only                      | 0.61 |
| FAISS + cross-encoder reranking | 0.78 |

If P@K goes up → the change helped. This is how you make engineering decisions without guessing.

## Other Metrics (for reference)

| Metric | What it measures |
|--------|-----------------|
| **Precision@K** | Of top-K returned, how many are relevant |
| **Recall@K** | Of all relevant chunks, how many appear in top-K |
| **MRR** (Mean Reciprocal Rank) | How high the first correct result appears |
| **NDCG** | Weighted — correct results ranked higher score more |

Precision@K is the simplest to start with. NDCG is used in production systems.

## Related
- [[FAISS]] — what you're evaluating
- [[Cross-Encoder Reranking]] — use P@K to prove reranking helped
- LLM-as-judge — a complementary evaluation method for answer quality (not just retrieval)

### Golden Queries

#me : In evaluating RAB, precision at the rate k. Are the queries predefined and are those called golden queries? 

#tars : I need to search for information about RAB and "precision at rate k" to provide you with an accurate answer.Let me search more specifically for "RAB golden queries" or information about query datasets in RAB evaluation.Based on the search results, I can now provide you with an answer about RAG evaluation and golden queries/datasets.

Yes, in RAG (Retrieval-Augmented Generation) evaluation, queries are typically predefined in curated test sets called "golden datasets". These are also referred to as:

- **Golden datasets** - serving as regression tests that catch quality drops before they reach production
- **Golden queries** - queries used to run retrieval evaluation at different k values
- **Ground truth datasets** - containing **golden** contexts that are relevant to a query to perform evaluation using information retrieval metrics

The terminology "golden" comes from the information retrieval field where binary classifications of documents as relevant or nonrelevant are referred to as the "gold standard" or "ground truth" judgment of relevance.

Multiple queries paired with their **golden** responses collectively form a golden dataset, which shall be used as a benchmark to assess the quality of generated answers in RAG systems. A useful starting golden dataset contains 30-50 real or realistic queries that reflect main use cases, including factual questions with clear answers, multi-document questions requiring synthesis, ambiguous queries, and cases where information is not available.

