"""Read user notes from GitHub to provide context during intake."""
from shared.github_client import GitHubClient

_MAX_FILE_CHARS = 2_000
_MAX_TOTAL_CHARS = 8_000


def fetch_notes_summary(client: GitHubClient) -> str:
    """Return a concatenated summary of all .md files under notes/."""
    paths = client.list_dir("notes")
    if not paths:
        return ""

    parts: list[str] = []
    for path in paths:
        if not path.endswith(".md"):
            continue
        try:
            content = client.get_file(path)
            parts.append(f"### {path}\n{content[:_MAX_FILE_CHARS]}")
        except Exception:
            continue

    return "\n\n".join(parts)[:_MAX_TOTAL_CHARS]
