# AI Genius Episode 1 — Presenter Script

**"Code with AI: GitHub Copilot for AI-Native Coding Workflows"**
1 hour · All skill levels

---

## Run of Show

| Time | Segment | Topic | Slide/Asset | Demo |
|------|---------|-------|-------------|------|
| 0:00 | Opening | What does AI-native actually mean? | Title slide / README | None |
| 0:05 | Live demo | Run the starter app, show it working | None | Terminal: `app.py` commands |
| 0:10 | Context | `copilot-instructions.md` + test suite | `.github/copilot-instructions.md` | Terminal: `pytest` |
| 0:15 | Exercise 01 | Write a well-formed issue together | Browser: Issues tab, template | None |
| 0:25 | Exercise 02 | Assign to Copilot, watch it work | None | Browser + Copilot App |
| 0:30 | Exercise 03 | Review the generated PR | None | Browser: PR diff, session log |
| 0:45 | Exercise 04 | Iterate via PR comments | None | Browser: PR comments, merge |
| 0:55 | Stretch (optional) | Azure Table Storage + Azure OpenAI | Architecture diagram | Code walkthrough, no live Azure needed |
| 0:58 | Closing | 5 Golden Rules + call to action | None | None |

> **Timing note:** the core loop (Segments 1 to 7) fits inside 55 minutes. Segment 8 (Azure stretch) is a flexible filler, use it if Exercise 02 to 04 finish early, or compress it to a 1 minute pointer to the exercises folder if you're running behind. This keeps the session honest to its 60 minute billing even when a live Copilot session runs long.

---

## Segment 1 — Opening (0:00 to 0:05)

*Screen: Title slide or repo README*

**SAY:**
> Welcome everyone. My name is Michelle. I'm a Developer Engagement Lead at Microsoft.
>
> Today we're going to do something a little different. I'm not going to teach you GitHub Copilot features. I'm going to change how you think about writing code.
>
> When I say "AI-native", I don't mean using Copilot to autocomplete a line of code. I mean treating it as a junior developer on your team, one that is incredibly fast, very literal, and needs clear direction to do its best work.
>
> In this session, you are the tech lead. You define **what** to build and **why**. Copilot handles **how**. Your job is to write good briefs and do smart reviews.
>
> By the end of this hour, you will have completed the full AI-native loop: write issue, delegate to Copilot, review the PR, iterate.

> 🔎 **Fun fact to drop here:** GitHub Copilot's coding agent runs your assigned issue inside an isolated GitHub Actions VM. It genuinely cannot touch production, cannot push directly to protected branches, and cannot merge on its own. Everything it does is captured in a session log you can read start to finish. What you're about to watch is the same sandboxed, auditable process a real engineering team would use, not a stage trick.

> 💡 **Pause here and ask:** "How many of you have used GitHub Copilot for code completion?" Then: "How many have used Copilot to write an entire feature from a GitHub Issue?" The second number is usually much smaller, that gap is exactly what this session closes.

---

## Segment 2 — Live Demo: The Starter App (0:05 to 0:10)

*Screen: Terminal in the starter-app directory*

**SAY:**
> Let me show you what we're working with. This is a Python command-line task manager. It sounds simple, but it's a real codebase with priorities, tags, due dates, timestamps, and an automated test suite behind it.
>
> This is the app you'll be extending today using Copilot.

**DO, type these commands live:**

```bash
cd starter-app

# Add a few tasks with different options
python app.py add "Deploy the API" --priority high --due 2025-12-31 --tag work
python app.py add "Buy coffee" --priority low --tag personal
python app.py add "Update README" --priority medium --tag work

# Show the full task list
python app.py list

# Show filters
python app.py stats
python app.py list --priority high
python app.py list --overdue
```

**SAY:**
> Notice that overdue tasks light up in red automatically, thanks to `rich` formatting. The app has filtering built in.
>
> Now, what if I want to store these tasks in Azure instead of a local file? And what if I want the app to automatically suggest a tag using AI when I add a task? That's what Copilot is going to build for us today.

---

## Segment 3 — Context: Instructions & Tests (0:10 to 0:15)

*Screen: VS Code or GitHub, `.github/copilot-instructions.md`*

