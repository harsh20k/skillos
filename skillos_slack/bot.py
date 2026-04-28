"""Slack Bolt app for SkillOS slash commands.

Commands:
  /learn <goal>          → Intake Lambda (multi-turn onboarding)
  /done <skill> [msg]    → Tracker Lambda (log progress, unlock nodes)
  /skip <skill>          → Mark skill skipped for today
  /harder <skill>        → Increase difficulty in active.json
  /easier <skill>        → Decrease difficulty in active.json
  /skills, /skill        → List active skills and today's task count (alias)
  /pause <skill>         → Freeze a skill (excluded from planning + skip detection)
  /resume <skill>        → Unfreeze a paused skill
  /list-all-skills       → Visual list of all skills with status badges
  /todays-tasks          → Show today's full task list with completion status
  /remaining-tasks       → Show only unchecked tasks for today
  /reshuffle-tasks       → Regenerate today's tasks via Planner
  /why-tasks             → Explain the reasoning behind each task (DAG-based, no LLM)
  /skillos <message>     → LLM supervisor — natural language routing to any agent
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
# /list-all-skills — visual overview with status badges
# ---------------------------------------------------------------------------

@app.command("/list-all-skills")
def handle_list_all_skills(ack, command, say):
    ack()
    from shared.github_client import GitHubClient

    gh = GitHubClient()
    try:
        all_skills: list[dict] = json.loads(gh.get_file("skills/active.json"))
    except Exception as exc:
        say(f"Error fetching skills: {exc}")
        return

    _STATUS_BADGE = {
        "active": ":green_circle: Active",
        "paused": ":double_vertical_bar: Paused",
        "completed": ":white_check_mark: Completed",
    }

    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "All Skills", "emoji": True},
        },
        {"type": "divider"},
    ]

    for skill in all_skills:
        status = skill.get("status", "active")
        badge = _STATUS_BADGE.get(status, status)
        difficulty = skill.get("difficulty", "beginner")
        start = skill.get("start_date", "unknown")
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"*{skill['display_name']}*  {badge}\n"
                    f"`{difficulty}` · started {start} · `{skill['name']}`"
                ),
            },
        })

    if not all_skills:
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": "No skills yet. Use `/learn <goal>` to get started."},
        })

    say(blocks=blocks, text="All Skills")


# ---------------------------------------------------------------------------
# /todays-tasks — full task list with completion status
# ---------------------------------------------------------------------------

@app.command("/todays-tasks")
def handle_todays_tasks(ack, command, say):
    ack()
    from datetime import date
    from shared.github_client import GitHubClient

    gh = GitHubClient()
    today = date.today().isoformat()

    try:
        active: list[dict] = json.loads(gh.get_file("skills/active.json"))
    except Exception as exc:
        say(f"Error: {exc}")
        return

    active_skills = [s for s in active if s.get("status", "active") == "active"]
    if not active_skills:
        say("No active skills. Use `/learn` to start one.")
        return

    # Collect tasks from each skill's daily file
    all_lines: list[str] = [f"*Tasks for {today}*\n"]
    any_found = False
    for skill in active_skills:
        name = skill["name"]
        display = skill["display_name"]
        try:
            content = gh.get_file(f"skills/{name}/daily/{today}.md")
            task_lines = [l for l in content.splitlines() if l.strip().startswith("- [")]
            if task_lines:
                any_found = True
                all_lines.append(f"\n*{display}*")
                all_lines.extend(task_lines)
        except Exception:
            continue

    if not any_found:
        say("No tasks found for today. The planner runs at 08:00.")
        return
    say("\n".join(all_lines))


# ---------------------------------------------------------------------------
# /remaining-tasks — only unchecked tasks
# ---------------------------------------------------------------------------

@app.command("/remaining-tasks")
def handle_remaining_tasks(ack, command, say):
    ack()
    from datetime import date
    from shared.github_client import GitHubClient

    gh = GitHubClient()
    today = date.today().isoformat()

    try:
        active: list[dict] = json.loads(gh.get_file("skills/active.json"))
    except Exception as exc:
        say(f"Error: {exc}")
        return

    active_skills = [s for s in active if s.get("status", "active") == "active"]
    lines: list[str] = [f"*Remaining tasks — {today}*\n"]
    any_found = False

    for skill in active_skills:
        name = skill["name"]
        display = skill["display_name"]
        try:
            content = gh.get_file(f"skills/{name}/daily/{today}.md")
            unchecked = [l for l in content.splitlines() if l.strip().startswith("- [ ]")]
            if unchecked:
                any_found = True
                lines.append(f"\n*{display}*")
                lines.extend(unchecked)
        except Exception:
            continue

    if not any_found:
        say(":tada: All tasks done for today!")
        return
    say("\n".join(lines))


# ---------------------------------------------------------------------------
# /reshuffle-tasks — regenerate today's plan via Planner Lambda
# ---------------------------------------------------------------------------

def _reshuffle_ack(ack):
    ack(text="Reshuffling tasks (this may take ~15s)…", response_type="ephemeral")


def _reshuffle_lazy(command, say):
    try:
        _invoke(os.environ["PLANNER_LAMBDA_NAME"], {})
        say(":arrows_counterclockwise: Tasks reshuffled! Use `/todays-tasks` to see the new plan.")
    except Exception as exc:
        say(f"Error reshuffling tasks: `{exc}`")


app.command("/reshuffle-tasks")(ack=_reshuffle_ack, lazy=[_reshuffle_lazy])


# ---------------------------------------------------------------------------
# /why-tasks — deterministic DAG-based explanation (no LLM)
# ---------------------------------------------------------------------------

@app.command("/why-tasks")
def handle_why_tasks(ack, command, say):
    ack()
    from datetime import date
    from shared.github_client import GitHubClient
    from agents.planner.skill_tree import parse_skill_tree
    import re

    gh = GitHubClient()
    today = date.today().isoformat()

    try:
        active: list[dict] = json.loads(gh.get_file("skills/active.json"))
    except Exception as exc:
        say(f"Error: {exc}")
        return

    active_skills = [s for s in active if s.get("status", "active") == "active"]
    lines: list[str] = [f"*Why each task? — {today}*\n"]
    any_found = False

    for skill in active_skills:
        name = skill["name"]
        display = skill["display_name"]
        try:
            daily_content = gh.get_file(f"skills/{name}/daily/{today}.md")
            tree = parse_skill_tree(gh.get_file(f"skills/{name}/skill-tree.md"))
        except Exception:
            continue

        node_map = {n["id"]: n for n in tree.get("nodes", [])}

        task_lines = [l for l in daily_content.splitlines() if l.strip().startswith("- [")]
        if not task_lines:
            continue

        any_found = True
        lines.append(f"\n*{display}*")

        for task_line in task_lines:
            # Extract node_id from `#node-id` at end of line
            node_match = re.search(r"`#([^`]+)`", task_line)
            if not node_match:
                lines.append(f"{task_line}\n  _↳ No node link found._")
                continue

            node_id = node_match.group(1)
            node = node_map.get(node_id)
            if not node:
                lines.append(f"{task_line}\n  _↳ Node `{node_id}` not in skill tree._")
                continue

            prereqs = node.get("prerequisites", [])
            if prereqs:
                prereq_labels = [node_map[p]["label"] if p in node_map else p for p in prereqs]
                why = f"Unlocks after: {', '.join(prereq_labels)}"
            else:
                why = "Root node — starting point for this skill"

            lines.append(f"{task_line}\n  _↳ *{node['label']}* — {why}_")

    if not any_found:
        say("No tasks found for today. The planner runs at 08:00.")
        return
    say("\n".join(lines))


# ---------------------------------------------------------------------------
# /pause and /resume
# ---------------------------------------------------------------------------

def _set_skill_status(command, say, new_status: str) -> None:
    skill = command.get("text", "").strip()
    action = "pause" if new_status == "paused" else "resume"
    if not skill:
        say(f"Usage: `/{action} <skill>`")
        return

    from shared.github_client import GitHubClient

    gh = GitHubClient()
    try:
        active: list[dict] = json.loads(gh.get_file("skills/active.json"))
        updated = False
        for s in active:
            if s["name"] == skill:
                s["status"] = new_status
                updated = True
                break

        if not updated:
            say(f"Skill `{skill}` not found.")
            return

        gh.write_file(
            "skills/active.json",
            json.dumps(active, indent=2),
            f"skills: {action} {skill}",
        )
        if new_status == "paused":
            say(f":double_vertical_bar: Paused *{skill}*. It will be excluded from planning and skip detection until you `/resume` it.")
        else:
            say(f":arrow_forward: Resumed *{skill}*. It will be included in tomorrow's plan.")
    except Exception as exc:
        say(f"Error: {exc}")


@app.command("/pause")
def handle_pause(ack, command, say):
    ack()
    _set_skill_status(command, say, "paused")


@app.command("/resume")
def handle_resume(ack, command, say):
    ack()
    _set_skill_status(command, say, "active")


# ---------------------------------------------------------------------------
# /skillos — LLM supervisor: unified natural language entry point
# ---------------------------------------------------------------------------

def _skillos_ack(ack):
    ack(text="Thinking…", response_type="ephemeral")


def _skillos_lazy(command, say):
    text = command.get("text", "").strip()
    if not text:
        say(
            "Usage: `/skillos <what you want to do>`\n"
            "Examples:\n"
            "• `/skillos show my tasks`\n"
            "• `/skillos I finished portrait practice today`\n"
            "• `/skillos pause public-speaking`\n"
            "• `/skillos I want to learn guitar`"
        )
        return

    try:
        result = _invoke(
            os.environ["SUPERVISOR_LAMBDA_NAME"],
            {"message": text, "user_id": command["user_id"]},
        )
        say(result.get("reply", "Something went wrong. Try a specific command like `/todays-tasks`."))
    except Exception as exc:
        say(f"Something went wrong calling the supervisor: `{exc}`")


app.command("/skillos")(ack=_skillos_ack, lazy=[_skillos_lazy])


# ---------------------------------------------------------------------------
# Lambda entry point
# ---------------------------------------------------------------------------

handler = SlackRequestHandler(app=app)


def lambda_handler(event: dict, context) -> dict:
    return handler.handle(event, context)
