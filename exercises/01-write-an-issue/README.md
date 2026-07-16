# Exercise 01 -- Write a Well-Formed Issue

## Goal

Learn to write GitHub Issues that give Copilot the context it needs to produce high-quality code.

## Why This Matters

In an AI-native workflow, your issue IS your prompt. The quality of Copilot's output is directly tied to the quality of the issue you write. A vague issue produces vague code. A specific, well-structured issue with clear acceptance criteria produces code that is far more likely to match your intent.

**Key insight:** You are not just describing a task for a human teammate. You are writing a specification that an AI agent will interpret and act on immediately.

---

## What Makes a Good AI-Native Issue

A well-formed issue for Copilot includes:

| Section | Purpose |
|---|---|
| **Problem statement** | What gap or pain point are you solving? |
| **Desired behaviour** | What should the user be able to do when this is done? |
| **Acceptance criteria** | A checklist of conditions that define "done" |
| **Constraints** | Libraries to use, things to avoid, performance requirements |
| **Definition of Done** | Final verification checklist |

---

## Your Task

1. Go to the **Issues** tab in this repo.
2. Click **New issue** and choose the **Feature Request** template.
3. Write an issue for one of the following features in the starter app:

   **Option A:** Add a due date to tasks
   > Users should be able to set an optional due date when creating a task, and see overdue tasks highlighted in the task list.

   **Option B:** Filter tasks by status
   > Users should be able to run a command to list only completed tasks, or only incomplete tasks, instead of always seeing everything.

   **Option C:** Export tasks to CSV
   > Users should be able to export their task list to a CSV file so they can open it in a spreadsheet tool.

4. Fill in **every section** of the template. Do not leave any section empty.
5. Submit the issue.

---

## Reflection Questions

- How specific did you have to be to clearly describe "done"?
- What information would Copilot need that a human teammate might already know?
- Did writing the acceptance criteria help you clarify your own thinking about the feature?

---

## Next Step

Once you've written your issue, move on to [Exercise 02 -- Assign to Copilot](../02-assign-to-copilot/README.md).