**SAY:**
> Before Copilot writes a single line of code, it reads two things: your issue, and the copilot-instructions file.
>
> Think of `copilot-instructions.md` as the onboarding document you'd give a new developer. It tells Copilot what libraries to use, how to handle secrets, what the test approach is, and what "done" looks like.

**DO:**
1. Open `.github/copilot-instructions.md` on screen
2. Point out these specific sections:
   - The task schema (the JSON example)
   - The Azure Table Storage section (SDK name, env var names)
   - The "Never hardcode credentials" rule
   - The testing approach (pytest, mocking Azure calls)

**SAY:**
> This file is the reason Copilot will reach for the right Azure SDK instead of a random library it found on the internet. Context is everything.
>
> Now let me show you the test suite.

**DO:**

```bash
# Open starter-app/tests/test_tasks.py, briefly scroll through the class structure
# Then run it live:
python -m pytest tests/ -v
```

Point out: all tests passing, in under a second.

**SAY:**
> When Copilot adds the Azure backend, it has to keep every one of these tests passing. That's the safety net. And it will write new tests for the new code too.

> 🔎 **Interesting fact:** keeping the dependency list minimal (`click`, `rich`, `pytest`) isn't just good practice for humans, it directly improves what an AI coding agent can do with your repo. Fewer, well-known libraries mean less ambiguity for the model to resolve when it explores your codebase.

---

## Segment 4 — Exercise 01: Write the Issue (0:15 to 0:25)

*Screen: GitHub Issues tab, New Issue form*

**SAY:**
> Now it's your turn. Open the Issues tab on your forked repo and click New Issue.
>
> The golden rule of AI-native development is this: **your issue IS your prompt.** If you write a vague issue, you get vague code. If you write a precise specification, you get precise code.
>
> I'm going to write an issue live and talk through each section as I fill it in.

**DO, type or paste this issue:**

> **Title:** Migrate task storage to Azure Table Storage
>
> **Problem statement:**
> Tasks are stored in a local JSON file (`tasks.json`). This means data is lost when the machine changes and cannot be shared across devices. We need a cloud-backed storage option.
>
> **Desired behaviour:**
> - When `AZURE_STORAGE_CONNECTION_STRING` is set, tasks are stored in Azure Table Storage
> - When not set, the app falls back to the existing local JSON file
> - All existing CLI commands work identically, zero breaking changes
>
> **Acceptance criteria:**
> - [ ] A `storage.py` module with a `TaskStorage` protocol: `load() -> list[dict]` and `save(tasks) -> None`
> - [ ] `LocalStorage` implements `TaskStorage` using the existing JSON approach
> - [ ] `AzureTableStorage` implements `TaskStorage` using `azure-data-tables`
> - [ ] `app.py` calls `get_storage()` at startup to pick the right backend
> - [ ] `AZURE_STORAGE_CONNECTION_STRING` is loaded from `.env` using `python-dotenv`
> - [ ] Connection errors print a clear message and exit with code 1
> - [ ] `azure-data-tables` and `python-dotenv` added to `requirements.txt`
> - [ ] Tests mock Azure calls, no real API calls in tests
> - [ ] No connection strings or account keys in source code
>
> **Constraints:**
> Use `azure-data-tables` (not the older `azure-storage-table` SDK).
> Use `PartitionKey = "tasks"` and `RowKey = str(task["id"])`.
>
> **Submit the issue.**

**SAY:**
> Notice how specific I was. I named the module. I named the protocol. I named the method signatures. I named the environment variable.
>
> A human developer might fill in those gaps from experience. Copilot takes you literally. The more you specify, the closer the output is to what you actually want.
>
> You've got 5 minutes. Either follow along with the same issue, or write your own from Exercise 01 Option B, C, or D in the exercises folder.

> 🔎 **Interesting fact:** this is essentially prompt engineering wearing a GitHub Issues costume. The same principles, specificity, examples, constraints, that make a good LLM prompt make a good AI-native issue.

> 👀 **WATCH FOR:** walk around the room while participants write. Look for issues that are vague in the Acceptance Criteria section, gently prompt: "What exactly would done look like? What would you check before merging?"

---

## Segment 5 — Exercise 02: Assign to Copilot (0:25 to 0:30)

*Screen: GitHub Issue, Assignees panel on the right*

