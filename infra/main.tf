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
  description = "Bedrock model/inference profile ID — swap without code changes"
  default     = "us.anthropic.claude-3-5-haiku-20241022-v1:0"
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
