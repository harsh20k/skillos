# ML & RAG Learning Roadmap

A structured learning path from transformer basics to production-ready RAG systems. Each topic builds directly on the previous one.

---

## The Full Pipeline

```mermaid
flowchart TD
    A[Raw Documents] --> B[Document Parsing]
    B --> C[Chunking]
    C --> D[BERT Embeddings]
    D --> E[FAISS Vector Store]
    
    Q[User Query] --> QE[Embed Query]
    QE --> E
    E -->|top 50 candidates| R[Cross-Encoder Reranking]
    R -->|top 5 chunks| LLM[LLM — Generate Answer]
    
    LLM --> EVAL[Evaluation]
    EVAL --> PK[Precision@K]
    EVAL --> JU[LLM-as-Judge]
    JU --> AB[A/B Testing]
    AB --> OB[Observability]
```

---

## The 12 Topics

### Foundation — Understanding the ML Layer
1. **[[Transformers Overview]]** — The architecture behind all LLMs. BERT, GPT, Claude all use this. Opens the hood on what Bedrock is doing.
2. **[[BERT Embeddings]]** — One vector per sentence representing its meaning. The core unit of RAG. Cosine similarity measures how close two meanings are → [[Cosine Similarity]]
3. **[[FAISS]]** — Store and search millions of embeddings fast using approximate nearest neighbor search. The vector store inside every RAG system.

### Advanced RAG — Making Retrieval Better
4. **[[Chunking Strategies]]** — How you split documents before embedding. Fixed-size with 20% overlap is the default. Bad chunking = bad retrieval regardless of model quality.
5. **[[Cross-Encoder Reranking]]** — Two-stage retrieval: FAISS retrieves top 50 fast, cross-encoder reranks top 50 accurately. Reads query + chunk jointly.
6. **[[Precision@K & Retrieval Eval]]** — Measure retrieval quality. Of the top-K chunks returned, how many were actually correct? Run before/after each pipeline change.

### Agents — Formalizing Orchestration
7. **[[LangChain Basics]]** — Composable building blocks for RAG pipelines. Chains, retrievers, tools. Equivalent to what Bedrock Agent does, but explicit and controllable in Python.
8. **[[Multi-Agent with CrewAI]]** — Multiple specialised agents collaborating. Retriever agent + validator agent. Formalises what Bedrock Agent does implicitly with action groups.

### Real-World Data
9. **[[Document Parsing (PDF to JSON)]]** — Parse PDFs into structured JSON before chunking. Critical for tables — raw text extraction destroys row/column structure.

### Production — Measuring & Shipping
10. **[[LLM-as-Judge Evaluation]]** — Use Claude to score answer quality across three dimensions: faithfulness, relevance, completeness. Catches hallucination and gaps P@K misses.
11. **[[A-B Testing Prompts & Shadow Deployment]]** — Run two prompt variants on real traffic, score with LLM-as-judge, switch only when consistently better.
12. **[[Latency & Observability]]** — p95 latency, CloudWatch metrics, X-Ray traces. Know which tool is slow, how many calls the agent makes, where failures happen.

---

## Learning Clusters

| Cluster                 | Topics           | Theme                       |
| ----------------------- | ---------------- | --------------------------- |
| **Embeddings & Search** | 1 → 2 → 3        | Foundational ML concepts    |
| **Advanced RAG**        | 4 → 5 → 6        | Improving what you've built |
| **Agents**              | 7 → 8            | Formalising orchestration   |
| **Production**          | 9 → 10 → 11 → 12 | Measuring and shipping      |

---

## GroundSense Gaps This Roadmap Fills

| Gap                                                    | Topic                                       |
| ------------------------------------------------------ | ------------------------------------------- |
| No visibility into tool call order or timing           | [[Latency & Observability]]                 |
| Tables in PDFs likely being mangled before chunking    | [[Document Parsing (PDF to JSON)]]          |
| No measurement of answer quality (hallucination, gaps) | [[LLM-as-Judge Evaluation]]                 |
| No way to safely test prompt changes                   | [[A-B Testing Prompts & Shadow Deployment]] |
| Retrieval quality never measured                       | [[Precision@K & Retrieval Eval]]            |

[[Brochure Analytix Lab Full stack AI developer]]
