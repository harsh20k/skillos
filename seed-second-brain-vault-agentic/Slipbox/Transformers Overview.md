# Transformers Overview

The neural network architecture behind all modern LLMs — BERT, GPT, Claude, etc. Introduced in the 2017 paper *"Attention Is All You Need"*.

## Core Idea

A transformer reads text and produces **context-aware vector representations** of each token. Unlike older models, it understands the whole sentence at once (not word-by-word).

> "bank" near "river" → different vector than "bank" near "money"

## Two Key Objects (HuggingFace)

| Object        | Role                                           |
| ------------- | ---------------------------------------------- |
| **Tokenizer** | Splits text into tokens → converts to integers |
| **Model**     | Takes integers → outputs vectors               |

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

inputs = tokenizer("Hello world", return_tensors="pt")
outputs = model(**inputs)
# outputs.last_hidden_state → shape: [1, num_tokens, 768]
```

## The 768 Number

Every token gets a **768-dimensional vector**. This encodes its meaning in context. To get one vector per sentence, take the `[CLS]` token (first token) — it's trained to summarise the whole input. This is called an **embedding**.

## BERT vs GPT

| | BERT | GPT |
|--|------|-----|
| Purpose | Understand text | Generate text |
| Direction | Reads full sentence (bidirectional) | Left-to-right only |
| Use case | Search, classification, embeddings | Chat, completion |

## TF-IDF vs BERT Embeddings

| | TF-IDF | BERT |
|--|--------|------|
| Synonyms | "car" ≠ "automobile" | "car" ≈ "automobile" |
| Context | None | Full sentence context |
| Vector type | Sparse (mostly zeros) | Dense (768 floats) |

## Related
- [[Cosine Similarity]] — how to compare embeddings
- FAISS — how to search embeddings at scale
