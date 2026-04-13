# HTTP API Gateway — receives Slack slash commands
# POST /slack/events → slack_bot Lambda

resource "aws_apigatewayv2_api" "skillos" {
  name          = "skillos-api"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_integration" "slack_bot" {
  api_id             = aws_apigatewayv2_api.skillos.id
  integration_type   = "AWS_PROXY"
  integration_uri    = aws_lambda_function.slack_bot.invoke_arn
  integration_method = "POST"
}

resource "aws_apigatewayv2_route" "slack_events" {
  api_id    = aws_apigatewayv2_api.skillos.id
  route_key = "POST /slack/events"
  target    = "integrations/${aws_apigatewayv2_integration.slack_bot.id}"
}

resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.skillos.id
  name        = "$default"
  auto_deploy = true
}

resource "aws_lambda_permission" "slack_bot_apigw" {
  statement_id  = "AllowAPIGatewaySlackBot"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.slack_bot.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.skillos.execution_arn}/*/*"
}

output "slack_webhook_url" {
  value       = "${aws_apigatewayv2_stage.default.invoke_url}/slack/events"
  description = "Set this as the Request URL in your Slack app slash command configuration"
}
