# Output Parsing (Agents)

**Tags:** #agentic-ai #agent-design

**Related:** [[Hot Topics List in Agentic AI]] | [[Error Handling (Agents)]] | [[Tool Orchestration]]

---

## What is it?
Extracting structured, usable data from LLM outputs — which are raw text by default.

## The problem
LLMs don't reliably return clean JSON or structured data unless forced. Agents that depend on structured output break when parsing fails.

## Parsing strategies

### 1. Strict JSON mode
Force JSON via system prompt or model API setting (e.g., OpenAI `response_format: json_object`). Most reliable.

### 2. Regex / string extraction
Parse known patterns from text. Brittle but works for simple cases.

### 3. Retry with correction
If parsing fails, re-prompt: *"Your last output wasn't valid JSON. Here's what you returned: [X]. Please fix it."*

### 4. Output schema + validation
Define a Pydantic/TypedDict schema, validate against it, reject if invalid.

## GroundSense analogy
Bedrock action group Lambdas return structured JSON responses back to the agent — if the schema is wrong, the agent gets confused. Output parsing is the reverse: ensuring the *agent's* decisions come back in a parseable format.

## Best practice
- Always specify exact output format in the prompt with an example
- Validate before consuming — never assume LLM returned valid structure
- Log raw outputs for debugging