**SAY:**
> Now for the part that still feels a bit like magic the first time you see it.
>
> Open the issue you just submitted. On the right side, find the Assignees panel. Click the gear icon. Search for "Copilot" and assign it.

**DO:**
1. Demonstrate on your own issue
2. Click the Assignees gear, select Copilot
3. Show the confirmation comment that appears on the issue
4. Open the GitHub Copilot App on your desktop, go to My Work, find the active session
5. Put this on the main screen so everyone can see Copilot working

**SAY:**
> While we wait, watch what it does first. It doesn't start coding immediately. It **explores**. It reads `copilot-instructions.md`. It reads `app.py`. It reads the existing tests.
>
> That's exactly what a good developer does, understand the codebase before touching it.

> 👀 **WATCH FOR:**
> - Point out when Copilot references `copilot-instructions.md`, this is the payoff for Segment 3
> - Point out when it reads the existing tests, it's learning the test patterns
> - If the PR isn't ready by 0:30, don't wait, move to Exercise 03 framing and return when it's ready

> 💡 **Ask participants:** "What did you notice about how Copilot explored the codebase? What did it look at first?"

---

## Segment 6 — Exercise 03: Review the PR (0:30 to 0:45)

*Screen: Pull Requests tab, draft PR opened by Copilot*

**SAY:**
> Copilot has opened a draft PR. This is where your most important skill in AI-native development comes into play: **critical review**.
>
> Copilot is very good at writing plausible code. Plausible is not the same as correct, secure, or exactly what you asked for. You are the quality gate.
>
> Before we look at any code, read the session log in the PR description. Copilot explains every decision it made. This is like reading a PR summary from a junior developer, you understand the reasoning before you review the diff.

**DO:**
1. Open the draft PR
2. Read the session log aloud (at least the first paragraph)
3. Go to "Files changed" and walk through the checklist:

| Check | What to look for |
|-------|-----------------|
| `storage.py` exists | Has a `TaskStorage` protocol with `load()` and `save()` |
| `app.py` calls `get_storage()` | Not the old JSON functions directly |
| No hardcoded secrets | Zero connection strings or API keys visible |
| `requirements.txt` updated | Includes `azure-data-tables` and `python-dotenv` |
| New tests exist | Tests mock Azure calls, no real API calls |

**SAY:**
> I want you to find at least one thing to comment on. Not because Copilot did it wrong, maybe it didn't, but because the skill of writing precise PR feedback is itself what we're practising.
>
> Good PR comments are **specific.** Not "this could be better." Instead: "The error message on line 42 says connection failed but doesn't tell the user what env var to set. Can you include the variable name in the message?"

**DO:**
1. Demonstrate leaving a comment on a specific line in Files changed
2. Give participants 5 minutes to review and leave their own comment

> 🔎 **Interesting fact:** this checklist habit is what separates AI-native teams that ship reliable software from teams that ship plausible-looking bugs. Plausible is not the same as correct, and only a human reviewer catches that gap.

> 👀 **WATCH FOR:** redirect vague comments like "improve this", ask "What specifically? What would the improved version look like?" Celebrate anyone who catches a real security issue.

---

## Segment 7 — Exercise 04: Iterate (0:45 to 0:55)

*Screen: PR, Copilot responding to comments*

**SAY:**
> Here's the mental model I want you to hold: Copilot is a junior developer who is incredibly fast, very literal, and absolutely does not take offence at feedback.
>
> You don't throw away the work and start again. You give precise feedback and let it improve.

**DO:**
1. Watch Copilot pick up your comment and update the branch
2. Once it pushes the update, re-review the specific section you commented on
3. Ask yourself:
   - Did it address the feedback correctly?
   - Did it introduce any new issues in the process?
   - Is the PR ready to merge?
4. If you want another round, leave a second, more specific comment
5. When satisfied: change from Draft to Ready for Review, approve, merge

> 💡 **Good examples for a second-round comment:**
> - *"The validation rejects empty strings, but doesn't trim whitespace first. A name of spaces-only should also be rejected."*
> - *"The error says 'connection failed' but doesn't include the env var name so the user knows what to set."*
> - *"Can you extract the Azure entity mapping into its own function? It's mixed in with the save logic."*

