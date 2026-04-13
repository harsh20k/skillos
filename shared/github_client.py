"""Thin wrapper around PyGithub for SkillOS file operations."""
import os
from datetime import datetime, timezone

from github import Github, GithubException
from github.Repository import Repository


class GitHubClient:
    def __init__(self) -> None:
        token = os.environ["GITHUB_TOKEN"]
        repo_name = os.environ["GITHUB_REPO"]  # e.g. "harsh20k/skillos"
        self._gh = Github(token)
        self._repo: Repository = self._gh.get_repo(repo_name)
        self._branch = os.environ.get("GITHUB_BRANCH", "main")

    def get_file(self, path: str) -> str:
        contents = self._repo.get_contents(path, ref=self._branch)
        return contents.decoded_content.decode("utf-8")

    def _get_sha(self, path: str) -> str | None:
        try:
            contents = self._repo.get_contents(path, ref=self._branch)
            return contents.sha
        except GithubException:
            return None

    def list_dir(self, path: str) -> list[str]:
        try:
            contents = self._repo.get_contents(path, ref=self._branch)
            if isinstance(contents, list):
                return [c.path for c in contents]
            return [contents.path]
        except GithubException:
            return []

    def write_file(self, path: str, content: str, message: str) -> None:
        sha = self._get_sha(path)
        if sha:
            self._repo.update_file(path, message, content, sha, branch=self._branch)
        else:
            self._repo.create_file(path, message, content, branch=self._branch)

    def commit_exists_today(self, skill: str) -> bool:
        """Return True if a progress commit exists for skill today (UTC)."""
        today_start = datetime.now(tz=timezone.utc).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        commits = self._repo.get_commits(
            path=f"skills/{skill}/progress.md",
            since=today_start,
        )
        return len(commits.get_page(0)) > 0
