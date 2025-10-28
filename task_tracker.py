import sys
from storage import load_tasks, save_tasks

def list_tasks():
    """
    Load tasks from storage and print them in a readable format.
    """
    tasks = load_tasks()

    if not tasks:
        print("No tasks yet.")
        return

    for task in tasks:
        # Each task is expected to look like:
        # { "id": 1, "description": "Buy milk", "status": "todo" }
        task_id = task.get("id", "?")
        desc = task.get("description", "(no description)")
        status = task.get("status", "unknown")

        print(f"[{task_id}] [{status}] {desc}")


def add_task(description):
    """
    Create a new task with a unique ID and default status 'todo',
    then save it to disk.
    """
    tasks = load_tasks()

    # Determine the next ID.
    if not tasks:
        next_id = 1
    else:
        existing_ids = [task.get("id", 0) for task in tasks]
        next_id = max(existing_ids) + 1

    new_task = {
        "id": next_id,
        "description": description,
        "status": "todo"
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f'Added task {next_id}: "{description}" [todo]')


def mark_done(task_id_str):
    """
    Mark a task as done by its ID, then save.
    task_id_str will be a string from the command line like "2".
    We'll convert it to int and update that task.
    """
    tasks = load_tasks()

    # Convert the ID from string ("2") to int (2)
    try:
        task_id = int(task_id_str)
    except ValueError:
        print(f"Error: '{task_id_str}' is not a valid task ID (must be a number).")
        return

    # Try to find the task with that ID
    found = False
    for task in tasks:
        if task.get("id") == task_id:
            task["status"] = "done"
            found = True
            break

    if not found:
        print(f"No task with id {task_id} found.")
        return

    # Save updated tasks
    save_tasks(tasks)
    print(f"Task {task_id} marked as done.")


def main():
    # Examples:
    #   python task_tracker.py list
    #   python task_tracker.py add "Buy milk"
    #   python task_tracker.py done 2
    #
    # sys.argv[0] -> script name
    # sys.argv[1] -> command ("list", "add", "done")
    #
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python task_tracker.py list")
        print('  python task_tracker.py add "task description"')
        print("  python task_tracker.py done <task_id>")
        return

    command = sys.argv[1].lower()

    if command == "list":
        list_tasks()

    elif command == "add":
        # Need a description after 'add'
        if len(sys.argv) < 3:
            print('Error: Missing task description.')
            print('Usage: python task_tracker.py add "Buy milk"')
            return

        description = sys.argv[2]
        add_task(description)

    elif command == "done":
        # Need an ID after 'done'
        if len(sys.argv) < 3:
            print("Error: Missing task ID.")
            print("Usage: python task_tracker.py done 2")
            return

        task_id_str = sys.argv[2]
        mark_done(task_id_str)

    else:
        print(f"Unknown command: {command}")
        print("Try one of:")
        print("  list")
        print('  add "task description"')
        print("  done <task_id>")


if __name__ == "__main__":
    main()
