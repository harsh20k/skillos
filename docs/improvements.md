# SkillOS — improvement backlog

Short-lived ideas and follow-ups that are not yet ADRs or Linear issues.

---

## Intake: simple RAG-style note retrieval (before / during scaffold)

**Today:** `agents/intake/github_reader.py` builds `notes_summary` by listing all `notes/**/*.md`, taking the **first 2,000 characters** per file, concatenating in list order, and capping the bundle at **8,000 characters**. There is **no** semantic search, keyword search, or relevance ranking.

**Idea:** Add a **lightweight retrieval** step so intake sees **note chunks that match the user’s goal** (and optionally conversation so far), not an arbitrary prefix of every file.

- **When:** Run retrieval **after** there is a usable query (e.g. latest user message in `IntakeState["messages"]`, or accumulated clarify context), and **before** or **in parallel with** heavy clarify/scaffold turns—so the scaffold (and late clarify) is grounded in **relevant** vault content.
- **How (simple tiers):**
  - **Tier A:** Lexical — chunk markdown, index with BM25 or simple TF-IDF over `notes/`, top-k chunks by user goal string.
  - **Tier B:** Embeddings — chunk → embed (Bedrock or small local model), store vectors (in-repo JSON/S3/OpenSearch-lite), similarity search, top-k + optional MMR.
- **Integration:** Replace or **supplement** `fetch_notes_summary` (e.g. `fetch_notes_for_query(client, query, k=...)`) and pass that string into the same “existing notes for context” slot in `clarify` (or a dedicated node between `read_notes` and `clarify` once the first human message exists).
- **Guardrails:** Token budget cap (like today’s 8k), cite chunk paths in context for debuggability, fallback to current behavior if index missing or query empty.

**Outcome:** Better modeling of **what the user already knows** when proposing a new skill tree, without loading unrelated or truncated-only notes.

---

*Add new items below with a `##` heading and a short “Today / Idea / Outcome” block.*