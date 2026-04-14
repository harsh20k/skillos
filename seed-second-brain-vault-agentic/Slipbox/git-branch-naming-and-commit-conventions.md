---
date: 2026-04-10
tags: [git, conventions, workflow, linear]
---

# Git Branch Naming & Commit Conventions

Branch naming and commit message conventions that keep your Git history clean and professional — and integrate with Linear for automatic issue tracking.

---

## Branch Naming Format

```
type/LIN-ID-short-description
```

**Examples:**
```
feature/LIN-123-add-bedrock-agent
bugfix/LIN-45-fix-dynamodb-query
hotfix/LIN-89-patch-lambda-timeout
chore/LIN-67-update-terraform-vars
docs/LIN-10-add-readme-setup
test/LIN-55-add-rag-pipeline-tests
```

### Type Prefixes

| Prefix | Use for |
|--------|---------|
| `feature/` | New functionality |
| `bugfix/` | Fixing a bug |
| `hotfix/` | Urgent production fix |
| `chore/` | Cleanup, refactor, config |
| `docs/` | Documentation only |
| `test/` | Adding or fixing tests |

### Rules
- No spaces or special characters
- Keep slug under ~50 chars total
- Be descriptive: `fix-login-validation` not `fixes`
- Stay consistent — pick a format and never deviate

---

## Commit Message Format (Conventional Commits)

```
type: short description (LIN-ID)
```

**Examples:**
```bash
git commit -m "feat: add Bedrock agent integration (LIN-123)"
git commit -m "fix: resolve DynamoDB cold start issue (LIN-45)"
git commit -m "hotfix: patch Lambda timeout in prod (LIN-89)"
git commit -m "chore: update Terraform variables (LIN-67)"
git commit -m "docs: add README setup instructions (LIN-10)"
git commit -m "test: add unit tests for RAG pipeline (LIN-55)"
```

### Branch → Commit Mapping

| Branch prefix | Commit prefix |
|--------------|---------------|
| `feature/` | `feat:` |
| `bugfix/` | `fix:` |
| `hotfix/` | `hotfix:` |
| `chore/` | `chore:` |
| `docs/` | `docs:` |
| `test/` | `test:` |

---

## Linear Integration via Magic Words

When committing directly to main (solo workflow), use magic words to auto-update Linear issues:

```bash
git commit -m "fix: resolve login validation (closes LIN-123)"
# closes / fixes / resolves → marks issue as Done automatically
```

Without magic words → commit links to the issue but status stays manual.

---

## PR (Pull Request) — What It Is

A PR is a request to merge your feature branch into `main`. It enables:
- Code review before changes hit main
- CI/CD tests run automatically
- Discussion on the change
- Auto-status updates in Linear (In Progress → In Review → Done)

For solo work, you can still open PRs and merge yourself — keeps history clean and signals good habits.

---

## Related Notes
- [[git-commands-for-noobs]]
