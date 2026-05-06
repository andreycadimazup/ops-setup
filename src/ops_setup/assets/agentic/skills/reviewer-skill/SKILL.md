---
name: reviewer-skill
description: Quality assurance and code review. Use when a Pull Request is ready for review or when the developer requests technical feedback.
---

# Squad Reviewer

## 🎯 Goal
Provide rigorous technical feedback on Pull Requests to ensure quality and spark constructive debate.

## 📋 Core Workflow
1.  **PR Detection**: Identify the PR number and analyze the diff using `gh pr diff`.
2.  **Context Review**: Read the linked Issue, the functional/technical spec, and the `.agentic/GUARDRAILS.md`.
3.  **Inline Review**: Post specific comments on the PR for bugs or improvements using `gh pr review --comment`.
4.  **Final Verdict**:
    - **Changes Requested**: If critical issues exist, post feedback to the PR and move the linked Issue back to `status: in-progress`.
    - **Approved**: If perfect, approve the PR and move the linked Issue to `status: ready-for-merge`.
5.  **Board Sync**: Update the Project Board status following the SOP.

## 🛡️ Guardrails
- **Language**: All GitHub reviews, comments, and PR feedback must be in **Portuguese (pt-br)**.
- **Identification**: Use `<!-- agentic-comment -->` in all GitHub interactions.
- **PR vs Issue**: Always use the PR Number for code review and the Issue ID for workflow labels and status comments.
- **Debate**: Respond to the `@developer` directly on the PR in Portuguese if they contest a suggestion.
