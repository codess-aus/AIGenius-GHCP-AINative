# Chapter 4 - Iterate via PR Comments

<!-- HERO IMAGE PLACEHOLDER: prompt below -->
<!-- IMAGE PROMPT: A flat illustration of two speech bubbles looping arrows between a human and a robot icon refining a document together, dark navy background, gold accents, 16:9. -->
<!-- ALT TEXT: Human and AI exchanging feedback in an iterative loop. -->

Iteration is where AI-native teams gain speed without giving up quality. Good comments transform "almost right" output into production-ready work.

## Good vs. bad iteration comments

### Validation refinement

**Too vague (bad):**
> "Validation is wrong."

**Actionable (good):**
> "Please reject task names that are empty after trimming whitespace. Add a test for input `'   '` and verify it returns a user-friendly error."

### Architecture refinement

**Too vague (bad):**
> "Refactor this."

**Actionable (good):**
> "Move Azure table serialization into a helper function so storage and CLI concerns stay separate. Keep CLI command signatures unchanged."

### UX refinement

**Too vague (bad):**
> "Error message is confusing."

**Actionable (good):**
> "Update the error to include valid date format (`YYYY-MM-DD`) and a concrete example."

## Comment formula that works

Use this pattern:

1. **What is wrong now**
2. **What exact behavior is expected**
3. **How to verify (test/manual step)**

## When to iterate vs. abandon a PR

Iterate when:

- Core approach is correct but incomplete
- Most acceptance criteria are satisfied
- Remaining fixes are localized

Abandon/restart when:

- Architecture violates core constraints
- Security model is fundamentally broken
- Diff is too large/noisy to review confidently
- Rework would exceed rewrite effort

If you restart, write a tighter issue with explicit constraints and keep prior lessons in `copilot-instructions.md`.
