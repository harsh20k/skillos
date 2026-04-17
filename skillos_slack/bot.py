"""Slack Bolt app for SkillOS slash commands.

Commands:
  /learn <goal>       → Intake Lambda (multi-turn onboarding)
  /done <skill> [msg] → Tracker Lambda (log progress, unlock nodes)
  /skip <skill>       → Mark skill skipped for today
  /harder <skill>     → Increase difficulty in active.json
  /easier <skill>     → Decrease difficulty in active.json
  /skills, /skill     → List active skills and today's task count (alias)
"""
import json
import os

from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
    process_before_response=True,
)

_lambda_client = None
_DIFFICULTY_LEVELS = ["beginner", "intermediate", "advanced"]


def _lambda_client_get():
    """Lazy init: keeps import of botocore off the critical path when unused."""
    global _lambda_client
    if _lambda_client is None:
        import boto3

        _lambda_client = boto3.client("lambda")
    return _lambda_client


def _invoke(fn_name: str, payload: dict) -> dict:
    resp = _lambda_client_get().invoke(
        FunctionName=fn_name,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload).encode(),
    )
    return json.loads(resp["Payload"].read())


# ---------------------------------------------------------------------------
# /learn
# ---------------------------------------------------------------------------
# Slash commands must be acknowledged within ~3s. Intake invokes Bedrock + GitHub
# and often exceeds that; use lazy listeners so API Gateway returns immediately.


def _learn_ack(ack):
    # Slack needs an HTTP response quickly; Bolt then self-invokes for the lazy step.
    ack(
        text="Got it — drafting a reply (this can take ~10–20s)…",
        response_type="ephemeral",
    )


def _learn_lazy(command, say):
    text = command.get("text", "").strip()
    if not text:
        say("Usage: `/learn <your learning goal>`")
        return

    try:
        result = _invoke(
            os.environ["INTAKE_LAMBDA_NAME"],
            {"user_id": command["user_id"], "message": text},
        )
        say(result.get("reply", "Something went wrong. Please try again."))
    except Exception as exc:
        say(f"Something went wrong calling intake: `{exc}`")


app.command("/learn")(ack=_learn_ack, lazy=[_learn_lazy])


# ---------------------------------------------------------------------------
# /done
# ---------------------------------------------------------------------------


def _done_ack(ack):
    ack(
        text="Logging progress…",
        response_type="ephemeral",
    )


def _done_lazy(command, say):
    parts = command.get("text", "").strip().split(maxsplit=1)
    if not parts:
        say("Usage: `/done <skill> [optional note]`")
        return

    skill, context = parts[0], parts[1] if len(parts) > 1 else ""
    try:
        result = _invoke(
            os.environ["TRACKER_LAMBDA_NAME"],
            {"skill": skill, "user_id": command["user_id"], "context": context},
        )
    except Exception as exc:
        say(f"Something went wrong calling tracker: `{exc}`")
        return

    if result.get("status") == "error":
        say(f"Error: {result['message']}")
        return

    note = result.get("note", "")
    unlocked = result.get("unlocked", [])
    msg = f"Progress logged for *{skill}*!\n> {note}"
    if unlocked:
        msg += f"\n:unlock: Newly unlocked: {', '.join(f'`{n}`' for n in unlocked)}"
    say(msg)


app.command("/done")(ack=_done_ack, lazy=[_done_lazy])


# ---------------------------------------------------------------------------
# /skip
# ---------------------------------------------------------------------------

@app.command("/skip")
def handle_skip(ack, command, say):
    ack()
    skill = command.get("text", "").strip()
    if not skill:
        say("Usage: `/skip <skill>`")
        return

    # Write a skip flag to S3 immediately (rollover picks it up at 23:00)
    import boto3 as _boto3
    from datetime import date

    s3 = _boto3.client("s3")
    bucket = os.environ.get("S3_BUCKET", "skillos-state")
    key = "skip_state.json"

    try:
        existing = json.loads(s3.get_object(Bucket=bucket, Key=key)["Body"].read())
    except Exception:
        existing = {}

    existing[skill] = {"skipped_date": date.today().isoformat(), "rollover_tasks": []}
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(existing, indent=2).encode(),
        ContentType="application/json",
    )
    say(f"Skipped *{skill}* for today. Tasks will roll over to tomorrow (max 2).")


# ---------------------------------------------------------------------------
# /harder and /easier
# ---------------------------------------------------------------------------

@app.command("/harder")
def handle_harder(ack, command, say):
    ack()
    _adjust_difficulty(command, say, delta=+1)


@app.command("/easier")
def handle_easier(ack, command, say):
    ack()
    _adjust_difficulty(command, say, delta=-1)


def _adjust_difficulty(command, say, delta: int) -> None:
    skill = command.get("text", "").strip()
    direction = "harder" if delta > 0 else "easier"
    if not skill:
        say(f"Usage: `/{direction} <skill>`")
        return

    from shared.github_client import GitHubClient

    gh = GitHubClient()
    try:
        active: list[dict] = json.loads(gh.get_file("skills/active.json"))
        updated = False
        for s in active:
            if s["name"] == skill:
                idx = _DIFFICULTY_LEVELS.index(s.get("difficulty", "beginner"))
                s["difficulty"] = _DIFFICULTY_LEVELS[
                    max(0, min(idx + delta, len(_DIFFICULTY_LEVELS) - 1))
                ]
                updated = True
                new_level = s["difficulty"]
                break

        if not updated:
            say(f"Skill `{skill}` not found.")
            return

        gh.write_file(
            "skills/active.json",
            json.dumps(active, indent=2),
            f"skills: difficulty {direction} {skill}",
        )
        say(f"Adjusted *{skill}* to `{new_level}`.")
    except Exception as exc:
        say(f"Error: {exc}")


# ---------------------------------------------------------------------------
# /skills (Slack apps may register /skill — same handler)
# ---------------------------------------------------------------------------

@app.command("/skill")
@app.command("/skills")
def handle_skills(ack, command, say):
    ack()
    from datetime import date

    from shared.github_client import GitHubClient

    gh = GitHubClient()
    today = date.today().isoformat()

    try:
        active: list[dict] = json.loads(gh.get_file("skills/active.json"))
    except Exception as exc:
        say(f"Error fetching skills: {exc}")
        return

    lines = ["*Active Skills*"]
    for skill in active:
        name, display = skill["name"], skill["display_name"]
        difficulty = skill.get("difficulty", "beginner")
        try:
            daily = gh.get_file(f"skills/{name}/daily/{today}.md")
            total = daily.count("- [ ]") + daily.count("- [x]")
            done = daily.count("- [x]")
            task_info = f"{done}/{total} tasks done"
        except Exception:
            task_info = "no tasks yet"
        lines.append(f"• *{display}* ({difficulty}) — {task_info}")

    say("\n".join(lines))


# ---------------------------------------------------------------------------
# Lambda entry point
# ---------------------------------------------------------------------------

handler = SlackRequestHandler(app=app)


def lambda_handler(event: dict, context) -> dict:
    return handler.handle(event, context)
