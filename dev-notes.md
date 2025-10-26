## If I forgot everything, do this first

1. Open Command Prompt
2. Go to the project folder:
   cd C:\Users\gamin\Desktop\task-tracker
3. Run:
   python task_tracker.py list
4. If that works, the CLI is fine.
5. If it crashes, run:
   python storage.py
   - If storage.py crashes -> problem is in storage / tasks.json
   - If storage.py works but task_tracker.py fails -> problem is in CLI logic

This tells me where to debug first.


## storage.py (data layer)

- This file is responsible for LOADING and SAVING all tasks.
- Only `storage.py` is allowed to talk directly to `tasks.json`.
  Other files should call `load_tasks()` and `save_tasks()` instead of opening the file themselves.

### load_tasks():
- Reads tasks.json from disk and returns a Python list.
- If the file doesn't exist or is invalid, we return [] instead of crashing.
- This keeps the app from blowing up on first run.

### save_tasks(tasks):
- Takes a Python list of task dicts and writes it back to tasks.json.
- Uses json.dump(..., indent=2) so the file is human-readable.


## tasks.json (the "database")

- This file stores the actual task list so that tasks stay saved after the program ends.
- It's just JSON. Example of what it could look like later:

[
  {
    "id": 1,
    "description": "Buy milk",
    "status": "todo"
  }
]

- The program will:
  - load this file at the start,
  - update it,
  - write it back.


## Running the CLI

Examples (these will grow over time):

python task_tracker.py list
    -> Show all tasks

python task_tracker.py add "Buy milk"
    -> (future) Add a new task with status "todo"

python task_tracker.py done 2
    -> (future) Mark task #2 as done

Note: We use sys.argv in task_tracker.py to read these command-line arguments.


## Progress Log

2025-10-26
- Set up Python project and confirmed we can run code from terminal
- Initialized Git and pushed repo to GitHub under correct identity
- Added tasks.json and storage.py (data layer / persistence)
- Confirmed we can load from disk using: python storage.py
- Started CLI flow in task_tracker.py (list command)
- Created dev-notes.md to document how the system works like a real project
