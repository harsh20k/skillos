#!/usr/bin/env bash
# Build SkillOS Lambda layer (Python 3.12 deps) in a Linux image so wheels match
# AWS Lambda x86_64. Run from any host with Docker before `terraform apply`.
#
# Usage:
#   ./scripts/build_lambda_layer.sh
#
# Env:
#   LAMBDA_BUILD_IMAGE  (default: public.ecr.aws/sam/build-python3.12:latest)
#   DOCKER_PLATFORM     (default: linux/amd64 — use linux/arm64 only if Lambdas are arm64)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LAYER_ROOT="${REPO_ROOT}/infra/layer-build"
PYTHON_DIR="${LAYER_ROOT}/python"
REQ="${REPO_ROOT}/requirements.txt"

LAMBDA_BUILD_IMAGE="${LAMBDA_BUILD_IMAGE:-public.ecr.aws/sam/build-python3.12:latest}"
DOCKER_PLATFORM="${DOCKER_PLATFORM:-linux/amd64}"

if ! command -v docker >/dev/null 2>&1; then
  echo "error: docker is required to build the Lambda layer" >&2
  exit 1
fi

if [[ ! -f "${REQ}" ]]; then
  echo "error: missing ${REQ}" >&2
  exit 1
fi

rm -rf "${PYTHON_DIR}"
mkdir -p "${PYTHON_DIR}"

echo "Building layer with ${LAMBDA_BUILD_IMAGE} (${DOCKER_PLATFORM})..."

docker run --rm \
  --platform "${DOCKER_PLATFORM}" \
  -v "${REPO_ROOT}:/workspace:rw" \
  -w /workspace \
  "${LAMBDA_BUILD_IMAGE}" \
  /bin/bash -lc "pip install --upgrade pip setuptools wheel && pip install --no-cache-dir -r requirements.txt -t infra/layer-build/python"

find "${PYTHON_DIR}" -type d -name '__pycache__' -prune -exec rm -rf {} + 2>/dev/null || true

echo "ok: dependencies installed under infra/layer-build/python ($(du -sh "${PYTHON_DIR}" | cut -f1))"
