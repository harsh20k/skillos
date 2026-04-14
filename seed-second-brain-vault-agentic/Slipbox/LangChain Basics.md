# LangChain Basics

A Python framework that packages the "retrieve → format → LLM call" glue code into reusable, composable building blocks.

## Why it exists

Without LangChain, every RAG project rewrites the same boilerplate. LangChain standardises the pieces so you can swap components (e.g. FAISS → Pinecone, OpenAI → Claude) without rewriting the wiring.

## Three Core Primitives

### 1. Chain
A sequence of steps where the output of one feeds into the next.

```python
chain = prompt_template | llm | output_parser
result = chain.invoke({"query": "What is the return policy?"})
```

### 2. Retriever
Wraps any vector store with a standard interface — `.get_relevant_documents(query)`.

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
docs = retriever.get_relevant_documents("What are hazard levels?")
```

Equivalent to: `bedrock_agent_runtime.retrieve()` + manual chunk formatting in GroundSense.

### 3. Tool
A Python function the agent can choose to call, described by a docstring.

```python
from langchain.tools import tool

@tool
def get_hazard_assessment(location: str) -> str:
    """Returns hazard assessment for a given location."""
    # your logic here
    return result
```

Equivalent to: a tool Lambda in a Bedrock Agent action group.

## RetrievalQA Chain (most common RAG pattern)

```python
from langchain.chains import RetrievalQA

chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
)
chain.invoke("What are the hazard levels near site 42?")
# retrieve → format → LLM call — all in one line
```

## GroundSense Mapping

| GroundSense | LangChain equivalent |
|-------------|---------------------|
| `invoke_agent` (Bedrock Agent) | Agent executor |
| Tool Lambda | Tool (`@tool` decorated function) |
| `bedrock_agent_runtime.retrieve()` + formatting | Retriever |
| Bedrock Agent picking tools from action groups | Agent reasoning loop |

## Why learn it if Bedrock Agent works?

- **Portability** — not AWS-locked
- **Control** — inspect and modify every step in Python
- **Evaluation** — easier to plug in LLM-as-judge scoring (topic #10)
- **Multi-agent** — CrewAI and other frameworks build on top of LangChain patterns

## Related
- [[FAISS]] — common retriever backend
- [[Chunking Strategies]] — feeds into the retriever
- [[Cross-Encoder Reranking]] — can be added as a step in the chain
- Multi-agent with CrewAI — extends these patterns to multiple collaborating agents
