# SkillOS

> *"Tell me what you want to learn. I'll build the path, send you today's tasks, and track every step."*

SkillOS is a proof-of-concept multi-agent AI system that turns any learning goal into a structured, daily-action plan — tracked entirely in GitHub markdown and delivered via Slack. Inspired by **Scottie**, the Nova Scotia government's conversational AI chatbot, SkillOS demonstrates how agentic AI can be applied to personal knowledge development with real guardrails, versioned state, and composable AWS infrastructure.

Agents are orchestrated using **LangGraph** (supervisor + subgraph pattern), with **Claude 3.5 Sonnet via Amazon Bedrock** as the LLM, and **LangSmith** for agent observability.

---

## How it works

1. **User states one or more goals** — e.g. "I want to learn portrait sketching and public speaking"
2. **Intake Agent** reads the user's GitHub knowledge base (existing notes), assesses current skill level via 2–3 questions per goal, and confirms scope — each goal becomes an independent skill tree
3. **Planner Agent** generates a skill tree (DAG with unlock conditions) per active skill and produces today's 3–5 concrete, time-boxed tasks *total across all skills* — budget is distributed proportionally, not multiplied per skill
4. **Slack Bot** delivers the daily brief at 08:00 with tasks grouped by skill, badges, and slash commands
5. **Skip Detector** runs at 23:00 — checks progress per skill independently; a skip in one skill does not penalise rollover for another (max 2 tasks carried forward *per skill*)
6. **Tracker Agent** fires on `/done <skill>` — writes progress markdown to the correct skill directory, updates that skill tree's node statuses, and commits + pushes to GitHub

---

## Agent design


| Agent         | Trigger                   | LLM Call                          | Guardrail                                                       |
| ------------- | ------------------------- | --------------------------------- | --------------------------------------------------------------- |
| Intake Agent  | User message / onboarding | Yes — goal scoping per skill      | Rejects vague goals; prompts one skill at a time                |
| Planner Agent | EventBridge 08:00         | Yes — cross-skill task generation | No task > 30 min; 3–5 tasks total across all active skills      |
| Skip Detector | EventBridge 23:00         | No — pure logic                   | Caps rollover at 2 tasks *per skill*, evaluated independently   |
| Tracker Agent | Slack `/done <skill>`     | Yes — progress note + node unlock | Dry-run diff before commit; errors if skill name not recognised |


Each agent runs as its own **stateless Lambda function**. Context is reconstructed fresh from GitHub + S3 on every invocation — no persistent agent process in memory.

---

## Orchestration architecture

SkillOS uses a **LangGraph multi-agent supervisor** pattern:

```
SupervisorGraph
├── IntakeSubgraph     (StateGraph: clarify → assess → scaffold)
├── PlannerSubgraph    (StateGraph: read_state → generate → write_tasks)
├── SkipDetectorNode   (pure logic node, no LLM)
└── TrackerSubgraph    (StateGraph: validate → generate_note → commit)
```

- Each subgraph is a `StateGraph` with typed state (`TypedDict`) and tool-calling nodes
- The supervisor routes based on the incoming trigger (EventBridge event type or Slack command)
- A **custom LangGraph checkpointer** persists graph state to GitHub commits — every state transition is a versioned, human-readable commit
- **LangSmith** traces every agent run for full observability (token usage, node timing, tool calls)

---

## AWS Infrastructure

```
EventBridge (08:00) ──→ Planner Lambda
EventBridge (23:00) ──→ Skip Detector Lambda
API Gateway          ──→ Tracker Lambda  ←── Slack /done
                              │
                    S3 (skip_state.json)
                    GitHub (skill-tree · daily/ · progress.md)
```

- **Lambda** — Python 3.12, one function per agent
- **EventBridge** — cron rules at 08:00 and 23:00
- **API Gateway** — receives Slack slash commands
- **S3** — ephemeral state (skip flags, session cache)
- **Secrets Manager** — GitHub token, Slack bot token, LangSmith API key
- **Bedrock** — Claude 3.5 Sonnet, IAM-authenticated (no hardcoded API keys)
- **GitHub** — primary memory and versioned state store
- **Terraform** — infrastructure as code

---

## GitHub repo structure (runtime)

