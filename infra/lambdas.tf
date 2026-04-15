# ---------------------------------------------------------------------------
# Lambda layer (third-party deps) — build first: ../scripts/build_lambda_layer.sh
# ---------------------------------------------------------------------------

data "archive_file" "skillos_layer" {
  type        = "zip"
  source_dir  = "${path.module}/layer-build"
  output_path = "${path.module}/skillos-layer.zip"
  excludes    = [".DS_Store"]

  lifecycle {
    precondition {
      condition     = length(fileset("${path.module}/layer-build/python", "**")) > 0
      error_message = "Lambda layer is empty or missing. From repo root run: ./scripts/build_lambda_layer.sh (requires Docker), then re-run Terraform."
    }
  }
}

resource "aws_lambda_layer_version" "skillos_deps" {
  layer_name               = "skillos-python-deps"
  filename                 = data.archive_file.skillos_layer.output_path
  compatible_runtimes      = ["python3.12"]
  compatible_architectures = ["x86_64"]
  source_code_hash         = data.archive_file.skillos_layer.output_base64sha256
}

# ---------------------------------------------------------------------------
# Lambda source package (application code only; deps in layer above)
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
  name = "lambda_policy"
  role = aws_iam_role.lambda_exec.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = concat(
      [
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
          Action   = ["s3:ListBucket"]
          Resource = "arn:aws:s3:::${var.s3_state_bucket}"
        },
        {
          Effect   = "Allow"
          Action   = ["secretsmanager:GetSecretValue"]
          Resource = "*"
        },
        {
          Effect = "Allow"
          Action = [
            "bedrock:InvokeModel",
            "bedrock:InvokeModelWithResponseStream"
          ]
          Resource = [
            "arn:aws:bedrock:*::foundation-model/*",
            "arn:aws:bedrock:*:*:inference-profile/*"
          ]
        },
        {
          Effect   = "Allow"
          Action   = ["lambda:InvokeFunction"]
          Resource = "*"
        }
      ],
      var.bedrock_assume_role_arn == "" ? [] : [
        {
          Effect   = "Allow"
          Action   = ["sts:AssumeRole"]
          Resource = var.bedrock_assume_role_arn
        }
      ]
    )
  })
}

# ---------------------------------------------------------------------------
# Common environment variables
# ---------------------------------------------------------------------------

locals {
  lambda_layers = [aws_lambda_layer_version.skillos_deps.arn]

  bedrock_cross_account_env = merge(
    var.bedrock_assume_role_arn == "" ? {} : {
      BEDROCK_ASSUME_ROLE_ARN          = var.bedrock_assume_role_arn
      BEDROCK_ASSUME_ROLE_SESSION_NAME = var.bedrock_assume_role_session_name
    },
    var.bedrock_assume_role_arn != "" && var.bedrock_assume_role_external_id != "" ? {
      BEDROCK_ASSUME_ROLE_EXTERNAL_ID = var.bedrock_assume_role_external_id
    } : {},
    var.bedrock_assume_role_arn != "" && var.bedrock_region != "" ? {
      BEDROCK_REGION = var.bedrock_region
    } : {},
  )

  common_env = merge({
    GITHUB_REPO          = var.github_repo
    GITHUB_BRANCH        = var.github_branch
    S3_BUCKET            = var.s3_state_bucket
    BEDROCK_MODEL_ID     = var.bedrock_model_id
    LANGCHAIN_TRACING_V2 = "true"
    LANGCHAIN_API_KEY    = data.aws_secretsmanager_secret_version.langsmith_api_key.secret_string
    GITHUB_TOKEN         = data.aws_secretsmanager_secret_version.github_token.secret_string
  }, local.bedrock_cross_account_env)
}

# ---------------------------------------------------------------------------
# Lambda functions
# ---------------------------------------------------------------------------

resource "aws_lambda_function" "intake" {
  function_name    = "skillos-intake"
  filename         = data.archive_file.skillos.output_path
  source_code_hash = data.archive_file.skillos.output_base64sha256
  layers           = local.lambda_layers
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
  layers           = local.lambda_layers
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
  layers           = local.lambda_layers
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
  layers           = local.lambda_layers
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
  layers           = local.lambda_layers
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

output "intake_lambda_name" { value = aws_lambda_function.intake.function_name }
output "planner_lambda_name" { value = aws_lambda_function.planner.function_name }
output "skip_detector_lambda_name" { value = aws_lambda_function.skip_detector.function_name }
output "tracker_lambda_name" { value = aws_lambda_function.tracker.function_name }
output "slack_bot_lambda_name" { value = aws_lambda_function.slack_bot.function_name }
