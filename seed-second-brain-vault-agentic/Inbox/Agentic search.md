---
creation date: 2026-03-22 17:23
tags:
description:
---

#me : Overview of Agentic Seach

#tars : I'll search for information about Agentic Search to provide you with an overview.
## Overview of Agentic Search

**Agentic Search** is an AI-powered information retrieval approach that goes beyond traditional keyword matching or basic generative search. It actively understands a user's underlying intent, performs [[#How Iterative Queries Work|iterative queries|]], synthesizes information from multiple sources, and refines results to achieve a comprehensive answer or solution.

### Key Characteristics

An agentic system takes actions on a human's behalf, follows multi-step instructions, keeps memory and context, and features tool calling—these are the signature features of an agent. Agentic search refers to systems that are capable of interpreting user intent, picking up information from multiple sources, and completing chained actions autonomously — without requiring step-by-step instruction from the user.

### How It Works

Agentic search lets you ask questions in natural language and have the system plan and execute the retrieval automatically. A preconfigured agent reads the question, plans the search, and returns relevant results.

The process typically involves:

1. **Query Understanding**: An LLM analyzes the entire chat thread to identify the underlying information need. Instead of a single, catch-all query, the LLM breaks down compound questions into focused subqueries based on: user questions, chat history, and parameters on the request.

2. **Multi-step Execution**: Subqueries run in parallel. Each subquery is semantically reranked to promote the most relevant matches. The best results are combined into a unified response that an LLM can use to generate answers.

3. **Iterative Refinement**: The agent can determine to run more RAG queries/keyword searches if it believes it doesn't have enough information. The agent can determine that this is the case and choose to fire more RAG/keyword search queries if it thinks it's needed.

### Core Components

A search agent system is composed of a corpus of documents used to construct a search index, a search API which takes queries in and returns results, a set of "tools" that allow a language model to use the search API, and the AI model which is given the task and tools and instructed to provide an answer.

### Use Cases

Agentic search is particularly valuable for:
- Providing agents and apps with the most relevant content for answering harder questions, leveraging chat context and proprietary content
- Complex queries requiring synthesis from multiple data sources
- Enterprise environments where real-time, permission-aware search is critical

#me : What are Iterative queries ?

#tars : Based on the context of agentic search, **iterative queries** refer to the process where the AI agent performs multiple rounds of searching and refinement rather than executing just a single search.

## How Iterative Queries Work

In agentic search systems:

1. **Initial Query Execution**: The agent starts by breaking down a complex question into focused subqueries and executing searches

2. **Assessment**: After receiving initial results, the agent evaluates whether it has sufficient information to answer the user's question comprehensively

3. **Additional Searches**: If the agent determines it lacks enough information or needs clarification, it automatically performs additional searches without requiring the user to ask follow-up questions

4. **Refinement**: Each round of queries can be refined based on what was learned from previous searches, allowing the agent to progressively zero in on the most relevant information

## Key Difference from Traditional Search

Unlike traditional search where you get one set of results from one query, iterative queries allow the agent to:
- **Adapt**: Adjust search strategy based on intermediate results
- **Fill gaps**: Identify missing information and search specifically for it
- **Converge**: Keep searching until a satisfactory answer can be constructed

This iterative approach mimics how a human researcher might conduct research - not just searching once, but following leads, identifying gaps in knowledge, and conducting additional targeted searches until they have enough information to answer the question thoroughly.

#me : Agentid search for RAG enhancement

#tars : I'll search for information about how agentic search enhances RAG (Retrieval-Augmented Generation) systems.## Agentic Search for RAG Enhancement

Agentic RAG is the use of AI agents to facilitate retrieval augmented generation (RAG), adding AI agents to the RAG pipeline to increase adaptability and accuracy.

### Key Limitations of Traditional RAG

Traditional RAG systems are constrained by static workflows and lack the adaptability required for multistep reasoning and complex task management. Traditional RAG systems are reactive data retrieval tools that find relevant information in response to specific queries, with no ability to adapt to changing contexts or access other data.

### How Agentic Search Enhances RAG

**1. Dynamic Retrieval Strategies**

Agentic RAG embeds autonomous AI agents into the RAG pipeline that leverage agentic design patterns—reflection, planning, tool use, and multiagent collaboration—to dynamically manage retrieval strategies and iteratively refine contextual understanding.

**2. Query Intelligence**

An LLM breaks down complex queries into smaller, focused subqueries for better coverage, which can include chat history for extra context, and runs subqueries in parallel. The agent can itself decide the prompt to use for vector search, rewriting the prompt to get even better results.

**3. Iterative Refinement**

An agent can use a reasoning model to check the relevancy of an answer and rewrite the query, iterating until the best response is achieved. The agent can iteratively fetch information, first doing one vector search call, checking if it has enough information, and if not, fetching even more information.

**4. Flexible Multi-Source Access**

Agentic RAG applications pull data from multiple external knowledge bases and allow for external tool use, whereas standard RAG pipelines connect an LLM to a single external dataset.

### Key Benefits

- Improved accuracy because responses are based on verified, current data
- Reduced hallucinations by using external, verifiable data
- Real-time relevance through access to the very latest information
- The agent can decide the weighting between keyword search and vector similarity itself, typically knowing if it's searching for a keyword or semantically similar content

### Implementation Approaches

Instead of doing chunk retrieval before using an LLM to answer, an agentic RAG system makes the chunk retrieval function a tool that the LLM can access. Each subquery is semantically reranked to promote the most relevant matches, with the best results combined into a unified response that an LLM can use to generate answers.