"""
Configurable LLM factory.

Default: Claude 3 Haiku on Bedrock (~20x cheaper than Sonnet).
Override via BEDROCK_MODEL_ID env var — swap models without code changes.

Common model IDs:
  anthropic.claude-3-haiku-20240307-v1:0       (default, cheapest)
  anthropic.claude-3-5-haiku-20241022-v1:0     (better reasoning, still cheap)
  anthropic.claude-3-5-sonnet-20241022-v2:0    (highest quality)
"""
import os

from langchain_aws import ChatBedrock

_DEFAULT_MODEL = "anthropic.claude-3-haiku-20240307-v1:0"


def get_llm(streaming: bool = False) -> ChatBedrock:
    return ChatBedrock(
        model_id=os.environ.get("BEDROCK_MODEL_ID", _DEFAULT_MODEL),
        region_name=os.environ.get("AWS_REGION", "us-east-1"),
        streaming=streaming,
        model_kwargs={"max_tokens": 4096},
    )
