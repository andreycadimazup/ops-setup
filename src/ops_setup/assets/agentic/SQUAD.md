# Agentic Squad (Full-Cycle Development)

## 🚀 End-to-End Life Cycle
This squad focuses on fast, high-quality delivery where the developer assumes full responsibility for the technical implementation, from understanding the context to submitting the PR and subsequent technical debate.

## 📋 The Workflow (State Machine)

| Current Status | Responsible Agent | Next Status (Success) | Expected Action |
| :--- | :--- | :--- | :--- |
| `status: idea` / `status: need-spec` | `@product-manager` & `@architect` | `status: spec-review` | Joint consensus: Functional + Technical spec in a single unified comment. |
| `status: spec-review` | **Human (User)** | `status: ready-for-dev` (via `@orchestrator`) | Reviews the spec and comments with "approved", "lgtm", or "ok". |
| `status: ready-for-dev` | `@developer` | `status: in-progress` | Starts the technical implementation. |
| `status: in-progress` | `@developer` | `status: in-review` | Completes implementation and opens a Pull Request. |
| `status: in-review` | `@reviewer` | `status: ready-for-merge` | Reviews the PR, debates technically, and approves/requests changes. |

## 💬 Communication Rules (Value-Added Only)
1.  **Meaningful Actions**: Comments should only be made for actions that contribute to the task's technical history or next steps (e.g., providing a spec, a PR summary, or review feedback).
2.  **Language Rule**: ALL comments made on GitHub (Issues or PRs) MUST be written in **Portuguese (pt-br)**.
3.  **Agentic Tag**: EVERY comment made by an agent MUST include the hidden tag `<!-- agentic-comment -->` at the end of the body to distinguish it from human interactions.
4.  **No Status-Only Noise**: Avoid comments that only report a label change or a simple delegation unless it's an exceptional case or an error.
5.  **Transparency**: Summarize what was accomplished and any technical decisions made.
6.  **No Raw File Paths**: NEVER mention agents by their file paths (e.g., `@.agentic/agents/dev.md`). ALWAYS use their `@name` handle (e.g., `@developer`).
7.  **Context in the PR**: All code-specific discussions between `@developer` and `@reviewer` must happen on the PR to keep the technical history centralized.

## 🧠 Persistence & Memory
- All decisions, plans, and **technical debates** are recorded as **comments** on the GitHub Issue or the PR itself.
- This ensures a transparent audit trail of why certain technical decisions were made.

## 🛠 Technical Guidelines (Security & Encoding)
- **UTF-8 Everything**: Always use UTF-8 encoding (especially on Windows/PowerShell: `$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8`).
- **Constructive Review**: Feedback should be technical, granular (inline comments), and focused on quality, not just pointing out errors.
- **Developer Autonomy**: The developer is encouraged to defend their implementation if they believe the reviewer's suggestion is incorrect or not ideal.

## 🛑 Project Guardrails (SDLC)
To adapt software development lifecycle (SDLC) rules per project without constantly modifying agent prompts, all agents MUST read and strictly follow the rules defined in `.agentic/GUARDRAILS.md`. This file contains customizable constraints, such as branching strategies, code quality rules, and PR approval policies.

## 👥 Available Specialists
- `orchestrator-skill`: Manages the flow and ensures the correct specialist is triggered via sub-agents.
- `developer-skill`: The executor and primary debater. Handles implementation and responses to feedback.
- `reviewer-skill`: The critic. Ensures quality and security, and initiates technical discussions.
- `product-manager-skill`: Specialist in the "What" and "Why" (Requirements).
- `architect-skill`: Specialist in the "How" (Technical Design).

---
*Autonomous, collaborative, and specialist-driven delivery.*
