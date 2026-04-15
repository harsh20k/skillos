# SkillOS Runbook: Cross-Account Bedrock

Target setup:

- **Account A**: owns Bedrock model access and pays for model invocations.
- **Account B**: hosts all SkillOS infrastructure (Lambda, API Gateway, EventBridge, S3, Secrets).

This runbook configures SkillOS Lambdas in Account B to assume a role in Account A before invoking Bedrock.

## Architecture

1. Lambda executes in Account B with its normal execution role.
2. Lambda calls `sts:AssumeRole` to a Bedrock access role in Account A.
3. Lambda creates a Bedrock Runtime client with temporary credentials from Account A.
4. Bedrock invocation runs in Account A region/model permissions and is billed to Account A.

## Prerequisites

- Bedrock model access is enabled in Account A for the target region.
- You know:
  - `ACCOUNT_A_ID`
  - `ACCOUNT_B_ID`
  - Bedrock region (example: `us-east-1`)
  - External ID string for trust hardening (example: `skillos-bedrock-xacct-2026`)

### CLI setup assumptions

This runbook uses AWS CLI named profiles:

- `account-a` -> authenticated to Account A
- `account-b` -> authenticated to Account B

Set reusable shell vars:

```bash
export ACCOUNT_A_ID="411960113601"
export ACCOUNT_B_ID="965384155969"
export AWS_REGION="us-east-1"
export BEDROCK_ROLE_NAME="SkillosBedrockFromAccountBRole"
export LAMBDA_EXEC_ROLE_NAME="skillos-lambda-exec"
export EXTERNAL_ID="skillos-bedrock-xacct-2026"
```

## Step 1: Create Bedrock access role in Account A

Create IAM role in Account A (example name: `SkillosBedrockFromAccountBRole`) with this trust policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<ACCOUNT_B_ID>:role/skillos-lambda-exec"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "skillos-bedrock-xacct-2026"
        }
      }
    }
  ]
}
```

Attach this permissions policy to the same role in Account A:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/*",
        "arn:aws:bedrock:*:*:inference-profile/*"
      ]
    }
  ]
}
```

Notes:

- Tighten resources to specific model/inference-profile ARNs after first successful test.
- If your organization uses SCPs, verify Account A allows Bedrock and STS.

### CLI (Account A)

Create trust policy file:

```bash
cat > /tmp/skillos-bedrock-trust-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::${ACCOUNT_B_ID}:role/${LAMBDA_EXEC_ROLE_NAME}"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "${EXTERNAL_ID}"
        }
      }
    }
  ]
}
EOF
```

Create role in Account A:

```bash
aws --profile account-a iam create-role \
  --role-name "${BEDROCK_ROLE_NAME}" \
  --assume-role-policy-document file:///tmp/skillos-bedrock-trust-policy.json
```

Create permission policy file:

```bash
cat > /tmp/skillos-bedrock-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/*",
        "arn:aws:bedrock:*:*:inference-profile/*"
      ]
    }
  ]
}
EOF
```

Attach inline policy to role:

```bash
aws --profile account-a iam put-role-policy \
  --role-name "${BEDROCK_ROLE_NAME}" \
  --policy-name "SkillosBedrockInvokePolicy" \
  --policy-document file:///tmp/skillos-bedrock-policy.json
```

## Step 2: Grant AssumeRole permission in Account B

In Account B, update Lambda execution role policy (`skillos-lambda-exec`) to allow assuming Account A role:

```json
{
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": "arn:aws:iam::<ACCOUNT_A_ID>:role/SkillosBedrockFromAccountBRole"
}
```

For this repository, add the statement in `infra/lambdas.tf` under `aws_iam_role_policy.lambda_policy`.

### CLI (Account B)

Create inline policy doc for Lambda execution role:

```bash
cat > /tmp/skillos-assume-account-a-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::${ACCOUNT_A_ID}:role/${BEDROCK_ROLE_NAME}"
    }
  ]
}
EOF
```

Attach it to Account B Lambda role:

```bash
aws --profile account-b iam put-role-policy \
  --role-name "${LAMBDA_EXEC_ROLE_NAME}" \
  --policy-name "SkillosAssumeAccountABedrockRole" \
  --policy-document file:///tmp/skillos-assume-account-a-policy.json
```

## Step 3: Add cross-account env vars in Terraform (Account B stack)

Add these env vars to `local.common_env` in `infra/lambdas.tf`:

- `BEDROCK_ASSUME_ROLE_ARN=arn:aws:iam::<ACCOUNT_A_ID>:role/SkillosBedrockFromAccountBRole`
- `BEDROCK_ASSUME_ROLE_EXTERNAL_ID=skillos-bedrock-xacct-2026`
- `BEDROCK_ASSUME_ROLE_SESSION_NAME=skillos-bedrock-session`

Optional but recommended:

- `BEDROCK_REGION=us-east-1` (if Bedrock region differs from `AWS_REGION` used for infra)

### CLI option (no Terraform change, immediate runtime update)

