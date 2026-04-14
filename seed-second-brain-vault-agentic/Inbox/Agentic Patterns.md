---
creation date: 2026-03-22 13:45
tags:
description:
---
#me : what are agentic patterns? 

# [[Hot Topics in Agentic AI]]

#tars : Agentic patterns refer to design patterns and architectural approaches for building AI agents—systems that can autonomously perform tasks, make decisions, and interact with their environment to achieve goals. These patterns have emerged as best practices for developing more capable and reliable AI systems, particularly with large language models (LLMs).

Common agentic patterns include:

1. **Reflection/Self-Critique** - The agent reviews and critiques its own outputs to improve quality and catch errors

2. **Tool Use** - Agents can call external tools, APIs, or functions to access information or perform actions beyond their base capabilities

3. **Planning** - Breaking down complex tasks into steps or creating action plans before execution

4. **Multi-agent Collaboration** - Multiple specialized agents working together, each handling different aspects of a problem

5. **Memory/State Management** - Maintaining context and information across interactions to enable more coherent long-running tasks

6. **ReAct (Reasoning + Acting)** - Alternating between reasoning about the problem and taking actions, allowing the agent to adjust its approach dynamically

These patterns help address limitations of simple prompt-response interactions by enabling agents to be more autonomous, iterative, and capable of handling complex, multi-step tasks. They're increasingly used in applications like coding assistants, research tools, customer service automation, and workflow orchestration.

# Agentic Search over vector Embeddings

#me : **Agentic Search over Vector embeddings** ? Thoughts?

#tars : [[Agentic search]] over vector embeddings is an interesting evolution that combines [[Semantic Search]] capabilities with autonomous decision-making. Here are some thoughts on this approach:

**Key Advantages:**

1. **[[Dynamic Query Refinement in Agentic Search|Dynamic Query Refinement]]** - Instead of a single vector search, an agent can iteratively refine queries based on initial results, reformulating searches to fill gaps or explore different semantic angles

2. **[[Multi-step Retrieval]]** - Agents can perform sequential searches, using insights from one search to inform the next, building up comprehensive understanding progressively

3. **[[Intelligent Filtering]]** - Beyond similarity scores, agents can apply reasoning to evaluate relevance, synthesize across multiple retrieved chunks, and determine what additional context is needed

4. **Hybrid Strategies** - Agents can decide when to use vector search vs. keyword search vs. graph traversal, or combine multiple retrieval methods based on the query type

**Practical Applications:**

- **[[Agentic search#How Agentic Search Enhances RAG|RAG Enhancement]]** - Moving beyond simple "retrieve-then-generate" to iterative retrieval with relevance checking
- **Research Assistants** - Exploring document collections with follow-up questions and cross-referencing
- **Complex Q&A** - Gathering evidence from multiple sources before synthesizing answers

**Challenges:**

- **Latency** - Multiple search iterations add overhead
- **Cost** - More LLM calls for planning and evaluation
- **Complexity** - Harder to debug and predict behavior
- **Diminishing Returns** - Not all queries benefit from agentic complexity

**Design Considerations:**

- When should the agent stop searching?
- How to balance exploration vs. exploitation?
- Should the agent rerank/rewrite retrieved content?
- How to maintain coherent context across searches?

This approach makes most sense for complex information needs where simple semantic search is insufficient, though it may be overkill for straightforward lookups.

#me : what is the pattern "Background Agent with CI Feedback"?

#tars : 

## Background Agent with CI Feedback

The **"Background Agent with CI Feedback"** pattern is an agentic approach where an AI coding agent operates asynchronously in the background and uses Continuous Integration (CI) test results as a feedback loop to iteratively improve code until it passes all checks.

## How It Works:

The agent pushes code to a branch and triggers CI tests, polls CI results periodically for failures, uses test failure outputs as feedback to apply fixes, and notifies humans when all tests pass.

## Key Characteristics:

1. **Asynchronous Operation** - Background agents operate in a remote environment, allowing you to spawn tasks that edit and run code independently in the background

2. **Iterative Self-Correction** - The agent uses test failure outputs (stack traces, error messages) as machine-readable feedback and autonomously applies fixes to specific files or functions without human intervention

3. **CI as Validation Layer** - The pattern integrates with CI/CD pipelines by enabling the agent to act on CI checks in GitHub pull requests, creating an "outer loop" of validation

4. **Human-in-the-Loop** - A developer receives the PR, reviews the agent's work, and decides whether to approve, request changes, or reject the fix

## Benefits:

- Fixes are proposed within minutes of a failure, drastically reducing the time from broken build to merged patch
- Agents handle tedious tasks of identifying, debugging, and fixing common errors, letting engineers focus on architecture and features
- Prevents blocking developers during long test suite runs

## Trade-offs:

- The agent may produce PRs that fail CI, which is frustrating and forces engineers to decide whether to fix the half-broken code
- Requires proper CI infrastructure and error parsing capabilities

>This pattern essentially treats CI as an automated "teacher" that guides the agent toward correct solutions through repeated feedback cycles.


# Dogfooding with Rapid Iteration for Agent Improvement

#me : Concisely explain Dogfooding with Rapid Iteration for Agent Improvement?

#tars : **Dogfooding with Rapid Iteration for Agent Improvement** is a pattern where developers use their own AI agent internally ("eating your own dog food") and rapidly iterate on it based on real-world usage feedback.

**Core Idea:**
- Deploy the agent for internal use on actual tasks
- Collect feedback, failure cases, and edge cases from daily usage
- Quickly iterate and improve the agent based on observed behavior
- Repeat continuously

**Key Benefits:**
- **Real-world testing** - Discover issues that synthetic tests miss
- **Fast feedback loops** - Internal users provide immediate, detailed feedback
- **Authentic use cases** - Agents face genuine problems, not contrived examples
- **Quality signal** - If your team won't use it, customers probably won't either

**Example:**
A company building a coding agent uses it internally for their own development work, observes where it fails or produces poor code, updates prompts/tools/guardrails, and redeploys within hours or days.

**Why "Rapid Iteration" matters:**
Unlike traditional software, agents can often be improved through prompt engineering, tool adjustments, or fine-tuning without full release cycles—allowing daily or even hourly improvements based on dogfooding insights.

This pattern is particularly valuable early in agent development when behavior is unpredictable and traditional testing methods are insufficient.

