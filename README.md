# SkillOS

> *"Tell me what you want to learn. I'll build the path, send you today's tasks, and track every step."*

SkillOS is a proof-of-concept multi-agent AI system that turns any learning goal into a structured, daily-action plan — tracked entirely in GitHub markdown and delivered via Slack. Inspired by **Scottie**, the Nova Scotia government's conversational AI chatbot, SkillOS demonstrates how agentic AI can be applied to personal knowledge development with real guardrails, versioned state, and composable AWS infrastructure.

---

## How it works

1. **User states a goal** — e.g. "I want to learn portrait sketching"
2. **Intake Agent** reads the user's GitHub knowledge base (existing notes), assesses current skill level via 2–3 questions, and confirms scope
3. **Planner Agent** generates a skill tree (DAG with unlock conditions) and produces today's 3–5 concrete, time-boxed tasks — no vague ideas, only actionable items
4. **Slack Bot** delivers the daily brief at 08:00 with tasks, badges, and slash commands
5. **Skip Detector** runs at 23:00 — if no progress was committed, it flags the day and prepares a rollover (max 2 tasks carried forward, with encouragement — no shame language)
6. **Tracker Agent** fires on `/done` — writes progress markdown, updates the skill tree node statuses, and commits + pushes to GitHub

---

## Agent design

| Agent | Trigger | LLM Call | Guardrail |
|---|---|---|---|
| Intake Agent | User message / onboarding | Yes — goal scoping | Rejects vague goals |
| Planner Agent | EventBridge 08:00 | Yes — task generation | No task > 30 min |
| Skip Detector | EventBridge 23:00 | No — pure logic | Caps rollover at 2 tasks |
| Tracker Agent | Slack `/done` | Yes — progress note + node unlock | Dry-run diff before commit |

Each agent runs as its own **stateless Lambda function**. Context is reconstructed fresh from GitHub + S3 on every invocation — no persistent agent process in memory.

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
- **Secrets Manager** — GitHub token, Slack bot token
- **GitHub** — primary memory and versioned state store
- **Terraform** — infrastructure as code

---

## GitHub repo structure (runtime)

```
/skills/{skill-name}/
  skill-tree.md          # skill DAG with node unlock conditions
  progress.md            # running log updated by Tracker Agent
  daily/
    YYYY-MM-DD.md        # per-day tasks + completion status
/notes/                  # user's knowledge base (read-only by Intake Agent)
```

---

## Slack commands

| Command | Action |
|---|---|
| `/done` | Triggers Tracker Lambda, commits progress, unlocks nodes |
| `/skip` | Explicit skip, sets rollover flag early |
| `/harder` | Signals Planner to increase next day's difficulty |
| `/easier` | Signals Planner to reduce difficulty |

---

## Skip & rollover logic

- Skip Detector fires at 23:00 and checks if any `progress:` commit exists for today
- If not, writes `skip_state.json` to S3 with the list of incomplete tasks
- Planner reads this at 08:00 and carries forward a max of **2 tasks** (most important ones)
- Encouragement tone is enforced at the prompt level — no streak counters, no guilt language

---

## Key design decisions

- **GitHub as the memory layer** — every state change is a commit. Fully auditable, inspectable, and human-readable without any dashboard
- **Stateless Lambdas** — context reconstructed fresh on every invocation. Makes debugging trivial and removes cold-state bugs
- **Slack as the UI** — zero friction. Slash commands map directly to agent triggers
- **Guardrails as named components** — each agent has explicit enforcement logic, not just a prompt instruction
- **Loose coupling via shared memory** — agents communicate through GitHub/S3 state, not direct calls

---

## Tech stack

- Python 3.12 (Lambda runtime)
- Anthropic SDK (Claude Sonnet)
- PyGithub (GitHub REST API)
- Slack Bolt SDK
- Terraform
- AWS: Lambda · EventBridge · API Gateway · S3 · Secrets Manager

---

## Project status

Proof of concept — not production ready. Built to demonstrate multi-agent architecture depth, guardrail design, and AWS serverless deployment patterns.

---

## Repo structure

```
skillos/
├── agents/
│   ├── intake/
│   │   ├── handler.py       # Lambda handler
│   │   ├── prompt.py        # system prompt + guardrail
│   │   └── github_reader.py # reads notes/ from GitHub
│   ├── planner/
│   │   ├── handler.py
│   │   ├── prompt.py
│   │   └── skill_tree.py    # DAG logic + node unlock
│   ├── skip_detector/
│   │   ├── handler.py
│   │   └── rollover.py      # rollover capping logic
│   └── tracker/
│       ├── handler.py
│       ├── prompt.py
│       └── github_writer.py # commit + push logic
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
├── requirements.txt
└── README.md
```
