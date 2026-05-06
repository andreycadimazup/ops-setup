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
    questionary.print("Adding Agents skill files...")

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

def create_agentic_files(repo: Repository, setup_branch: str):
    questionary.print("Adding Agentic skill files...")

    create_file(
        repo,
        path=".agentic/SQUAD.md",
        message=f"feat(ops): add agentic SQUAD",
        content=load_file_content(f"./src/ops_setup/assets/agentic/SQUAD.md"),
        branch=setup_branch
    )

    create_file(
        repo,
        path=".agentic/GUARDRAILS.md",
        message=f"feat(ops): add agentic GUARDRAILS",
        content=load_file_content(f"./src/ops_setup/assets/agentic/GUARDRAILS.md"),
        branch=setup_branch
    )

    agent_skills = [
       "architect-skill",
       "developer-skill",
       "orchestrator-skill",
       "product-manager-skill",
       "reviewer-skill"
    ]

    for skill in agent_skills:
        asset_path = f"./src/ops_setup/assets/agentic/skills/{skill}/SKILL.md"
        create_file(
            repo,
            path=f".agentic/skills/{skill}/SKILL.md",
            message = f"feat(ops): add agentic {skill.replace('-', ' ')}",
            content=load_file_content(asset_path),
            branch=setup_branch
        )

        if skill == "orchestrator-skill":
            create_file(
                repo,
                path=f".agentic/skills/{skill}/references/context-hooks.md",
                message=f"feat(ops): add agentic {skill.replace('-', ' ')} context hooks ref",
                content=load_file_content(f"./src/ops_setup/assets/agentic/skills/{skill}/references/context-hooks.md"),
                branch=setup_branch
            )


def create_github_workflow_files(repo: Repository, setup_branch: str, selected_provider: str):
    questionary.print("Adding GitHub workflow: agentic-squad.yml...")

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

def create_ops_pr(repo: Repository, setup_branch: str, selected_provider: str, base_branch:str="main"):
    title = "Feat: One Person Squad setup things"
    questionary.print(f"Creating PR ({title})...")

    pr_body_desc = f"""
## Description
Adding the necessary files for One Person Squad to function with the provider: **{selected_provider}**

## Changes
- [x] Added Agent Squad Github workflow
- [x] Added Agent Skill files
- [x] Added Agentic Skill files
"""
    repo.create_pull(
        base=base_branch,
        head=setup_branch,
        title=title,
        body=pr_body_desc,
    )


def main() -> None:
    questionary.print("Zup Labs One Person Squad setup tool!")
    repo = fetch_repo()

    create_repo_labels(repo)

    providers = ["gemini", "claude", "copilot", "codex"]
    selected_provider = questionary.select("Select a provider:", choices=providers).ask()
    create_repo_provider_secret(repo, selected_provider)

    setup_branch = "feat/ops-setup"
    prepare_ops_setup_branch(repo, setup_branch)

    create_github_workflow_files(repo, setup_branch, selected_provider)

    create_agentic_files(repo, setup_branch)

    create_agent_files(repo, setup_branch)

    create_ops_pr(repo, setup_branch, selected_provider)
