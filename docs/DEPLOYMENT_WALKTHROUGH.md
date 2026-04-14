# SkillOS Deployment Walkthrough (From Current State)

This guide picks up from where you are now and walks through the remaining deployment steps in order.

## 0) Preconditions

- You are in repo root: `skillos/`
- Docker is running
- You can use AWS profile with create permissions (recommended: `tf_provisioner_janakfoto`)
- You have a GitHub fine-grained PAT for the **data repo** with:
  - Contents: Read and write
  - Metadata: Read-only

## 1) Build Lambda dependency layer

From repo root:

```bash
./scripts/build_lambda_layer.sh
```

Expected result: `infra/layer-build/python/` populated.

## 2) Create a new Terraform state bucket (unique name)

If `skillos-terraform-state` is stuck in `OperationAborted`, use a unique bucket:

```bash
aws s3api create-bucket \
  --bucket skillos-terraform-state-965384155969 \
  --region us-east-1 \
  --profile tf_provisioner_janakfoto

aws s3api put-bucket-versioning \
  --bucket skillos-terraform-state-965384155969 \
  --versioning-configuration Status=Enabled \
  --region us-east-1 \
  --profile tf_provisioner_janakfoto
```

## 3) Update Terraform backend bucket

In `infra/main.tf`, set the backend bucket to the new unique bucket:

```hcl
backend "s3" {
  bucket = "skillos-terraform-state-965384155969"
  key    = "skillos/terraform.tfstate"
  region = "us-east-1"
}
```

Then reinitialize backend:

```bash
cd infra
terraform init -reconfigure
cd ..
```

## 4) Create Secrets Manager secrets

Create these 4 secrets in `us-east-1` (same region as deploy):

```bash
aws secretsmanager create-secret \
  --name skillos/github-token \
  --secret-string 'YOUR_GITHUB_PAT' \
  --region us-east-1 \
  --profile tf_provisioner_janakfoto

aws secretsmanager create-secret \
  --name skillos/slack-bot-token \
  --secret-string 'xoxb-...' \
  --region us-east-1 \
  --profile tf_provisioner_janakfoto

aws secretsmanager create-secret \
  --name skillos/slack-signing-secret \
  --secret-string 'YOUR_SLACK_SIGNING_SECRET' \
  --region us-east-1 \
  --profile tf_provisioner_janakfoto

aws secretsmanager create-secret \
  --name skillos/langsmith-api-key \
  --secret-string 'lsv2_...' \
  --region us-east-1 \
  --profile tf_provisioner_janakfoto
```

If a secret already exists, update it:

```bash
aws secretsmanager put-secret-value \
  --secret-id skillos/github-token \
  --secret-string 'NEW_VALUE' \
  --region us-east-1 \
  --profile tf_provisioner_janakfoto
```

## 5) Set `infra/terraform.tfvars`

Create `infra/terraform.tfvars` with at least:

```hcl
github_repo = "OWNER/YOUR_SKILLOS_DATA_REPO"
```

Notes:

- `github_repo` is the **knowledge/skills repo** (not necessarily this code repo).
- Do not put secret values in tfvars.

## 6) Seed the GitHub data repo structure

Your `github_repo` must contain:

```text
skills/
  active.json
  <skill-name>/
    skill-tree.md
    progress.md
    daily/
notes/   # optional
```

Minimum `skills/active.json`:

```json
[
  {
    "name": "portrait-sketching",
    "display_name": "Portrait Sketching",
    "difficulty": "beginner"
  }
]
```

## 7) Terraform deploy

From `infra/`:

```bash
terraform init -reconfigure
terraform plan -var-file=terraform.tfvars
terraform apply -var-file=terraform.tfvars
```

Capture output:

- `slack_webhook_url`
[https://wf4wtgp1k9.execute-api.us-east-1.amazonaws.com//slack/events](https://wf4wtgp1k9.execute-api.us-east-1.amazonaws.com//slack/events)

## 8) Slack wiring

In Slack App config:

1. Create slash commands:
  - `/learn`
  - `/done`
  - `/skip`
  - `/harder`
  - `/easier`
  - `/skills`
2. Set each Request URL to:
  - `<slack_webhook_url>/slack/events` (Terraform output already includes `/slack/events`; use exactly output value)
3. Install/reinstall app to workspace if needed.

## 9) Smoke tests

1. Lambda console:
  - invoke `skillos-planner` with `{}`
  - invoke `skillos-skip-detector` with `{}`
2. Slack:
  - `/skills`
  - `/learn I want to learn portrait sketching`
3. CloudWatch:
  - check `/aws/lambda/skillos-*` logs for runtime errors

## 10) Common failures and fixes

- **Import errors in Lambda**
  - Re-run `./scripts/build_lambda_layer.sh`, then `terraform apply` again.
- **Secret not found**
  - Verify names exactly match `infra/secrets.tf`.
- **GitHub 401/403**
  - Check PAT validity + repo permissions + `github_repo` value.
- **Slack signature/token errors**
  - Rotate and update Slack secrets, then re-apply.
- **Backend init issues**
  - Ensure bucket exists and backend bucket name in `infra/main.tf` matches exactly.

