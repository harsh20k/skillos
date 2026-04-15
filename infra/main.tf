terraform {
  required_version = ">= 1.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
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
