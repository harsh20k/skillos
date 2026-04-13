# SkillOS — Deploy (AWS + Terraform)

**Stack:** 5 Lambdas (Python 3.12), EventBridge (Planner08:00 UTC, Skip 23:00 UTC), HTTP API `POST /slack/events` → Slack bot, S3 `skip_state`, Bedrock LLM, Secrets Manager. Code: [`infra/`](../infra/).

## Before you apply

1. **Terraform state bucket** (must exist; not created by this repo): default `skillos-terraform-state` in `us-east-1` — see `backend` in [`infra/main.tf`](../infra/main.tf).  
   `aws s3api create-bucket --bucket skillos-terraform-state --region us-east-1` + enable versioning.

2. **Secrets** (same region as deploy) — names in [`infra/secrets.tf`](../infra/secrets.tf):

   - `skillos/github-token` — PAT, `repo` read/write  
   - `skillos/slack-bot-token` — `xoxb-...`  
   - `skillos/slack-signing-secret`  
   - `skillos/langchain-api-key` — LangSmith (or placeholder)

   Terraform injects these into Lambda **env**; values end up in **tfstate** — lock down the state bucket.

3. **Bedrock:** enable model for `var.bedrock_model_id` (default Haiku in `main.tf`) in that region.

4. **Lambda deps:** `lambdas.tf` zips source only. Bundle deps before a working deploy: e.g. `pip install -r requirements.txt -t python/` as a **layer**, or install into a folder included in the zip, or use a **container** image.

5. **`infra/terraform.tfvars`** (no secrets in git):

   ```hcl
   github_repo = "owner/repo"   # required
   # aws_region, github_branch, s3_state_bucket, bedrock_model_id — optional overrides
   ```

## Deploy

```bash
cd infra
terraform init
terraform apply -var-file=terraform.tfvars
```

Use output **`slack_webhook_url`** as the **Request URL** for Slack slash commands `/learn`, `/done`, `/skip`, `/harder`, `/easier`, `/skills` (see [`slack/bot.py`](../slack/bot.py)).

## Slack

Create app at api.slack.com → Slash Commands → same URL for each command (ends with `/slack/events`). Install app → put token + signing secret in Secrets Manager → `terraform apply` (or update secret + redeploy if env is stale).

## GitHub repo (`github_repo`)

Expects `skills/active.json`, `skills/<name>/skill-tree.md`, `progress.md`, `daily/`, optional `notes/`.

## Quick checks

CloudWatch → `skillos-*` log groups. Test Planner Lambda with `{}`. Slack: `/skills`, `/learn …`.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| ImportError on Lambda | Add layer / bundle `requirements.txt`. |
| Bedrock denied | Model access + region. |
| GitHub 401/403 | PAT + `GITHUB_REPO`. |
| Slack signature | Signing secret + exact webhook URL. |
| Secret not found | Create secrets before apply. |
| Backend error | State bucket missing / wrong region. |

More: [ADR-001](adr/001-langgraph-orchestration.md), [README](../README.md).
