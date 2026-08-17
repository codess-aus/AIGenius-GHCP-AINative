# Exercise 02A -- Parallel Execution with `/fleet`

> ⚠️ **Token cost warning:** `/fleet` spins up multiple subagents instead of one. If you're on a personal/paid plan and don't have a real backlog to justify it, it's fine to read through this exercise and skip running it live.

## Goal

Use the Copilot CLI's `/fleet` slash command to break one objective into independent sub-tasks and have subagents work them in parallel, instead of running the single-issue loop from Exercise 02 one task at a time.

## Pre-reqs

- You completed Exercise 02 (assigning an issue and observing the sandbox loop).
- Node.js 22+ installed (required by the Copilot CLI).
- A terminal with access to your `starter-app` clone.
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli) access on your plan.

## Set Up

### Step 1 -- Install the Copilot CLI

Pick whichever matches your OS:

```bash
# npm (any OS, requires Node.js 22+)
npm install -g @github/copilot

# Homebrew (macOS/Linux)
brew install --cask copilot-cli

# WinGet (Windows)
winget install GitHub.Copilot

# Install script (macOS/Linux)
curl -fsSL https://gh.io/copilot-install | bash
```

**✓ Validate:** Run `copilot --version` and confirm it prints a version number.

### Step 2 -- Authenticate

```bash
copilot
```

Follow the interactive prompts to sign in with your GitHub account the first time you launch it.

**✓ Validate:** Run `copilot` again; it should drop you straight into a session instead of asking you to sign in.

## Your Task

### Step 1 -- Open a session in your repo

From the root of your `starter-app` clone:

```bash
copilot
```

### Step 2 -- Give `/fleet` an objective with independent sub-tasks

Inside the interactive session, run:

```
/fleet Break the remaining Exercise 05 work into independent sub-tasks
(Azure OpenAI client setup, tag suggestion function, tests) and
work them in parallel
```

Or, non-interactively from your shell (the `--no-ask-user` flag is required outside interactive mode):

```bash
copilot -p "/fleet Break the remaining Exercise 05 work into independent sub-tasks (Azure OpenAI client setup, tag suggestion function, tests) and work them in parallel" --no-ask-user
```

### Step 3 -- Watch the orchestrator work

Copilot's main agent will:

1. Analyze your objective and decide whether it can be split into independent sub-tasks.
2. Act as an orchestrator, dispatching sub-tasks to subagents that can run in parallel.
3. Each subagent works in its own context window, sharing the same file system.
4. The orchestrator collects the results and reassembles them into one combined output.

### Step 4 -- Review the combined result

Once `/fleet` finishes, review what came back exactly as you would a single-agent PR: check the diff, check that tests were run, and confirm nothing sequential got parallelized incorrectly (for example, a sub-task that depended on another one's output).

## Tips for good `/fleet` prompts

- Be explicit about deliverables, e.g. list the exact files or modules you want each worker to own.
- Structure prompts so the split is obvious (e.g. "Create `docs/authentication.md`, `docs/endpoints.md`, `docs/errors.md`").
- Vague prompts may be handled sequentially instead of in parallel; `/fleet` only parallelizes work it can prove is independent.
- Avoid `/fleet` for sequential tasks (step 2 needs step 1's concrete output) or tightly coupled edits where workers would contend for the same file.

## Reflection Questions

- Did Copilot actually split your objective into parallel sub-tasks, or run them sequentially? Why?
- How did reviewing a `/fleet` result differ from reviewing a single-agent PR from Exercise 02?
- What kind of task in your own backlog would be a good fit for `/fleet`, and what kind wouldn't?

## Next Step

Continue to [Exercise 02B - Persistent Teams with `/squad`](../02b-squad-framework/README.md).
