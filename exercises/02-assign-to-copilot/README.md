# Exercise 02 -- Assign the Issue to Copilot

## Goal

Delegate your issue to Copilot and observe it working in real time, then use Copilot Chat and the Copilot CLI to explore the codebase while you wait.

## The Mindset Shift

In the old workflow, after writing an issue you would open your IDE and start coding. In the AI-native workflow, you've just delegated this task to a team member. Your job is now to **guide and review**, not type every line yourself.

Copilot spins up a secure, isolated GitHub Actions VM to do this work. It cannot touch your production environment, cannot merge without your approval, and keeps a full session log so you can see exactly what it did and why.

---

## Your Task

### Step 1 -- Assign the Issue

1. Open the issue you wrote in Exercise 01.
2. In the **Assignees** panel on the right, click the gear icon.
3. Search for and select **Copilot** from the list.
4. Save the assignment.

You should see Copilot appear in the assignees list and a comment appear on the issue indicating it has picked up the work.

### Step 2 -- Open the Copilot App

1. Open the **GitHub Copilot App** on your desktop.
2. Navigate to the **My Work** view.
3. Find the active session for your issue.

### Step 3 -- Observe

Watch Copilot work. You will see it:

- Clone the repository into a secure sandbox
- Explore the codebase to understand the existing structure
- Make code changes
- Open a draft PR with a session log explaining its decisions

Do not intervene yet. Just observe.

### Step 4 -- Explore with Copilot Chat

While the agent session runs in the background, open **Copilot Chat** in your editor (VS Code, JetBrains, or the github.com chat panel) against your local clone of `starter-app`. Try asking it:

- `@workspace explain how app.py stores and loads tasks`
- `@workspace what would I need to change to add a new field to a task?`
- `/explain` on the `list` command in `app.py`

This is a different mode of working with Copilot: instead of delegating a whole task, you are having a conversation to build understanding. Notice how Chat answers are grounded in the actual files in your workspace, the same codebase the agent is currently editing in its sandbox.

### Step 5 -- Explore with the Copilot CLI

If you have the [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli) installed, try it from your terminal in the repo root:

```bash
gh copilot suggest "run the starter-app tests and show a summary of failures"
gh copilot explain "python app.py stats"
```

The CLI is useful for quick, one-off questions and shell command help without leaving the terminal, a lighter-weight complement to the full agent workflow you triggered in Step 1.

---

## What to Look For

While Copilot is working, notice:

- How does it explore the codebase before writing code?
- Does it reference the `copilot-instructions.md` file?
- How long does it take from assignment to draft PR?
- What does it include in the session log?
- How does the experience of Chat/CLI (interactive, immediate) differ from the agent (autonomous, asynchronous)?

---

## Reflection Questions

- What surprised you about how Copilot approached the task?
- Did it interpret your issue the way you intended?
- What would you write differently in the issue now that you've seen the result?
- When would you reach for Chat or the CLI instead of assigning an issue to the agent?

---

## Next Step

Once Copilot has opened a draft PR, move on to [Exercise 03 -- Review a PR](../03-review-a-pr/README.md).
