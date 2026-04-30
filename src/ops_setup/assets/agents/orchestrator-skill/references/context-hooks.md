# Context Hooks (Dynamic Information)

The orchestrator and specialists use these "hooks" to fetch the most relevant context for the current task.

## 📥 Fetching Issue Context
To understand the requirement:
`gh issue view <ISSUE_ID> --json title,body,labels,comments`

## 📥 Fetching PR Context
To understand the current implementation status or feedback:
`gh pr view <PR_NUMBER> --json title,body,state,reviews,comments,statusCheckRollup`

## 📥 Fetching Project Board Context
To sync the status:
`gh issue view <ISSUE_ID> --json projectItems`

## 📥 Fetching File Diffs
To understand the changes being reviewed:
`gh pr diff <PR_NUMBER>`

---
**Standard Instruction:**
Always run these "hooks" at the beginning of the `orchestrator-skill` or `developer-skill` execution to ensure you are working with the latest state from GitHub.
