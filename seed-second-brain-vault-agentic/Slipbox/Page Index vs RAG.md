# Page Index vs RAG

**Tags:** #agentic-ai #rag #emerging

**Related:** [[Hot Topics in Agentic AI]] | [[KV Cache Reuse]] | [[Chunking Strategies]] | [[FAISS]]

---

## What is it?
Two different strategies for giving an LLM access to a large document corpus:

- **RAG (Retrieval-Augmented Generation)** — retrieve relevant chunks at query time and inject into context
- **Page Index (Full-context / Long-context)** — load the entire document (or large sections) into a very long context window; the model "reads" it all

---

## RAG — How it works
1. Pre-process: chunk documents, embed, store in vector DB
2. At query time: embed the query, retrieve top-K chunks
3. Inject chunks into the prompt alongside the query

**Best for:** Large corpora (thousands of docs), cost-sensitive workloads, when the relevant section is small and predictable.

**Weaknesses:**
- Retrieval can miss the right chunk (recall failure)
- No reasoning across multiple distant parts of a doc
- Chunk boundaries can cut off critical context

---

## Page Index — How it works
With models supporting 100K–1M+ token contexts, you can load entire documents or books directly into the prompt. The model attends to everything at once.

**Best for:** Single large documents where you need cross-section reasoning (e.g., legal contracts, codebases, research papers).

**Weaknesses:**
- Expensive — cost scales with every token in context
- "Lost in the middle" effect — model attention degrades for content in the middle of very long contexts
- Not practical for large corpora (you can't fit 1,000 docs)

---

## When to use which

| Scenario | Use |
|---|---|
| 10,000 product docs, user asks a question | RAG |
| Single 200-page contract, need cross-section analysis | Page Index |
| Codebase search across many files | RAG |
| Summarize one long report end-to-end | Page Index |
| Mixed: big corpus + deep single-doc analysis | RAG to find doc, then Page Index on that doc |

## [[GroundSense Project Description]] analogy
GroundSense uses RAG to retrieve relevant sensor knowledge and field history. If instead you wanted to analyze one complete field operations log in full, you'd use a page index approach — load the whole log and let the model reason across it.

## Emerging trend
The line is blurring — models with 1M token windows are making page indexing viable for medium-sized corpora, reducing the need for chunking. But cost and latency still favor RAG at scale.