If you need a fast manual test before code/terraform updates, update Lambda env directly:

```bash
aws --profile account-b lambda get-function-configuration \
  --function-name skillos-intake \
  --query 'Environment.Variables' > /tmp/skillos-intake-env.json
```

Merge required vars into that JSON and apply:

```bash
aws --profile account-b lambda update-function-configuration \
  --function-name skillos-intake \
  --environment "Variables={BEDROCK_ASSUME_ROLE_ARN=arn:aws:iam::${ACCOUNT_A_ID}:role/${BEDROCK_ROLE_NAME},BEDROCK_ASSUME_ROLE_EXTERNAL_ID=${EXTERNAL_ID},BEDROCK_ASSUME_ROLE_SESSION_NAME=skillos-bedrock-session,BEDROCK_REGION=${AWS_REGION}}"
```

For permanent configuration, use Terraform as the source of truth.

## Step 4: Update app Bedrock client creation

Current Bedrock client path is in `shared/llm.py` using `ChatBedrock`.
Implement this flow in code:

1. If `BEDROCK_ASSUME_ROLE_ARN` is set:
  - Call STS `AssumeRole` with:
    - `RoleArn` from env
    - `ExternalId` from env
    - `RoleSessionName` from env
  - Build a `boto3.Session` from temporary credentials.
  - Pass a Bedrock runtime client/session for Account A into LangChain Bedrock client.
2. Else:
  - Keep current same-account behavior.

Implementation guidance:

- Keep fallback path unchanged so local/dev can still run without cross-account config.
- Cache assumed credentials per warm Lambda container to reduce STS calls.
- Refresh credentials before expiry when cached.

## Step 5: Deploy Account B stack

Set cross-account variables in `infra/terraform.tfvars` (see `infra/terraform.tfvars.example`):

- `bedrock_assume_role_arn` — IAM role ARN in Account A (Bedrock + trust for `skillos-lambda-exec`)
- `bedrock_assume_role_external_id` — must match the trust policy `sts:ExternalId` on that role (if you use one)
- `bedrock_assume_role_session_name` — optional; default `skillos-bedrock-session`
- `bedrock_region` — optional; sets `BEDROCK_REGION` on Lambdas if Bedrock region should differ from `aws_region`

Terraform applies `sts:AssumeRole` on `skillos-lambda-exec` and merges the `BEDROCK_ASSUME_ROLE_*` env vars into all Lambdas when `bedrock_assume_role_arn` is non-empty.

From repo root:

```bash
./scripts/build_lambda_layer.sh
cd infra
terraform init
terraform apply -var-file=terraform.tfvars
```

### CLI-only IaC deployment wrapper

You can run the same deployment with explicit profile and region:

```bash
export AWS_PROFILE="account-b"
export AWS_DEFAULT_REGION="${AWS_REGION}"
./scripts/build_lambda_layer.sh
cd infra
terraform init
terraform apply -var-file=terraform.tfvars
```

## Step 6: Validate end-to-end

### Quick IAM/STSes test

**Who is calling `AssumeRole` matters.** The role in Account A must trust the **exact principal** you use in the CLI.

- **Production path:** Lambda runs as `arn:aws:iam::<ACCOUNT_B_ID>:role/skillos-lambda-exec`. Your Account A trust policy should list that role ARN (as in Step 1). After `terraform apply`, you do **not** need to manually assume that role to run SkillOS; Lambdas do it in code.
- **Manual CLI test as an IAM user** (e.g. `arn:aws:iam::965384155969:user/tf_provisioner_janakfoto`): both must be true:
  1. That user has an IAM policy allowing `sts:AssumeRole` on `arn:aws:iam::<ACCOUNT_A_ID>:role/<BEDROCK_ROLE_NAME>`.
  2. The **trust policy** on `SkillosBedrockFromAccountBRole` in Account A includes that user ARN in `Principal.AWS` (or a group of principals you use for ops). The trust policy that only allows `skillos-lambda-exec` will **reject** a human IAM user with `AccessDenied`, even if the user has `sts:AssumeRole` in their policy.

Example: add a second statement to the Account A role trust policy for break-glass testing (remove or tighten later):

```json
{
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::<ACCOUNT_B_ID>:user/tf_provisioner_janakfoto" },
  "Action": "sts:AssumeRole",
  "Condition": {
    "StringEquals": { "sts:ExternalId": "skillos-bedrock-xacct-2026" }
  }
}
```

Then ensure that user has `sts:AssumeRole` on that role ARN in Account B.

From a principal that is trusted by the role:

```bash
aws sts assume-role \
  --profile account-b \
  --role-arn arn:aws:iam::${ACCOUNT_A_ID}:role/${BEDROCK_ROLE_NAME} \
  --role-session-name skillos-manual-test \
  --external-id "${EXTERNAL_ID}"
```

If this fails, fix trust policy, caller IAM policy, role ARN, principal mismatch, or external ID mismatch.

### Direct Bedrock smoke test via CLI (cross-account)

