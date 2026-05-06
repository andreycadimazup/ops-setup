# Project Guardrails & SDLC Policies

This file defines the strict and project-specific rules that all agents MUST follow. These rules are customizable per project and override any default behavior of the agents.

## 🤖 Non-Interactive Execution (Headless)
As agents operate in the terminal without human intervention, all command-line tools MUST be used in non-interactive mode:
- **GitHub CLI (`gh`):** Always use environment variables like `GH_PROMPT_DISABLED=1` or explicit flags (`--title`, `--body`, `--fill`) to avoid selection menus.
- **Git:** Always use `git commit -m "message"` (never just `git commit` to avoid opening text editors like vim/nano).

## 📋 Standard Operating Procedures (SOP) for Agents
These rules apply to ALL agents and skills across the squad:

### 1. 🌍 Language & Communication
- **Portuguese (pt-br):** EVERY comment, specification, or PR description on GitHub MUST be written in Portuguese.
- **Hidden Tag:** Every comment MUST include the hidden tag `<!-- agentic-comment -->` for identification.
- **No Path Reference:** Refer to agents/skills by their names (e.g., `@developer`), NEVER use file paths (e.g., `.agentic/agents/developer.md`).

### 2. 🤖 Non-Interactive execution (`gh` CLI)
- **Prompt Disabled:** Always use `GH_PROMPT_DISABLED=1` environment variable.
- **Explicit Flags:** Use `--fill`, `-b`, or `-m` to avoid interactive prompts.
- **UTF-8 Support:** On Windows, ensure output encoding is set correctly: `$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8`.

### 3. 📊 Project Boards Sync
When changing an issue label via `gh issue edit`, ALWAYS:
1.  Check if the issue belongs to a project board: `gh issue view <ID> --json projectItems`.
2.  If it does, sync the "Status" field using `gh project item-edit` according to the mapping:
    - `status: idea`, `status: need-spec` -> **Backlog**
    - `status: ready-for-dev` -> **To Do**
    - `status: in-progress`, `status: busy` -> **In Progress**
    - `status: spec-review`, `status: in-review` -> **In Review**
    - `status: ready-for-merge` -> **Done**

### 4. 🧠 Context & Performance
- **Atomic Commits:** Keep commits small and logical. You MUST only stage and commit files that you have explicitly modified or created to fulfill the task.
- **Research First:** For implementation tasks, ALWAYS use the `codebase_investigator` tool for research before writing code.
- **Batch Tasks:** Use the `generalist` sub-agent for tasks involving multiple files or repetitive modifications.

## 🌿 Branching & Version Control
- **No Direct Commits to Main:** NEVER commit directly to the `main`, `master`, or `dev` branches.
- **Feature Branches:** Always create a new branch for your work using a standard naming convention (e.g., `feat/issue-<N>`, `fix/issue-<N>`, or `chore/issue-<N>`).
- **Atomic & Strict Commits:** Keep commits small and logical. You MUST only stage and commit files that you have explicitly modified or created to fulfill the task. Avoid staging unchanged files or unrelated changes. Use `git add <file>` specifically for each file and always verify the staged changes with `git status` or `git diff --staged` before committing.
- **Clear Messages:** Every commit must have a clear and descriptive message.

## 🛡️ Code Quality & Testing
- **No Broken Code:** NEVER commit code that has syntax errors, fails to compile, or breaks existing tests.
- **Local Verification:** Always run the project's linter, type-checker, and test suite (if available) locally before committing or pushing changes.

## 👀 Code Review & Pull Requests
- **No Self-Approval (Reviewer):** The `@reviewer` agent must NEVER blindly approve a PR. Approval is strictly contingent on a rigorous analysis of the `git diff`.
- **No Self-Approval (Developer):** The `@developer` agent cannot approve their own Pull Request or merge without explicit approval from a reviewer.
- **Completeness:** If the issue requires tests or documentation updates and they are missing, the reviewer MUST request changes.

## 🔐 Security & Environment
- **No Secrets:** Never commit, log, or print passwords, API keys, tokens, or sensitive environment variables in the output. Always use `.env.example` or mocked values in the code.

## 📊 Project Boards & Status Mapping
When updating the status of an issue (labels), you MUST also update the status on the associated Project Board (if any).

**Attention Agents:** To manipulate the board via CLI, you must:
1. Use `gh issue view <ISSUE_ID> --json projectItems` to get the Project ID and Item ID.
2. Identify the "Status" field ID in the project.
3. Use `gh project item-edit` to update the field value.

**Available Statuses on the Board (Default Mapping):**
- **Backlog:** Corresponds to `status: idea`, `status: need-spec`
- **To Do:** Corresponds to `status: ready-for-dev`
- **In Progress:** Corresponds to `status: in-progress`, `status: busy`
- **In Review:** Corresponds to `status: in-review`, `status: ready-for-merge`
