# Chapter 1 - Write a Well-Formed Issue

<!-- HERO IMAGE PLACEHOLDER: prompt below -->
<!-- IMAGE PROMPT: A flat, modern illustration of a developer typing a detailed spec into a glowing issue ticket, with an AI agent icon reading it in the background, dark navy background, gold accents, 16:9. -->
<!-- ALT TEXT: Developer writing a detailed feature issue while an AI agent reviews requirements in the background. -->

A strong issue is the single highest-leverage input in the AI-native loop. In practice, your issue becomes the spec, prompt, and success contract all at once.

## Why prompt quality matters in issues

When Copilot reads an issue, it converts natural language into engineering actions: files to inspect, APIs to call, tests to update, and constraints to obey. If your intent is vague, the implementation becomes guesswork.

Use this structure every time:

- **Problem statement**: What pain exists today?
- **Desired behavior**: What should users experience when done?
- **Acceptance criteria**: How will we verify success?
- **Constraints**: Which libraries/patterns must or must not be used?
- **Definition of done**: What final checks are mandatory?

## Worked issue example (Option C: `search` command)

### Title
`Add search command for task name/description with priority-ranked results`

### Problem statement
Users can add and list tasks, but cannot quickly find a specific task when the list grows.

### Desired behavior
A user can run `python app.py search "keyword"` to find matching tasks by name or description. Results should show high-priority tasks first and make matches easy to spot.

### Acceptance criteria
- [ ] Add `search` command to CLI with a required `keyword` argument
- [ ] Match against task `name` and `description` (case-insensitive)
- [ ] Sort matches by priority order: `high`, `medium`, `low`
- [ ] Highlight matching text in output
- [ ] Return a clear message if no tasks match
- [ ] Add tests for exact match, partial match, and no-match scenarios

### Constraints
- Reuse existing output style with `rich`
- Do not change task schema
- Keep existing commands unchanged

### Definition of done
- [ ] Existing tests pass
- [ ] New search tests pass
- [ ] Manual run demonstrates ranking and highlighting behavior

## Common mistakes

1. **Requirements are implied, not explicit**
   - Bad: "Add search support"
   - Better: include matching rules, sorting, display behavior, and test expectations.
2. **No constraints on dependencies or architecture**
   - This leads to unnecessary package additions or invasive refactors.
3. **No edge cases in acceptance criteria**
   - Include empty input handling, no-results behavior, and invalid values.
4. **Done criteria are missing verification steps**
   - Always require tests and a concrete manual check.
