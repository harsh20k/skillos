# SkillOS — Stack validation walkthrough

Use this after a successful `terraform apply` and Bedrock smoke test (e.g. `skillos-planner`). It covers **direct Lambda invokes**, **EventBridge schedules**, and **Slack end-to-end**.

**Prerequisites**

- `[docs/DEPLOYMENT.md](DEPLOYMENT.md)` completed: secrets, `github_repo`, layer/zip built, Lambdas deployed.
- GitHub repo has `skills/active.json`, `skills/<skill-id>/skill-tree.md`, and at least one skill id you can use in examples (below uses `portrait-sketching` — replace with a real id from your repo).

---

## 1. Exercise the rest of the stack

### 1.1 Get Terraform outputs (Slack URL)

```bash
cd infra
terraform output slack_webhook_url
```

You need this URL in [§2](#2-slack-end-to-end). It looks like  
`https://<api-id>.execute-api.<region>.amazonaws.com/slack/events`.

### 1.2 `skillos-intake` (same shape as `/learn`)

Intake expects `user_id` and `message`. It uses the GitHub checkpointer; the thread id is `intake-{user_id}`.

```bash
aws lambda invoke \
  --function-name skillos-intake \
  --cli-binary-format raw-in-base64-out \
  --payload '{"user_id":"U_TEST_001","message":"I want to deepen portrait sketching fundamentals"}' \
  /tmp/intake-out.json && cat /tmp/intake-out.json
```

**Expect:** JSON with `reply` and `done` (multi-turn may return `done: false` until the graph finishes onboarding).

**Logs:** CloudWatch → `/aws/lambda/skillos-intake`.

### 1.3 `skillos-tracker` (same shape as `/done`)

Tracker expects `skill`, optional `user_id`, optional `context` (progress note).

```bash
aws lambda invoke \
  --function-name skillos-tracker \
  --cli-binary-format raw-in-base64-out \
  --payload '{"skill":"portrait-sketching","user_id":"U_TEST_001","context":"Finished shading exercise on eyes"}' \
  /tmp/tracker-out.json && cat /tmp/tracker-out.json
```

**Expect:** `{"status":"ok","note":"...","unlocked":[...]}` or `{"status":"error","message":"..."}` if the skill is missing or validation fails.

**Logs:** `/aws/lambda/skillos-tracker`.

### 1.4 `skillos-skip-detector` and EventBridge

**Scheduled runs** (see `[infra/eventbridge.tf](../infra/eventbridge.tf)`):


| Rule                          | Schedule (UTC) | Target                  |
| ----------------------------- | -------------- | ----------------------- |
| `skillos-planner-08-00`       | `08:00` daily  | `skillos-planner`       |
| `skillos-skip-detector-23-00` | `23:00` daily  | `skillos-skip-detector` |


**Manual invoke** (skip detector accepts any payload; often `{}`):

```bash
aws lambda invoke \
  --function-name skillos-skip-detector \
  --cli-binary-format raw-in-base64-out \
  --payload '{}' \
  /tmp/skip-out.json && cat /tmp/skip-out.json
```

**Expect:** `{"status":"ok","skipped":[...]}` listing skills that had rollover/skip logic applied (may be empty).

**Verify rules exist:**

```bash
aws events list-rules --name-prefix skillos-
```

**Logs:** `/aws/lambda/skillos-skip-detector`.

---

## 2. Slack end-to-end

### 2.1 Point Slack at the API

1. Open [api.slack.com](https://api.slack.com/apps) → your SkillOS app.
2. **Slash Commands** → for **each** command (`/learn`, `/done`, `/skip`, `/harder`, `/easier`, `/skills`), set **Request URL** to the Terraform output **exactly**:
  - `https://...amazonaws.com/slack/events`  
   (same URL for every command; path must be `/slack/events`, method POST — see `[infra/api_gateway.tf](../infra/api_gateway.tf)`.)
3. **OAuth & Permissions** → install the app to your workspace if needed.
4. Secrets `**skillos/slack-bot-token`** and `**skillos/slack-signing-secret`** must match the app. After changing secrets, run `terraform apply` again so `skillos-slack-bot` picks up env vars (or update Lambda env manually).

### 2.2 Smoke tests

Run in Slack (see `[slack/bot.py](../slack/bot.py)`):


| Command              | What it exercises                                            |
| -------------------- | ------------------------------------------------------------ |
| `/skills`            | Reads `active.json` + state; no Bedrock required for listing |
| `/learn …`           | → `skillos-intake` (Bedrock + GitHub checkpointer)           |
| `/done …`            | → `skillos-tracker` (Bedrock + GitHub writes)                |
| `/skip …`            | S3 `skip_state.json` via slack-bot role                      |
| `/harder`, `/easier` | GitHub writes to `active.json`                               |


Suggested order:

1. `/skills` — confirms bot + signing + GitHub read path.
2. `/learn I want to practice …` — confirms Intake + Bedrock.
3. `/done <skill-id> optional note` — confirms Tracker (use a skill id from `/skills` or `active.json`).

### 2.3 If Slack fails


| Symptom                        | Likely cause                                                                |
| ------------------------------ | --------------------------------------------------------------------------- |
| `invalid_signature` / 401      | Wrong signing secret or Request URL mismatch (trailing slash, wrong stage). |
| 403 / timeout from API Gateway | Wrong route; must be `POST /slack/events`.                                  |
| Bot silent but API 200         | Check `/aws/lambda/skillos-slack-bot` logs; downstream Lambda errors.       |
| Intake/Tracker errors          | Same as §1 — CloudWatch on `skillos-intake` / `skillos-tracker`.            |


More: [DEPLOYMENT.md](DEPLOYMENT.md) troubleshooting table.

---

## 3. Done criteria

- Intake and Tracker succeed via **CLI** or **Slack** for a real skill in your repo.
- Skip detector runs manually and scheduled rules exist in EventBridge.
- Slack slash commands all use the **same** `slack_webhook_url` and return sensible responses.

Cross-account Bedrock: [BEDROCK_CROSS_ACCOUNT_RUNBOOK.md](BEDROCK_CROSS_ACCOUNT_RUNBOOK.md).