# Chapter 3 - Review a Draft PR

<!-- HERO IMAGE PLACEHOLDER: prompt below -->
<!-- IMAGE PROMPT: A flat illustration of a magnifying glass inspecting a pull request diff on a laptop screen, checklist floating beside it, dark navy background, gold accents, 16:9. -->
<!-- ALT TEXT: Reviewer inspecting a pull request diff with a quality checklist. -->

AI-generated code can look polished while still being wrong. Your review is the quality gate that protects reliability, security, and maintainability.

## Review in this order

1. **Session log first**: understand intent and assumptions.
2. **Diff second**: verify behavior-level correctness.
3. **Tests third**: confirm safety net coverage.

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
- [ ] No credentials or keys in source/log output
  - *Why:* secret leaks become incident response events.
- [ ] Inputs are validated before use
  - *Why:* blocks common injection and parsing issues.
- [ ] Failure paths do not reveal sensitive internals
  - *Why:* error output can leak implementation details.

### Dependencies
- [ ] New dependencies are justified and pinned appropriately
  - *Why:* each dependency adds supply-chain and maintenance cost.
- [ ] Imports are used and scoped narrowly
  - *Why:* reduces dead code and hidden coupling.

### Testing
- [ ] Existing tests still pass
  - *Why:* confirms no unintended breakage.
- [ ] New behavior has focused tests
  - *Why:* protects against regression in future iterations.

## High-signal review comment examples

- "Please trim whitespace before empty-name validation; `'   '` should fail too."
- "Can you add a test proving fallback behavior when `AZURE_STORAGE_CONNECTION_STRING` is missing?"
- "This helper mixes formatting and I/O. Please split for easier unit testing."
