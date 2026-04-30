from string import Template

import questionary

from github import Repository
from ops_setup.gh import *


def load_file_content(file_path: str) -> str:
    with open(file_path) as f:
        content = f.read()
    return content


def render_agentic_squad_workflow(provider: str) -> str:
    content = load_file_content("./src/ops_setup/assets/github/workflows/agentic-squad.yml")
    tpl = Template(content)
    result = tpl.safe_substitute(PROVIDER=provider)
    return result


def create_agent_files(repo: Repository, setup_branch: str):
    questionary.print("🤖 Adding Agents skill files...")

    agent_skills = [
       "architect-skill",
       "developer-skill",
       "orchestrator-skill",
       "product-manager-skill",
       "reviewer-skill"
    ]

    for skill in agent_skills:
        path = f".agents/{skill}/SKILL.md"
        asset_path = f"./src/ops_setup/assets/agents/{skill}/SKILL.md"
        message = f"feat(ops): add agent {skill.replace('-', ' ')}"
        create_file(
            repo,
            path=path,
            message=message,
            content=load_file_content(asset_path),
            branch=setup_branch
        )


def create_github_workflow_files(repo: Repository, setup_branch: str, selected_provider: str):
    questionary.print("🔧 Adding GitHub workflow: agentic-squad.yml...")

    # ADD: github/workflows/agentic-squad.yml
    agentic_squad_workflow = render_agentic_squad_workflow(selected_provider)
    create_file(
        repo,
        path=".github/workflows/agentic-squad.yml",
        message="feat(ops): add github workflow agentic squad",
        content=agentic_squad_workflow,
        branch=setup_branch
    )

    # ADD: github/workflows/copilot-instructions.md
    create_file(
        repo,
        path=".github/copilot-instructions.md",
        message="feat(ops): add github workflow copilot instructions",
        content=load_file_content("./src/ops_setup/assets/github/copilot-instructions.md"),
        branch=setup_branch
    )


def main() -> None:
    questionary.print("Zup Labs One Person Squad setup tool!")
    repo = fetch_repo()

    create_repo_labels(repo)

    providers = ["gemini", "claude", "copilot", "codex"]
    selected_provider = questionary.select("Select a provider:", choices=providers).ask()

    setup_branch = "feat/ops-setup"
    prepare_ops_setup_branch(repo, setup_branch)

    create_repo_provider_secret(repo, selected_provider)

    create_github_workflow_files(repo, setup_branch, selected_provider)

    create_agent_files(repo, setup_branch)

