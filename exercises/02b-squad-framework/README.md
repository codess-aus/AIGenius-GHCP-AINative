# Exercise 02B -- A Persistent Team with `/squad`

> ⚠️ **Token cost warning:** Squad, like `/fleet`, uses more AI usage than the single-agent loop from Exercise 02, since it can run multiple named agents. If you don't have a real project to justify it, it's fine to read through this exercise and skip running it live.

## Goal

Install the open source [Squad](https://github.com/bradygaster/squad) framework into a project and stand up a persistent team of named agents (frontend, backend, tester, lead, and so on) that stick around across issues and sessions, instead of Fleet's disposable, single-objective subagents.

## Pre-reqs

- You completed Exercise 02A (or at least read it) so you understand how `/fleet` differs from `/squad`.
- Node.js 22.5.0 or later, and npm.
- Git installed and configured.
- [GitHub CLI (`gh`)](https://cli.github.com/) installed, for Squad's Issues/PR features.
- The Copilot CLI installed (see Exercise 02A, Step 1).
- Squad is **alpha software** -- CLI commands may change between releases.

## Set Up

### Step 1 -- Verify your tooling

```bash
node --version
npm --version
git --version
gh --version
```

**✓ Validate:** All four commands print a version. Node.js must be 22.5.0 or higher.

### Step 2 -- Create (or pick) a project

You can try this on a scratch project first, or run it directly in your `starter-app` clone.

```bash
mkdir my-squad-demo && cd my-squad-demo
git init
```

**✓ Validate:** Run `git status`; you should see "No commits yet".

### Step 3 -- Install the Squad CLI

```bash
npm install -g @bradygaster/squad-cli
squad init
```

Squad walks you through setup step by step. If you'd rather start from a ready-made team:

```bash
squad init --preset default
```

This scaffolds a fully configured squad -- members, charters, and routing rules -- immediately.

**✓ Validate:** Check that `.squad/team.md` was created in your project.

### Step 4 -- Authenticate with GitHub

```bash
gh auth login
```

**✓ Validate:** Run `gh auth status`; you should see "Logged in to github.com". This is what lets Squad open Issues and PRs on your behalf.

## Your Task

### Step 1 -- Open Copilot with the Squad agent

```bash
copilot --agent squad --yolo
```

> The `--yolo` flag skips per-tool-call approval prompts. Squad makes many tool calls in a typical session, so without it you'd be approving constantly.

In VS Code, you can instead open Copilot Chat and select the **Squad** agent from the agent picker.

### Step 2 -- Describe what you're building

In the chat, tell Squad about your project:

```
I'm starting a new project. Set up the team.
Here's what I'm building: a CLI task manager in Python with Azure OpenAI tag suggestions.
```

### Step 3 -- Confirm the proposed team

Squad proposes a team of named specialists suited to the work (for example, a backend agent, a tester agent, a lead agent). Review the proposal and reply `yes` to confirm.

**✓ Validate:** Squad confirms the team is ready to work, and you can see the members reflected under `.squad/`.

### Step 4 -- Delegate work to the team

Ask Squad to pick up a real task, the same way you assigned an issue to Copilot in Exercise 02, but now routed to the specialist best suited to it:

```
Have the backend specialist add a --tag filter to the list command,
and have the tester write tests for it.
```

### Step 5 -- Observe persistence

Close the session and reopen it later (`copilot --agent squad --yolo` again, or reselect Squad in VS Code). Notice that your team, its context, and its prior decisions are still there under `.squad/`, unlike a Fleet run, which starts fresh each time.

## Upgrading Squad later

```bash
npm install -g @bradygaster/squad-cli@latest
squad upgrade
```

`squad upgrade` refreshes Squad-owned files and workflows, but never touches your `.squad/` team state, so your agents, decisions, and history are preserved.

## Reflection Questions

- How did delegating to a named specialist feel different from assigning the whole issue to one Copilot agent in Exercise 02?
- What did Squad remember between sessions that a fresh `/fleet` run would not?
- When would you reach for `/squad` instead of `/fleet`, and when would a single Copilot agent (Exercise 02) still be the right call?

## Next Step

Return to [Chapter 2 - Assign to Copilot](../../docs/chapter-2-assign-to-copilot.md) or continue to [Chapter 3 - Review a Draft PR](../03-review-a-pr/README.md).
