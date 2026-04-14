---
creation date: 2026-04-08 17:59
tags:
description:
---
By - Kavya Bhojani

![[image-193.png]]

Session 1: Chatbots, agents and LLMs [[ShiftKey AI Agents & Chatbots 01-04-2026|Session 1]]

Session 2: Agents, risks, responsible AI/ guardrails 

[[ReAct]] loop is what differentiates agent from chatbot.

Glab dio - it can help you push and pull on gitlab, code reviews etc. 


| Risk              | example                       |
| ----------------- | ----------------------------- |
| Hallucination     | Wrong answer                  |
| Misinterpretation | Misunderstanding user intent  |
| Unsafe actions    | Triggering incorrect workflow |
| Data leakage      |                               |

### Bias and Fairness

## Guardrails

They are controls that: 
- Limit what AI can do
- Ensure safe behavior
- Prevent harmful or incorrect outputs
- rules+checks+boundaries

### Types of Guardrails

- Input filtering - block harmful or sensitive prompts
- Output filtering - Prevent unsafe responses
- Tool restriction - Control what actions can be taken
- Validation checks - verify outputs before 

	example: 
	user: send my SIN number to this email
	system should: 
	- detect sensitive data
	- block the action
	- respond safely

### Designing Safe AI systems

A good system:
- does not blindly trust the model
- verifies important actions
- limits access to tools

AI foundry