**SAY:**
> Notice: **Copilot cannot merge.** The human is always the final gate. AI-native does not mean AI-autonomous. It means AI-collaborative. That's a deliberate design decision, not a limitation.
>
> How many rounds did it take? One? Three? The answer depends almost entirely on how precisely you wrote the original issue.

---

## Segment 8 — Stretch Goal: Azure + AI (0:55 to 0:58, optional filler)

*Screen: code walkthrough, no live Azure account required*

> **Use this segment only if Exercises 02 to 04 finished with time to spare. Otherwise, skip straight to Closing and point to Exercise 05 as homework.**

**SAY:**
> Let's look at what happens when the ask gets harder. There are two pre-written issues in the exercises folder: migrating storage to Azure Table Storage, which we just did, and adding Azure OpenAI tag suggestions.

**DO, show the architecture pattern:**

```
CLI (app.py)
    └── storage.py
            ├── LocalStorage (default)
            └── AzureTableStorage (env var activated)
```

**SAY:**
> The key design principle here is zero breaking changes. If `AZURE_STORAGE_CONNECTION_STRING` isn't set, it falls back to local JSON. Same for OpenAI, if the env vars aren't there, the app degrades gracefully rather than breaking.
>
> When you review this kind of PR, look extra hard for one thing: hardcoded credentials. That's the single most critical failure mode when delegating cloud integration work to an AI agent. Everything goes through environment variables and `python-dotenv`, never in source.

> 🔎 **Fun fact:** asking Copilot to mock cloud calls in tests, using `unittest.mock`, rather than hitting real Azure resources, is both a testing best practice and a cost and safety control. Your CI shouldn't be able to accidentally spin up billable cloud resources.

---

## Segment 9 — Closing (0:58 to 1:00)

*Screen: README, The 5 Golden Rules*

**SAY:**
> Let's land the plane. You just completed the full AI-native development loop.
>
> You wrote the issue. You delegated to Copilot. You reviewed the PR. You iterated via comments. You merged.
>
> That is the loop. And the better you get at each step, the faster and higher-quality your output becomes.

**Read the 5 Golden Rules aloud:**

1. **Write better issues**, your issue IS your prompt. Be specific.
2. **Review like a senior dev**, AI generates fast, humans verify smart.
3. **Use `copilot-instructions.md`**, give Copilot standing context about your project.
4. **Iterate, don't regenerate**, guide via comments rather than starting from scratch.
5. **Stay in the loop**, check the session log, understand what Copilot did and why.

**SAY:**
> For those of you who want to go further: Exercise 05 in the exercises folder has a ready-to-use issue for adding Azure OpenAI smart tag suggestions. Your homework: fork this repo, write the issue, assign it to Copilot, and run the loop on your own.
>
> You now have the skills to do that loop on any codebase, your work projects, your personal projects, anything.
>
> Thank you. I'll take questions.

---

## Emergency / Fallback Notes

**If Copilot is slow to start:**
- Show `copilot-instructions.md` and exercise READMEs while waiting, the preparation content fills 5 to 10 minutes naturally
- Ask participants to review the Exercise 05 pre-written issue and discuss: "What would you change? What's unclear?"

**If the PR contains a bug worth showing:**
- Use it. A real bug caught in review is the best possible demo of why human review matters
- Say: *"This is the payoff. Copilot is fast, but not infallible. You caught this, that's your value in the loop."*

**If someone asks about `copilot-instructions.md` being a security risk:**
- The file lives in `.github/`, it's part of the repo, just like the README. No secrets go in here, ever.
- Secrets live in environment variables or Azure Key Vault. That's why the instructions explicitly say so.

**If someone asks whether Copilot's coding agent can be a security risk in general:**
- The agent runs inside an isolated GitHub Actions VM per session, it has no persistent access beyond that run and cannot merge, push to protected branches, or touch production directly.
- The session log gives you a full audit trail of every decision and file it touched.

**If participants run out of time on Exercise 01:**
- It's fine, the Azure issue template in Exercise 05 is pre-written. They can copy-paste it.
- The learning is in the *reading and understanding* the acceptance criteria, not just in typing it.

**If running behind schedule overall:**
- Cut Segment 8 (Azure + AI stretch) entirely, it is designed as optional filler, not core content.
- Compress Segment 3 (Context) by skipping the live `pytest` run and just stating the test count and pass rate.
