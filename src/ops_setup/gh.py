import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import questionary
from github import Github, Auth, Repository, Branch
from github.GithubException import GithubException

from dotenv import load_dotenv

load_dotenv()

gh = Github(
    auth=Auth.Token(token=os.getenv("GITHUB_TOKEN")),
    verify=False,
    lazy=False
)


def fetch_repo() -> Repository:
    questionary.print("🔍 Fetching your GitHub repositories...")
    repositories = [r.name for r in gh.get_user().get_repos()]
    selected_repo = questionary.select(
        "Select a repository:",
        choices=repositories,
    ).ask()
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
            questionary.print(f'✔️ Label `{label["name"]}` created.')
        except GithubException as e:
            if e.status == 422 and "already_exists" in str(e.data):
                questionary.print(f'ℹ️ Label `{label["name"]}` already exists.')
            else:
                questionary.print(f'❌ Could not create label `{label["name"]}`: {e}')
        except Exception as e:
            questionary.print(f'❌ Could not create label `{label["name"]}`: {e}')


def create_repo_provider_secret(repo: Repository, selected_provider: str):
    # Provider selection
    provider_options = [
        {"name": "gemini", "secret": "GEMINI_API_KEY"},
        {"name": "claude", "secret": "ANTHROPIC_API_KEY"},
        {"name": "copilot", "secret": "OPENAI_API_KEY"},
        {"name": "codex", "secret": "GITHUB_TOKEN"},
    ]

    provider_secret_name = next(
        (p["secret"] for p in provider_options if p["name"] == selected_provider), None
    )

    if provider_secret_name:
        secret_value = questionary.password(
            f"Enter the value for secret '{provider_secret_name}':"
        ).ask()
        try:
            repo.create_secret(provider_secret_name, secret_value)
            questionary.print(f"✅ Secret '{provider_secret_name}' set successfully.")
        except Exception as e:
            questionary.print(f"❌ Could not set secret '{provider_secret_name}': {e}")
    else:
        questionary.print("❌ No provider selected.")


def prepare_ops_setup_branch(repo: Repository, branch_name: str):
    questionary.print(f"🌱 Creating setup branch '{branch_name}'")

    source_branch = repo.get_branch("main")
    source_sha = source_branch.commit.sha

    ref = f"refs/heads/{branch_name}"
    try:
        repo.create_git_ref(ref=ref, sha=source_sha)
    except GithubException as e:
        pass
    except Exception as e:
        pass


def create_file(
    repo: Repository,
    path: str,
    message: str,
    content: str,
    branch: str,
):
    repo.create_file(
        path=path,
        message=message,
        content=content,
        branch=branch
    )


__all__ = [
    "fetch_repo",
    "create_repo_labels",
    "create_repo_provider_secret",
    "prepare_ops_setup_branch",
    "create_file",
]
