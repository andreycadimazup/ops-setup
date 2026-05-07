import os
import urllib3
from typing import Dict, List

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import questionary
from github import Github, Auth, Repository
from github.GithubException import GithubException

from dotenv import load_dotenv

load_dotenv()

gh = Github(
    auth=Auth.Token(token=os.getenv("GITHUB_TOKEN")),
    verify=False,
    lazy=False
)


def fetch_repo() -> Repository:
    questionary.print("Fetching your GitHub repositories...")
    repositories = [r.name for r in gh.get_user().get_repos()]
    selected_repo = questionary.select("Select a repository:", choices=repositories).ask()
    repo = gh.get_user().get_repo(selected_repo)
    return repo


def create_repo_labels(repo: Repository):
    labels = [
        {"name": "status: idea", "color": "BFDADC", "description": "Initial idea"},
        {"name": "status: need-spec", "color": "F9D0C4", "description": "Needs a specialist"},
        {"name": "status: spec-review", "color": "F7C6C7", "description": "Specialist review"},
        {"name": "status: ready-for-dev", "color": "B4E2B9", "description": "Ready for development"},
        {"name": "status: in-progress", "color": "FBCA04", "description": "In development"},
        {"name": "status: ready-for-merge", "color": "0E8A16", "description": "Ready for merge"},
        {"name": "status: busy", "color": "D4C5F9", "description": "Waiting for availability"},
    ]

    print(f"🏷️ Creating OPS necessary labels in repository `{repo.name}`...")
    for label in labels:
        try:
            repo.create_label(
                name=label["name"],
                color=label["color"],
                description=label["description"]
            )
            questionary.print(f'Label `{label["name"]}` created.')
        except GithubException as e:
            if e.status == 422 and "already_exists" in str(e.data):
                questionary.print(f'Label `{label["name"]}` already exists.')
            else:
                questionary.print(f'Could not create label `{label["name"]}`: {e}')
        except Exception as e:
            questionary.print(f'Could not create label `{label["name"]}`: {e}')

from typing import Dict, List
import questionary
from github.Repository import Repository  # adjust import to your actual Repository class

def create_repo_provider_secret(repo: Repository, selected_provider: str):
    provider_options: Dict[str, List[str]] = {
        "gemini":  ["GEMINI_API_KEY"],
        "claude":  ["ANTHROPIC_API_KEY"],
        "copilot": ["GITHUB_TOKEN"],
        # Only ask for OPENAI_API_KEY; reuse it for CODEX_API_KEY
        "codex":   ["OPENAI_API_KEY"],
    }

    provider_secrets = provider_options.get(selected_provider)

    if not provider_secrets:
        questionary.print("No provider selected.")
        return

    for secret_name in provider_secrets:
        secret_value = questionary.password(
            f"Enter the value for secret '{secret_name}':"
        ).ask()

        if not secret_value:
            questionary.print(f"Secret '{secret_name}' was not provided, skipping.")
            continue

        try:
            # Create the secret the user actually typed
            repo.create_secret(secret_name, secret_value)
            questionary.print(f"Secret '{secret_name}' set successfully.")

            # For codex, also create CODEX_API_KEY from the same value
            if selected_provider == "codex" and secret_name == "OPENAI_API_KEY":
                repo.create_secret("CODEX_API_KEY", secret_value)
                questionary.print(
                    "Secret 'CODEX_API_KEY' set successfully using 'OPENAI_API_KEY'."
                )

        except Exception as e:
            questionary.print(f"Could not set secret '{secret_name}': {e}")


def prepare_ops_setup_branch(repo: Repository, branch_name: str):
    questionary.print(f"Creating setup branch '{branch_name}'")

    source_branch = repo.get_branch("main")
    source_sha = source_branch.commit.sha

    ref = f"refs/heads/{branch_name}"
    try:
        repo.create_git_ref(ref=ref, sha=source_sha)
    except GithubException as e:
        pass
    except Exception as e:
        pass


def create_file(repo: Repository, path: str, message: str, content: str, branch: str):
    repo.create_file(path=path, message=message, content=content, branch=branch)


__all__ = [
    "fetch_repo",
    "create_repo_labels",
    "create_repo_provider_secret",
    "prepare_ops_setup_branch",
    "create_file",
]
