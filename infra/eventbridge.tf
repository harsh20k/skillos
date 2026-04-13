# ---------------------------------------------------------------------------
# Planner — fires at 08:00 UTC daily
# ---------------------------------------------------------------------------

resource "aws_cloudwatch_event_rule" "planner_daily" {
  name                = "skillos-planner-08-00"
  description         = "Trigger SkillOS Planner at 08:00 UTC"
  schedule_expression = "cron(0 8 * * ? *)"
}

resource "aws_cloudwatch_event_target" "planner" {
  rule      = aws_cloudwatch_event_rule.planner_daily.name
  target_id = "skillos-planner"
  arn       = aws_lambda_function.planner.arn
}

resource "aws_lambda_permission" "planner_eventbridge" {
  statement_id  = "AllowEventBridgePlanner"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.planner.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.planner_daily.arn
}

# ---------------------------------------------------------------------------
# Skip Detector — fires at 23:00 UTC daily
# ---------------------------------------------------------------------------

resource "aws_cloudwatch_event_rule" "skip_detector_daily" {
  name                = "skillos-skip-detector-23-00"
  description         = "Trigger SkillOS Skip Detector at 23:00 UTC"
  schedule_expression = "cron(0 23 * * ? *)"
}

resource "aws_cloudwatch_event_target" "skip_detector" {
  rule      = aws_cloudwatch_event_rule.skip_detector_daily.name
  target_id = "skillos-skip-detector"
  arn       = aws_lambda_function.skip_detector.arn
}

resource "aws_lambda_permission" "skip_detector_eventbridge" {
  statement_id  = "AllowEventBridgeSkipDetector"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.skip_detector.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.skip_detector_daily.arn
}