```
/skills/
  active.json            # list of active skill names + metadata (start date, difficulty)
  {skill-name}/          # one directory per active skill, e.g. portrait, public-speaking
    skill-tree.md        # skill DAG with node unlock conditions
    progress.md          # running log updated by Tracker Agent
    daily/
      YYYY-MM-DD.md      # per-day tasks + completion status (cross-skill tasks marked with skill tag)
/notes/                  # user's knowledge base (read-only by Intake Agent)
```

---

## Slack commands


| Command           | Action                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| `/done <skill>`   | Triggers Tracker Lambda for the named skill, commits progress, unlocks nodes — e.g. `/done portrait` |
| `/skip <skill>`   | Explicit skip for a specific skill, sets rollover flag early — e.g. `/skip public-speaking`          |
| `/harder <skill>` | Signals Planner to increase next day's difficulty for that skill                                     |
| `/easier <skill>` | Signals Planner to reduce difficulty for that skill                                                  |
| `/skills`         | Lists all active skills and today's task count per skill                                             |


---

## Skip & rollover logic

- Skip Detector fires at 23:00 and checks each active skill independently for a `progress:` commit
- For each skill with no progress, it writes a per-skill entry into `skip_state.json` on S3
- Planner reads this at 08:00 and carries forward a max of **2 tasks per skipped skill** (most important ones), then re-balances the total daily budget across all active skills
- A skip in one skill never blocks or penalises another skill's tasks
- Encouragement tone is enforced at the prompt level — no streak counters, no guilt language

---

## Key design decisions

- **LangGraph supervisor + subgraphs** — industry-standard multi-agent orchestration; explicit state machines over ad-hoc prompt chaining ([ADR-001](docs/adr/001-langgraph-orchestration.md))
- **Claude via Bedrock** — IAM-authenticated, no hardcoded API keys; keeps all infra AWS-native
- **Custom GitHub checkpointer** — LangGraph state persisted as GitHub commits; every state transition is auditable and human-readable without any dashboard
- **LangSmith observability** — traces every agent run; token usage, node timing, and tool calls visible without custom logging
- **Stateless Lambdas** — context reconstructed fresh on every invocation; makes debugging trivial and removes cold-state bugs
- **Slack as the UI** — zero friction; slash commands map directly to agent triggers
- **Guardrails as named components** — each agent has explicit enforcement logic, not just a prompt instruction
- **Loose coupling via shared memory** — agents communicate through GitHub/S3 state, not direct calls

---

## Tech stack

- Python 3.12 (Lambda runtime)
- LangGraph (multi-agent orchestration, supervisor pattern)
- LangChain Anthropic / Bedrock (Claude 3.5 Sonnet)
- LangSmith (agent observability + tracing)
- PyGithub (GitHub REST API)
- Slack Bolt SDK
- Terraform
- AWS: Lambda · EventBridge · API Gateway · S3 · Secrets Manager · Bedrock

---

## Project status

Proof of concept — not production ready. Built to demonstrate multi-agent architecture depth, guardrail design, LangGraph orchestration patterns, and AWS serverless deployment.

---

## Repo structure

```
skillos/
├── agents/
│   ├── intake/
│   │   ├── handler.py       # Lambda handler + LangGraph subgraph entry
│   │   ├── graph.py         # IntakeSubgraph StateGraph definition
│   │   ├── prompt.py        # system prompt + guardrail
│   │   └── github_reader.py # reads notes/ from GitHub
│   ├── planner/
│   │   ├── handler.py
│   │   ├── graph.py         # PlannerSubgraph StateGraph definition
│   │   ├── prompt.py
│   │   └── skill_tree.py    # DAG logic + node unlock
│   ├── skip_detector/
│   │   ├── handler.py
│   │   └── rollover.py      # rollover capping logic (no LLM)
│   └── tracker/
│       ├── handler.py
│       ├── graph.py         # TrackerSubgraph StateGraph definition
│       ├── prompt.py
│       └── github_writer.py # commit + push logic
├── supervisor/
│   └── graph.py             # SupervisorGraph — routes to subgraphs
├── checkpointer/
│   └── github_checkpointer.py  # custom LangGraph checkpointer backed by GitHub
├── slack/
│   └── bot.py               # Slack Bolt app, slash command routing
├── infra/
│   ├── main.tf
│   ├── lambdas.tf
│   ├── eventbridge.tf
│   ├── api_gateway.tf
│   └── secrets.tf
├── shared/
│   └── github_client.py     # shared GitHub API client
├── docs/
│   └── adr/
│       └── 001-langgraph-orchestration.md
├── requirements.txt
└── README.md
```

