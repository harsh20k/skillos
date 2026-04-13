# ---------------------------------------------------------------------------
# Lambda source package
# ---------------------------------------------------------------------------

data "archive_file" "skillos" {
  type        = "zip"
  source_dir  = "${path.module}/.."
  output_path = "${path.module}/skillos.zip"
  excludes = [
    ".git", ".venv", "__pycache__", "*.pyc",
    "infra", "docs", "tests", ".cursor",
  ]
}

# ---------------------------------------------------------------------------
# IAM execution role (shared across all Lambdas)
# ---------------------------------------------------------------------------

resource "aws_iam_role" "lambda_exec" {
  name = "skillos-lambda-exec"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = "sts:AssumeRole"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy" "lambda_policy" {
  role = aws_iam_role.lambda_exec.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = "arn:aws:logs:*:*:*"
      },
      {
        Effect   = "Allow"
        Action   = ["s3:GetObject", "s3:PutObject"]
        Resource = "arn:aws:s3:::${var.s3_state_bucket}/*"
      },
      {
        Effect   = "Allow"
        Action   = ["secretsmanager:GetSecretValue"]
        Resource = "*"
      },
      {
        Effect   = "Allow"
        Action   = ["bedrock:InvokeModel"]
        Resource = "*"
      },
      {
        Effect   = "Allow"
        Action   = ["lambda:InvokeFunction"]
        Resource = "*"
      }
    ]
  })
}

# ---------------------------------------------------------------------------
# Common environment variables
# ---------------------------------------------------------------------------

locals {
  common_env = {
    GITHUB_REPO          = var.github_repo
    GITHUB_BRANCH        = var.github_branch
    S3_BUCKET            = var.s3_state_bucket
    AWS_REGION           = var.aws_region
    BEDROCK_MODEL_ID     = var.bedrock_model_id
    LANGCHAIN_TRACING_V2 = "true"
    LANGCHAIN_API_KEY    = data.aws_secretsmanager_secret_version.langchain_api_key.secret_string
    GITHUB_TOKEN         = data.aws_secretsmanager_secret_version.github_token.secret_string
  }
}

# ---------------------------------------------------------------------------
# Lambda functions
# ---------------------------------------------------------------------------

resource "aws_lambda_function" "intake" {
  function_name    = "skillos-intake"
  filename         = data.archive_file.skillos.output_path
  source_code_hash = data.archive_file.skillos.output_base64sha256
  handler          = "agents.intake.handler.lambda_handler"
  runtime          = "python3.12"
  role             = aws_iam_role.lambda_exec.arn
  timeout          = 60

  environment {
    variables = local.common_env
  }
}

resource "aws_lambda_function" "planner" {
  function_name    = "skillos-planner"
  filename         = data.archive_file.skillos.output_path
  source_code_hash = data.archive_file.skillos.output_base64sha256
  handler          = "agents.planner.handler.lambda_handler"
  runtime          = "python3.12"
  role             = aws_iam_role.lambda_exec.arn
  timeout          = 60

  environment {
    variables = local.common_env
  }
}

resource "aws_lambda_function" "skip_detector" {
  function_name    = "skillos-skip-detector"
  filename         = data.archive_file.skillos.output_path
  source_code_hash = data.archive_file.skillos.output_base64sha256
  handler          = "agents.skip_detector.handler.lambda_handler"
  runtime          = "python3.12"
  role             = aws_iam_role.lambda_exec.arn
  timeout          = 30

  environment {
    variables = local.common_env
  }
}

resource "aws_lambda_function" "tracker" {
  function_name    = "skillos-tracker"
  filename         = data.archive_file.skillos.output_path
  source_code_hash = data.archive_file.skillos.output_base64sha256
  handler          = "agents.tracker.handler.lambda_handler"
  runtime          = "python3.12"
  role             = aws_iam_role.lambda_exec.arn
  timeout          = 60

  environment {
    variables = local.common_env
  }
}

resource "aws_lambda_function" "slack_bot" {
  function_name    = "skillos-slack-bot"
  filename         = data.archive_file.skillos.output_path
  source_code_hash = data.archive_file.skillos.output_base64sha256
  handler          = "slack.bot.lambda_handler"
  runtime          = "python3.12"
  role             = aws_iam_role.lambda_exec.arn
  timeout          = 30

  environment {
    variables = merge(local.common_env, {
      SLACK_BOT_TOKEN      = data.aws_secretsmanager_secret_version.slack_bot_token.secret_string
      SLACK_SIGNING_SECRET = data.aws_secretsmanager_secret_version.slack_signing_secret.secret_string
      INTAKE_LAMBDA_NAME   = aws_lambda_function.intake.function_name
      TRACKER_LAMBDA_NAME  = aws_lambda_function.tracker.function_name
    })
  }
}

# ---------------------------------------------------------------------------
# Outputs
# ---------------------------------------------------------------------------

output "intake_lambda_name"       { value = aws_lambda_function.intake.function_name }
output "planner_lambda_name"      { value = aws_lambda_function.planner.function_name }
output "skip_detector_lambda_name" { value = aws_lambda_function.skip_detector.function_name }
output "tracker_lambda_name"      { value = aws_lambda_function.tracker.function_name }
output "slack_bot_lambda_name"    { value = aws_lambda_function.slack_bot.function_name }
