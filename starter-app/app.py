"""
Task Manager CLI -- AI Genius Episode 1 Workshop Starter App

A simple command-line task manager that demonstrates a real Python project
for attendees to extend using AI-native workflows with GitHub Copilot.

Usage:
    python app.py add "Buy groceries"
    python app.py list
    python app.py complete 1
    python app.py delete 1
"""

import json
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

TASKS_FILE = Path("tasks.json")
console = Console()


def load_tasks() -> list[dict]:
    """Load tasks from the JSON storage file.

    Returns:
        A list of task dictionaries. Returns an empty list if the file
        does not exist or cannot be parsed.
    """
    if not TASKS_FILE.exists():
        return []
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        console.print("[red]Warning: Could not read tasks file. Starting fresh.[/red]")
        return []


def save_tasks(tasks: list[dict]) -> None:
    """Persist tasks to the JSON storage file.

    Args:
        tasks: The list of task dictionaries to save.
    """
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def next_id(tasks: list[dict]) -> int:
    """Calculate the next available task ID.

    Args:
        tasks: The current list of tasks.

    Returns:
        An integer ID one greater than the current maximum, or 1 if there
        are no tasks.
    """
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


@click.group()
def cli() -> None:
    """A simple task manager. Manage your to-do list from the terminal."""


@cli.command()
@click.argument("name")
def add(name: str) -> None:
    """Add a new task.

    NAME is the description of the task to add.
    """
    name = name.strip()
    if not name:
        console.print("[red]Error: Task name cannot be empty.[/red]")
        sys.exit(1)
    if len(name) > 200:
        console.print("[red]Error: Task name cannot exceed 200 characters.[/red]")
        sys.exit(1)

    tasks = load_tasks()
    task = {
        "id": next_id(tasks),
        "name": name,
        "done": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    console.print(f"[green]Added task #{task['id']}:[/green] {name}")


@cli.command(name="list")
def list_tasks() -> None:
    """List all tasks."""
    tasks = load_tasks()

    if not tasks:
        console.print("[yellow]No tasks yet. Use 'add' to create one.[/yellow]")
        return

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Task")
    table.add_column("Status", width=10)

    for task in tasks:
        status = "[green]Done[/green]" if task["done"] else "[yellow]Pending[/yellow]"
        name = f"[strike]{task['name']}[/strike]" if task["done"] else task["name"]
        table.add_row(str(task["id"]), name, status)

    console.print(table)


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id: int) -> None:
    """Mark a task as complete.

    TASK_ID is the numeric ID of the task to complete.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                console.print(f"[yellow]Task #{task_id} is already marked as done.[/yellow]")
                return
            task["done"] = True
            save_tasks(tasks)
            console.print(f"[green]Task #{task_id} marked as complete.[/green]")
            return

    console.print(f"[red]Error: No task found with ID {task_id}.[/red]")
    sys.exit(1)


@cli.command()
@click.argument("task_id", type=int)
def delete(task_id: int) -> None:
    """Delete a task.

    TASK_ID is the numeric ID of the task to delete.
    """
    tasks = load_tasks()
    updated = [t for t in tasks if t["id"] != task_id]

    if len(updated) == len(tasks):
        console.print(f"[red]Error: No task found with ID {task_id}.[/red]")
        sys.exit(1)

    save_tasks(updated)
    console.print(f"[green]Task #{task_id} deleted.[/green]")


if __name__ == "__main__":
    cli()
