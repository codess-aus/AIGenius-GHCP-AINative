# Copilot Instructions for AIGenius-GHCP-AINative

This is a Python-based workshop project used in the AI Genius Episode 1 session on AI-native coding workflows with GitHub Copilot.

## Project Overview

The `starter-app` is a command-line task manager written in Python. It allows users to add, list, complete, and delete tasks. Tasks are stored in a local JSON file.

## Coding Conventions

- Use Python 3.10+ features and type hints throughout
- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Keep functions small and focused on a single responsibility
- Add docstrings to all public functions and classes
- Prefer f-strings for string formatting

## Project Structure

- `starter-app/app.py` -- main application entry point and CLI
- `starter-app/requirements.txt` -- Python dependencies

## Dependencies

- `click` -- for building the CLI interface
- `rich` -- for formatted terminal output

## Testing Approach

- Write unit tests using `pytest`
- Place tests in a `starter-app/tests/` directory
- Name test files `test_*.py`
- Test edge cases: empty task lists, invalid IDs, duplicate tasks

## What "Done" Looks Like

A feature is complete when:
- The CLI command works as described in the issue
- Input is validated and errors are handled gracefully
- The code has docstrings and type hints
- No hardcoded values or credentials appear in the code

## Style Notes

- Keep CLI output readable and user-friendly using `rich` formatting
- Error messages should be clear and actionable
- Use exit codes: 0 for success, non-zero for errors
