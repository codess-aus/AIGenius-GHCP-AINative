# Chapter 2 - Assign to Copilot

![AI-native loop diagram showing issue to agent to PR workflow](assets/ai-native-loop.png)

Assigning an issue is where the workflow shifts from maker mode to lead mode. You define what to build; Copilot executes in a controlled environment.

## Goal

Delegate the issue you wrote in Chapter 1 to Copilot and observe it working in real time.

## The Mindset Shift

In the old workflow, after writing an issue you would open your IDE and start coding. In the AI-native workflow, you've just delegated this task to a team member. Your job is now to **guide and review**, not type every line yourself.

Copilot spins up a secure, isolated GitHub-hosted environment (similar to an Actions VM) to do this work. It cannot touch your production environment, cannot merge without your approval, and keeps a full session log so you can see exactly what it did and why.

## What happens in the secure sandbox

After assignment, Copilot runs in an isolated environment:

1. Clones the target repository and checks out a working branch.
2. Reads project structure, issues, and instructions (including `copilot-instructions.md`).
3. Plans edits and applies code changes.
4. Runs validation steps (tests/lint/build when available).
5. Opens or updates a draft PR with a session log.

This isolation matters: no direct access to your local machine, no silent merge, and transparent change history.

## How `copilot-instructions.md` influences output

`copilot-instructions.md` acts as persistent repository context. In this workshop repo it defines:

- Python 3.10+, typing, and style expectations
- Testing approach (`pytest`, isolated fixtures)
- Azure patterns for env vars and SDK usage
- Security expectations (no hardcoded credentials)

Think of this file as your team's "house rules" for every AI-generated change.

## Your Task

### Step 1 - Assign the Issue

1. Open the issue you wrote in Chapter 1.
2. In the **Assignees** panel on the right, click the gear icon.
3. Search for and select **Copilot** from the list.
4. Save the assignment.

You should see Copilot appear in the assignees list and a comment appear on the issue indicating it has picked up the work.

### Step 2 - Open the Copilot App

1. Open the **GitHub Copilot App** on your desktop.
2. Navigate to the **My Work** view.
3. Find the active session for your issue.

### Step 3 - Observe

Watch Copilot work. You will see it:

- Clone the repository into a secure sandbox
- Explore the codebase to understand the existing structure
- Make code changes
- Open a draft PR with a session log explaining its decisions

Do not intervene yet. Just observe.

## What the session log contains

The session log is your audit trail. Expect to see:

- What files Copilot explored first
- Why it chose certain implementation paths
- Commands run for validation
- Any failures and subsequent fixes
- Final summary of completed work

Review this before reviewing the diff; it helps you catch mismatches between your intent and Copilot's assumptions.

## Quick observer checklist

- Did Copilot interpret the issue correctly?
- Did it follow repo-specific instructions?
- Did it test what it changed?
- Did it explain tradeoffs and limitations?

## Reflection Questions

- What surprised you about how Copilot approached the task?
- Did it interpret your issue the way you intended?
- What would you write differently in the issue now that you've seen the result?

## Next Step

Once Copilot has opened a draft PR, move on to [Chapter 3 - Review a Draft PR](chapter-3-review-a-pr.md).
