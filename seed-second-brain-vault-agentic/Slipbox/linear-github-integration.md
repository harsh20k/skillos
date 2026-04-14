---
date: 2026-04-10
tags: [linear, git, workflow, project-management]
---

# Linear ↔ GitHub Integration

How Linear connects to GitHub to automatically track work — without manual status updates.

---

## The Core Idea

Your Git activity (branches, commits, PRs) drives Linear issue status automatically. You work in GitHub; Linear updates itself.

---

## How It Links

**Via branch name:**
```
feature/LIN-123-add-bedrock-agent
```
→ Linear detects `LIN-123` and links the branch to that issue.

**Via commit message (solo workflow):**
```bash
git commit -m "feat: add bedrock agent (closes LIN-123)"
```
→ `closes` / `fixes` / `resolves` / `implements` mark the issue as Done.

**Via PR title or description:**
```
fix: resolve cold start issue (fixes LIN-45)
```
→ PR gets linked; issue moves through statuses automatically.

---

## Auto Status Flow (with branches + PRs)

```
Create branch    → issue moves to In Progress
Open PR          → issue moves to In Review
Merge PR         → issue moves to Done
```

For solo/direct-to-main commits, only the final step (Done) triggers automatically via magic words.

---

## Setup (one-time, admin only)

1. Go to Linear Settings → Integrations → GitHub
2. Authenticate and select repos to connect
3. Enable PR linking and commit linking separately
4. Team members can then configure personal git automations

---

## GitHub Copilot Agent (bonus)

You can assign a Linear issue directly to GitHub Copilot:
- Copilot opens a draft PR, works independently, streams progress to Linear
- Requests your review when done
- Good for: bug fixes, refactors, docs

---

## Related Notes
- [[git-branch-naming-and-commit-conventions]]
- [[Git Commands for Noobs]]
