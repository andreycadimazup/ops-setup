---
name: developer-skill
description: Full-cycle software implementation. Use when a requirement needs to be coded, bugs fixed, or technical feedback on a PR needs to be addressed.
---

# Squad Developer

## 🎯 Goal
Implement high-quality code and manage technical discussions in PRs while ensuring all changes are thoroughly researched and verified.

## 📋 Core Workflow

### 1. Research & Planning
- **Context Fetch**: Read the Issue (`gh issue view`) and PR feedback (`gh pr view --json comments,reviews`).
- **Deep Investigation**: ALWAYS use the `codebase_investigator` tool to understand architecture and dependencies before writing code.
- **Draft Plan**: Create a task list for implementation, including test strategies.
- **Handoff Comment**: Move issue to `status: in-progress` and post a summary of the plan (in Portuguese).

### 2. Implementation & Testing
- **Iterative Dev**: Apply changes in small, logical chunks.
- **Verification**: Run project-specific linters, type-checkers, and tests.
- **Batch Operations**: Use the `generalist` sub-agent for multi-file refactors or repetitive patterns.

### 3. Delivery
- **Atomic Commits**: Stage and commit ONLY explicitly modified or created files.
- **PR Creation**: If not existing, create a PR with a descriptive body (in Portuguese) including:
    - Change summary.
    - Technical rationale.
    - Verification steps.
    - "Fixes #<ISSUE_ID>".
- **Handoff**: Comment on the issue with the PR link and move it to `status: in-review`.

## 🛡️ Guardrails
- **Debate First**: If a `@reviewer` suggestion is questionable, reply on the PR (in Portuguese) explaining why instead of blindly implementing it.
- **Project SOP**: Follow all rules defined in `.agentic/GUARDRAILS.md`.
- **Language**: All GitHub comments, commit messages, and PR descriptions must be in **Portuguese (pt-br)**.
- **Identification**: Use `<!-- agentic-comment -->` in all GitHub interactions.
