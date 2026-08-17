# Chapter 3 - Review a Draft PR

<!-- HERO IMAGE PLACEHOLDER: prompt below -->
<!-- IMAGE PROMPT: Flat illustration of a magnifying glass inspecting a pull request diff panel on a laptop screen, with a floating checklist (checkmarks and a shield icon for security) beside it. Dark navy background, gold accents, 16:9. -->
<!-- ALT TEXT: Reviewer inspecting a pull request diff with a quality checklist. -->

AI-generated code can look polished while still being wrong. Your review is the quality gate that protects reliability, security, and maintainability.

## Goal

Review Copilot's pull request with the critical eye of a senior developer, then leave a real, actionable review comment.

## Your Most Important Skill

In an AI-native workflow, **critical review** is your highest-value activity. Copilot is very good at generating plausible code. But plausible is not the same as correct, secure, or aligned with your intent.

You are the quality gate. The AI generates fast. You verify smart.

## Review in this order

1. **Session log first**: understand intent and assumptions.
2. **Diff second**: verify behavior-level correctness.
3. **Tests third**: confirm safety net coverage.

## Your Task

### Step 1 - Open the Draft PR

1. Go to the **Pull Requests** tab in your repo.
2. Open the draft PR that Copilot created from your issue.

### Step 2 - Read the Session Log

Before looking at the code diff, read the session log Copilot included in the PR description. This explains:

- How it interpreted your issue
- What decisions it made and why
- What it chose not to do

### Step 3 - Review the Diff

Go through the **Files changed** tab carefully. Use the expanded checklist below as your review guide.

## Expanded PR review checklist

### Correctness
- [ ] Matches issue acceptance criteria exactly
  - *Why:* prevents partial delivery and scope drift.
- [ ] Handles edge cases and invalid input
  - *Why:* user-facing robustness fails first at boundaries.
- [ ] Preserves existing behavior outside the feature
  - *Why:* regressions are costly and often subtle.

### Code quality
- [ ] Functions are focused and easy to read
  - *Why:* maintainability determines long-term velocity.
- [ ] Naming is clear and domain-accurate
  - *Why:* names are the fastest path to understanding logic.
- [ ] New public functions include hints/docstrings where expected
  - *Why:* supports onboarding and future agent accuracy.

### Security
- [ ] No hardcoded credentials, API keys, or secrets
  - *Why:* secret leaks become incident response events.
- [ ] Inputs are validated before use
  - *Why:* blocks common injection and parsing issues.
- [ ] Failure paths do not reveal sensitive internals
  - *Why:* error output can leak implementation details.

### Dependencies
- [ ] New dependencies are justified and declared in `requirements.txt`
  - *Why:* each dependency adds supply-chain and maintenance cost.
- [ ] Imports are used and scoped narrowly
  - *Why:* reduces dead code and hidden coupling.

### Testing
- [ ] Existing tests still pass
  - *Why:* confirms no unintended breakage.
- [ ] New behavior has focused tests
  - *Why:* protects against regression in future iterations.

## Your Task (Continued)

4. Work through the checklist above.
5. Leave **at least one comment** on the PR requesting a change or asking a clarifying question.

## High-signal review comment examples

Good comments are specific. Instead of:
> "This could be better"

Try one of these:
> "Can you add input validation to the task name field? It should reject empty strings and names longer than 200 characters."

> "Please trim whitespace before empty-name validation; `'   '` should fail too."

> "Can you add a test proving fallback behavior when `AZURE_STORAGE_CONNECTION_STRING` is missing?"

> "This helper mixes formatting and I/O. Please split for easier unit testing."

## Reflection Questions

- Did Copilot miss anything from the acceptance criteria?
- Were there any decisions in the session log you disagreed with?
- How did writing a detailed issue affect the quality of the PR?

## Next Step

Once you've left a review comment, move on to [Chapter 4 - Iterate via PR Comments](chapter-4-iterate.md).
