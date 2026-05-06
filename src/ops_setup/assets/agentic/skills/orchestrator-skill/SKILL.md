---
name: orchestrator-skill
description: Manage the development lifecycle by coordinating between specialists. Use when the squad needs to decide the next step for an issue, transition states, or delegate tasks to @developer, @reviewer, @product-manager, or @architect.
---

# Squad Orchestrator

## 🎯 Goal
Manage the lifecycle of GitHub Issues and PRs by ensuring the correct specialist skill is triggered based on the current state.

## 🧠 Decision Logic (State Machine)
Trigger the appropriate skill based on the `status:` labels:

1.  **Requirement Definition**:
    - `status: idea` or `status: need-spec` -> **Delegate to `@product-manager-skill`** for functional draft, then **`@architect-skill`** for technical design.
2.  **Approval Check**:
    - `status: spec-review` -> Check for human approval (e.g., "approved", "ok", "lgtm").
    - If Approved -> Transition to `status: ready-for-dev`.
    - If Rejected -> Move back to `status: need-spec`.
3.  **Implementation**:
    - `status: ready-for-dev` -> **Delegate to `@developer-skill`**.
4.  **Verification**:
    - `status: in-review` -> **Delegate to `@reviewer-skill`**.

## 📋 Core Workflow
1.  **Sync State**: Read `.agentic/GUARDRAILS.md` for project rules and status mappings.
2.  **Analyze Context**: Fetch issue/PR details using `gh issue view` or `gh pr view`.
3.  **Transition & Delegate**: Update labels using `gh issue edit` and explicitly invoke the next skill.
4.  **Board Sync**: Ensure the GitHub Project Board is updated following the SOP in `GUARDRAILS.md`.

## 🛡️ Guardrails
- **Language**: All comments must be in **Portuguese (pt-br)**.
- **Identification**: Use `<!-- agentic-comment -->` in all GitHub interactions.
- **De-noising**: Avoid commenting just to announce state changes; only comment when adding value or performing a handoff.
