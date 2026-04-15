"""
Configurable LLM factory.

Default: Google Gemma 3 12B IT on Bedrock (cost-effective open-weight model).
Override via BEDROCK_MODEL_ID env var — swap models without code changes.

Google models use Bedrock **Converse** via ChatBedrockConverse. Anthropic / Meta / etc.
still use ChatBedrock (invoke path).

Cross-account Bedrock (Account A hosts Bedrock, Account B hosts infra):
  Set BEDROCK_ASSUME_ROLE_ARN to the role ARN in Account A.
  Optionally set BEDROCK_ASSUME_ROLE_EXTERNAL_ID, BEDROCK_ASSUME_ROLE_SESSION_NAME, BEDROCK_REGION.
  When set, get_llm() assumes the role and creates a Bedrock client with temporary credentials.
  Credentials are cached per Lambda container and refreshed automatically before expiry.

Common model IDs:
  google.gemma-3-12b-it                         (default)
  us.anthropic.claude-3-5-haiku-20241022-v1:0    (inference profile, Anthropic)
  anthropic.claude-3-5-sonnet-20241022-v2:0     (Sonnet, quality)
"""
import os
from datetime import datetime, timezone
from typing import Optional

import boto3
from langchain_aws import ChatBedrock, ChatBedrockConverse
from langchain_core.language_models.chat_models import BaseChatModel

_DEFAULT_MODEL = "google.gemma-3-12b-it"

# Module-level cache: (boto3 client, expiry datetime) — reused across Lambda warm invocations
_cached_client: Optional[object] = None
_cached_expiry: Optional[datetime] = None

# Refresh credentials this many seconds before actual expiry to avoid using stale creds
_REFRESH_BUFFER_SECONDS = 60


def _get_cross_account_bedrock_client() -> object:
    """Assume role in Account A and return a bedrock-runtime client using temp credentials.
    Caches the client per Lambda container and refreshes before expiry."""
    global _cached_client, _cached_expiry

    now = datetime.now(timezone.utc)
    if _cached_client is not None and _cached_expiry is not None:
        seconds_remaining = (_cached_expiry - now).total_seconds()
        if seconds_remaining > _REFRESH_BUFFER_SECONDS:
            return _cached_client

    role_arn = os.environ["BEDROCK_ASSUME_ROLE_ARN"]
    session_name = os.environ.get("BEDROCK_ASSUME_ROLE_SESSION_NAME", "skillos-bedrock-session")
    external_id = os.environ.get("BEDROCK_ASSUME_ROLE_EXTERNAL_ID")
    region = os.environ.get("BEDROCK_REGION", os.environ.get("AWS_REGION", "us-east-1"))

    assume_kwargs = {
        "RoleArn": role_arn,
        "RoleSessionName": session_name,
    }
    if external_id:
        assume_kwargs["ExternalId"] = external_id

    sts = boto3.client("sts")
    response = sts.assume_role(**assume_kwargs)
    creds = response["Credentials"]

    _cached_client = boto3.client(
        "bedrock-runtime",
        region_name=region,
        aws_access_key_id=creds["AccessKeyId"],
        aws_secret_access_key=creds["SecretAccessKey"],
        aws_session_token=creds["SessionToken"],
    )
    _cached_expiry = creds["Expiration"]

    return _cached_client


def _model_provider_prefix(model_id: str) -> str:
    parts = model_id.split(".", 2)
    if len(parts) > 1 and parts[0].lower() in {"eu", "us", "ap", "sa"}:
        return parts[1].lower()
    return parts[0].lower()


def get_llm(streaming: bool = False) -> BaseChatModel:
    model_id = os.environ.get("BEDROCK_MODEL_ID", _DEFAULT_MODEL)
    region = os.environ.get("BEDROCK_REGION", os.environ.get("AWS_REGION", "us-east-1"))
    client: Optional[object] = None
    if os.environ.get("BEDROCK_ASSUME_ROLE_ARN"):
        client = _get_cross_account_bedrock_client()

    if _model_provider_prefix(model_id) == "google":
        kwargs: dict = {
            "model": model_id,
            "region_name": region,
            "max_tokens": 4096,
        }
        if client is not None:
            kwargs["client"] = client
        return ChatBedrockConverse(**kwargs)

    kwargs_cb: dict = {
        "model_id": model_id,
        "region_name": region,
        "streaming": streaming,
        "model_kwargs": {"max_tokens": 4096},
    }
    if client is not None:
        kwargs_cb["client"] = client
    return ChatBedrock(**kwargs_cb)
