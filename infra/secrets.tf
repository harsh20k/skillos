# Secrets are created manually in AWS Secrets Manager before running terraform apply.
# Naming convention: skillos/<key>
#
# Required secrets:
#   skillos/github-token         — GitHub personal access token (repo read/write)
#   skillos/slack-bot-token      — Slack bot OAuth token (xoxb-...)
#   skillos/slack-signing-secret — Slack app signing secret
#   skillos/langchain-api-key    — LangSmith API key (for tracing)

data "aws_secretsmanager_secret" "github_token" {
  name = "skillos/github-token"
}

data "aws_secretsmanager_secret_version" "github_token" {
  secret_id = data.aws_secretsmanager_secret.github_token.id
}

data "aws_secretsmanager_secret" "slack_bot_token" {
  name = "skillos/slack-bot-token"
}

data "aws_secretsmanager_secret_version" "slack_bot_token" {
  secret_id = data.aws_secretsmanager_secret.slack_bot_token.id
}

data "aws_secretsmanager_secret" "slack_signing_secret" {
  name = "skillos/slack-signing-secret"
}

data "aws_secretsmanager_secret_version" "slack_signing_secret" {
  secret_id = data.aws_secretsmanager_secret.slack_signing_secret.id
}

data "aws_secretsmanager_secret" "langchain_api_key" {
  name = "skillos/langchain-api-key"
}

data "aws_secretsmanager_secret_version" "langchain_api_key" {
  secret_id = data.aws_secretsmanager_secret.langchain_api_key.id
}
