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

---

## Go Deeper (Optional): Scaling Up, From One Issue to a Fleet

> ⚠️ **Token cost warning:** Everything below is heavier on AI usage than the one-issue, one-agent loop you just ran. `/fleet` and `/squad` both spin up **multiple** agent sessions instead of one. If you're on a personal/paid plan and don't have a real project in mind to justify it, it's fine to just read this section and skip running it live.

So far you've done the smallest possible unit of AI-native work: one issue, one agent, one PR. That's the right place to start, but it doesn't scale to a real sprint, where you might have ten issues in flight. This is where `/fleet` and `/squad` come in, two different answers to the same question: *how do I go from one developer directing one agent, to a whole team directing many agents at once?*

### `/fleet`: parallel, stateless execution

`/fleet` is a Copilot CLI command built for parallel, stateless execution. You give it one objective, and an orchestrator agent breaks that objective into independent sub-tasks, checks which ones are unblocked, and runs them in parallel.

Think of it like this: if today's single Copilot agent is one developer picking up one issue, `/fleet` is like assigning ten related issues at once and having ten short-lived contractors work them simultaneously, then handing back the combined result.

### `/squad`: a persistent team of agents

`/squad` is a different shape of answer. It's not a single CLI command, it's an open source framework you install into your repo that creates a persistent team of named agents. Unlike Fleet's disposable sub-agents, Squad agents stick around across issues and sessions.

If Fleet is contractors for a single sprint, Squad is closer to hiring permanent specialists onto your team: they build context over time, and they can even use Fleet internally when they need a burst of parallel throughput.

### Why this maps to cloud-native architecture

- **`/fleet` is horizontal scaling for cognitive work.** A cloud-native app scales out stateless compute instances behind a load balancer to absorb load; `/fleet` scales out stateless sub-agents to absorb a backlog.
- **`/squad` is closer to a long-lived service mesh with persistent state.** Instead of ephemeral pods, you have specialized, addressable agents with their own memory and responsibilities, coordinating with each other.
- **Wave-based dependency scheduling** inside `/fleet`, run what's unblocked, wait, run the next wave, is conceptually the same DAG scheduling you already know from CI/CD pipelines or a Kubernetes job graph.

The takeaway: the single-issue loop from this exercise is the "hello world". `/fleet` and `/squad` are how that same loop scales to a real team's backlog without you personally babysitting every single agent session.

### How you'd scale this exercise out

If you had a real backlog instead of one issue, you could run something like:

```bash
/fleet Break the remaining Exercise 05 issue into independent sub-tasks
(Azure OpenAI client setup, tag suggestion function, tests) and
work them in parallel
```

The orchestrator splits the objective, dispatches the independent pieces at once, and reassembles the result as a single reviewable PR, rather than you running each sub-task through this exercise's loop one at a time.

### The safety model doesn't change

Neither `/fleet` nor `/squad` change the core safety model. Every sub-agent, whether disposable (Fleet) or persistent (Squad), still opens a PR, still cannot merge its own work, and still runs in an isolated sandbox with no production access, all governed by the same GitHub control plane you saw in Step 1 of this exercise. More agents means more parallel proposals for you to review, not less review.
