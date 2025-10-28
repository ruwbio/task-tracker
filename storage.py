import json
import os

# This is the filename where we'll keep all our tasks.
TASKS_FILE = "tasks.json"


def load_tasks():
    """
    Read tasks from tasks.json and return them as a Python list.
    If the file doesn't exist or is empty/broken, return [].
    """
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as f:
        try:
            data = json.load(f)
            # We expect data to be a list, like: [ {task1}, {task2}, ... ]
            return data
        except json.JSONDecodeError:
            # File exists but isn't valid JSON for some reason.
            # We fail safe by returning an empty list instead of crashing.
            return []


def save_tasks(tasks):
    """
    Take a Python list of tasks and write it back to tasks.json as JSON.
    Overwrites the file completely with the new version.
    """
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def main():
    """
    This is just for testing storage.py directly.
    When we run: python storage.py
    we'll load the tasks and print them so we can confirm it's working.
    """
    tasks = load_tasks()
    print("Loaded tasks:", tasks)


if __name__ == "__main__":
    main()