1. Assume role and capture temporary credentials:

```bash
CREDS_JSON=$(aws --profile account-b sts assume-role \
  --role-arn arn:aws:iam::${ACCOUNT_A_ID}:role/${BEDROCK_ROLE_NAME} \
  --role-session-name skillos-bedrock-smoke \
  --external-id "${EXTERNAL_ID}")
```

1. Export temp credentials:

```bash
export AWS_ACCESS_KEY_ID=$(echo "${CREDS_JSON}" | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo "${CREDS_JSON}" | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo "${CREDS_JSON}" | jq -r '.Credentials.SessionToken')
```

1. Invoke Bedrock in Account A context:

```bash
aws --region "${AWS_REGION}" bedrock-runtime invoke-model \
  --model-id "us.anthropic.claude-3-5-haiku-20241022-v1:0" \
  --content-type "application/json" \
  --accept "application/json" \
  --body '{"anthropic_version":"bedrock-2023-05-31","max_tokens":64,"messages":[{"role":"user","content":"hello from cross-account cli test"}]}' \
  /tmp/skillos-bedrock-smoke-output.json
```

1. Inspect output:

```bash
cat /tmp/skillos-bedrock-smoke-output.json
```

If this passes, cross-account Bedrock is correctly configured.

### Runtime test in SkillOS

- Invoke `skillos-intake` test event in Account B.
- Confirm CloudWatch logs in Account B show successful Bedrock response.
- Confirm Bedrock usage/cost appears in Account A.

### IAM inline policy name

`skillos-lambda-exec` uses a **single inline policy**. If `get-role-policy --policy-name lambda_policy` returns `NoSuchEntity`, list names first:

```bash
aws iam list-role-policies --role-name skillos-lambda-exec
aws iam get-role-policy --role-name skillos-lambda-exec --policy-name <name-from-list>
```

After the next `terraform apply`, the inline policy is pinned to the name `lambda_policy` in this repo’s `infra/lambdas.tf`.

## Troubleshooting

- `AccessDeniedException` on STS assume role:
  - Missing `sts:AssumeRole` permission in Account B role policy.
  - Trust policy principal ARN in Account A does not match real caller role ARN.
  - External ID mismatch.
- `AccessDeniedException` on Bedrock invoke:
  - Account A role policy missing Bedrock actions/resources.
  - Model access not enabled in Account A for selected model/region.
  - SCP boundary denies Bedrock in Account A.
- **AWS Marketplace / model subscription** — logs may mention `aws-marketplace:ViewSubscriptions` or `Subscribe`, or “subscription cannot be completed” (common for Anthropic and similar models):
  - In **Account A** (the account whose credentials call `InvokeModel`), open **Amazon Bedrock → Model access** (or **Bedrock → Marketplace** / model catalog) and **enable or subscribe** to the exact model / inference profile you use (e.g. Claude 3.5 Haiku). Wait a few minutes after accepting terms.
  - On the **Account A** Bedrock role (`SkillosBedrockFromAccountBRole`), add IAM permission for Marketplace if your org requires it, for example:
    - `aws-marketplace:ViewSubscriptions`
    - `aws-marketplace:Subscribe`
    - (scope `Resource` per your org’s policy; some teams use `"*"` for these actions during setup, then tighten)
  - Organization **SCPs** or **permission boundaries** can block Marketplace; an admin may need to allow those actions for Account A.
- Region/model mismatch:
  - `BEDROCK_MODEL_ID` must exist in the Bedrock region used by the client.
  - Set `BEDROCK_REGION` explicitly if infra region differs.
- **Inference profile IDs vs foundation model IDs:** For many Claude 3.5+ setups, on-demand use expects an **inference profile** ID (e.g. `us.anthropic.claude-3-5-haiku-20241022-v1:0`), not only `anthropic.claude-3-5-haiku-20241022-v1:0`. If Bedrock says on-demand isn’t supported for the model ID, switch to the profile ID from the console/model catalog.
- **Cross-region routing:** Global inference profiles can route to foundation models in **another region** than your client. IAM on the **Account A** Bedrock role must allow `bedrock:InvokeModel` on `arn:aws:bedrock:*::foundation-model/*` and `arn:aws:bedrock:*:*:inference-profile/*`, not a single-region foundation-model ARN only.

## Security and operations checklist

- Use a unique `ExternalId`.
- Scope trust policy principal to exact role ARN, not whole account.
- Scope Bedrock resources to exact model/profile ARNs after validation.
- Add CloudWatch metric filters for STS and Bedrock denial errors.
- Add AWS Budget alerts in Account A (Bedrock spend owner account).
- Remove temporary shell env vars containing credentials after CLI tests:
  - `unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN`

## Suggested rollout plan

1. Enable cross-account assume role in non-prod accounts.
2. Validate one Lambda path (`skillos-intake`) first.
3. Roll out to remaining functions.
4. Tighten IAM resources from wildcard to exact model/profile ARNs.
5. Promote to prod.

