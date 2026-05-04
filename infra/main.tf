terraform {
  required_version = ">= 1.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
  }

  backend "s3" {
    bucket = "skillos-terraform-state-965384155969"
    key    = "skillos/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region
}

# ---------------------------------------------------------------------------
# Variables
# ---------------------------------------------------------------------------

variable "aws_region" {
  description = "AWS region to deploy to"
  default     = "us-east-1"
}

variable "bedrock_model_id" {
  description = "Bedrock model or inference profile ID — swap without code changes (Gemma uses google.*; Claude 3.5+ often needs us.* inference profile)"
  default     = "google.gemma-3-12b-it"
}

variable "bedrock_assume_role_arn" {
  description = "If non-empty, SkillOS Lambdas call sts:AssumeRole on this ARN (typically Account A) before Bedrock. Leave empty for same-account Bedrock."
  type        = string
  default     = ""
}

variable "bedrock_assume_role_external_id" {
  description = "ExternalId for AssumeRole; must match the trust condition on bedrock_assume_role_arn. Omit or leave empty if trust policy does not use ExternalId."
  type        = string
  default     = ""
}

variable "bedrock_assume_role_session_name" {
  description = "Role session name passed to sts:AssumeRole"
  type        = string
  default     = "skillos-bedrock-session"
}

variable "bedrock_region" {
  description = "If non-empty, sets BEDROCK_REGION on Lambdas (Bedrock API region). When empty, runtime uses AWS_REGION."
  type        = string
  default     = ""
}

variable "github_repo" {
  description = "GitHub repo in owner/repo format (e.g. harsh20k/skillos)"
  type        = string
}

variable "github_branch" {
  description = "GitHub branch used as the memory layer"
  default     = "main"
}

variable "s3_state_bucket" {
  description = "S3 bucket for skip_state.json and ephemeral state"
  default     = "skillos-state"
}

variable "rag_chunk_size" {
  description = "Max characters per RAG note chunk (configurable for A/B comparison)"
  default     = "500"
}

variable "rag_chunk_overlap" {
  description = "Overlap between consecutive RAG chunks in characters"
  default     = "100"
}

variable "rag_top_k" {
  description = "Number of top-k chunks to retrieve per query"
  default     = "5"
}

variable "rag_embedding_model" {
  description = "Bedrock model ID for note embeddings"
  default     = "amazon.titan-embed-text-v2:0"
}

variable "rag_vector_bucket" {
  description = "S3 Vectors vector bucket name for the RAG notes index"
  default     = "skillos-rag-vectors"
}

variable "prompt_version" {
  description = "LangSmith Prompt Hub version tag to pull (e.g. 'latest', 'v2'). Used for A/B testing."
  type        = string
  default     = "latest"
}

# ---------------------------------------------------------------------------
# S3 state bucket
# ---------------------------------------------------------------------------

resource "aws_s3_bucket" "state" {
  bucket = var.s3_state_bucket
}

resource "aws_s3_bucket_versioning" "state" {
  bucket = aws_s3_bucket.state.id
  versioning_configuration {
    status = "Enabled"
  }
}

# ---------------------------------------------------------------------------
# S3 Vectors — vector bucket + notes index
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# GitHub Actions OIDC — allows vault repo to sync .md files to S3
# ---------------------------------------------------------------------------

data "aws_caller_identity" "current" {}

resource "aws_iam_openid_connect_provider" "github_actions" {
  url             = "https://token.actions.githubusercontent.com"
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
}

resource "aws_iam_role" "vault_sync" {
  name = "vault-sync-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = "sts:AssumeRoleWithWebIdentity"
      Principal = { Federated = aws_iam_openid_connect_provider.github_actions.arn }
      Condition = {
        StringEquals = {
          "token.actions.githubusercontent.com:aud" = "sts.amazonaws.com"
        }
        StringLike = {
          "token.actions.githubusercontent.com:sub" = "repo:harsh20k/second-brain-vault-agentic:ref:refs/heads/main"
        }
      }
    }]
  })
}

resource "aws_iam_role_policy" "vault_sync" {
  name = "vault-sync-policy"
  role = aws_iam_role.vault_sync.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["s3:PutObject", "s3:DeleteObject"]
        Resource = "arn:aws:s3:::${var.s3_state_bucket}/vault/*"
      },
      {
        Effect   = "Allow"
        Action   = ["s3:ListBucket"]
        Resource = "arn:aws:s3:::${var.s3_state_bucket}"
        Condition = {
          StringLike = { "s3:prefix" = ["vault/*"] }
        }
      }
    ]
  })
}

output "vault_sync_role_arn" {
  value = aws_iam_role.vault_sync.arn
}

# ---------------------------------------------------------------------------
# S3 Vectors — vector bucket + notes index
# ---------------------------------------------------------------------------

resource "aws_s3vectors_vector_bucket" "rag" {
  vector_bucket_name = var.rag_vector_bucket
}

resource "aws_s3vectors_index" "notes" {
  vector_bucket_name = aws_s3vectors_vector_bucket.rag.vector_bucket_name
  index_name         = "notes"
  data_type          = "float32"
  dimension          = 1024
  distance_metric    = "cosine"
}
