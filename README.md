# C2-Lab

**C2-Lab** is a beginner-friendly Python project built to explore task management, SQLite database operations, modular programming, and error handling through a local command-line application.

The project simulates a simple controller-and-agent workflow. Tasks are stored in a SQLite database, processed by an agent through a predefined executor, and assigned a final status based on the execution result.

> **Project scope:** This is a local educational simulation. It executes only predefined, harmless task types and does not provide remote command execution or a deployable command-and-control system.

## Features

- **SQLite task storage:** Persist tasks and their statuses in a local database.
- **Task management:** Add tasks, view pending tasks, and retrieve the next pending task.
- **Status tracking:** Track tasks through `pending`, `running`, `completed`, and `failed` states.
- **Modular architecture:** Separate database operations, task execution, agent logic, and application control.
- **Failure handling:** Mark unsupported tasks as failed and handle unexpected execution exceptions.
- **Automated checks:** Use Python assertions to verify executor results and task-status behavior.
- **Local persistence:** Keep task records between application runs.

## Architecture

The project is organized into four main modules.

| File | Responsibility |
|---|---|
| `main.py` | Provides the CLI, coordinates task processing, and updates task statuses. |
| `database.py` | Handles SQLite connections, task storage, retrieval, and status transitions. |
| `agent.py` | Receives a task record, invokes the executor, and returns the task ID and result. |
| `executor.py` | Executes supported simulated task types and returns their results. |

### Task execution flow

1. The user creates a task through the CLI.
2. The task is saved in SQLite with the initial status `pending`.
3. The controller retrieves the next pending task.
4. The controller changes its status to `running`.
5. The agent passes the task type to the executor.
6. The executor returns a result or `None` for an unsupported task.
7. The controller marks the task `completed` or `failed`.
8. If an unexpected exception occurs during processing, the controller catches it and attempts to mark the task `failed`.

```text
User
 |
 v
main.py (Controller)
 |
 v
database.py ---> SQLite database
 |
 v
agent.py
 |
 v
executor.py
 |
 v
Result returned to controller
 |
 +---- Valid result ------> completed
 |
 +---- Unsupported task --> failed
 |
 +---- Execution error ---> failed
```

## Supported Task Types

The executor currently supports two simulated task types.

| Task type | Expected result |
|---|---|
| `system_info` | `Simulated system information` |
| `health_check` | `Agent simulation is healthy` |

Any unsupported task type returns `None`. The controller interprets this as a failed task.

These are simulated results; the executor does not collect actual system information.

## Requirements

- Python 3
- SQLite support (included with most standard Python installations)
- Git (optional, for cloning the repository)

The project uses Python's built-in SQLite interface and does not require a third-party database server.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/harshphysicsquantum/C2-lab.git
cd C2-lab
```

Alternatively, download the repository and open the project folder locally.

### 2. Run the application

On Windows:

```powershell
python .\main.py
```

If your system uses `python3` instead, run:

```powershell
python3 main.py
```

The application initializes the database when it starts and displays a menu.

### 3. Use the menu

The current CLI provides these options:

1. **Add a task** — enter a supported or unsupported task type.
2. **View pending tasks** — display tasks waiting to be processed.
3. **Process next task** — process the next pending task.
4. **Exit** — close the application.

For a first run, add a `health_check` task and process it.

Expected result:

```text
Task result: Agent simulation is healthy
Task updated successfully
```

A supported task should finish with the status `completed`.

For a failure-path test, add a task named `unsupported_task` and process it. The executor returns `None`, and the controller marks the task `failed`.

## Task Statuses

The application uses task statuses to track execution.

| Status | Meaning |
|---|---|
| `pending` | The task is waiting to be processed. |
| `running` | The controller has started processing the task. |
| `completed` | The task returned a valid result. |
| `failed` | The task was unsupported or execution raised an exception. |

The database module validates permitted status transitions. The intended execution path is:

```text
pending -> running -> completed
                   \-> failed
```

An invalid transition, such as `completed -> running`, is rejected.

## Running the Tests

Run the test scripts from the project directory.

### Test executor behavior

```powershell
python .\test_executor.py
```

This checks that:

- `system_info` returns the expected simulated result.
- `health_check` returns the expected healthy-agent message.
- An unsupported task type returns `None`.

### Test task-status handling

```powershell
python .\test_status.py
```

This exercises valid transitions, rejects an invalid transition, checks a nonexistent task ID, and tests the `running -> failed` transition.

The tests use the project's SQLite database. They create task records, so repeated runs may add more records to the local database.

## Database and Local Files

The application uses a local SQLite database named `c2_lab.db`.

The database is created and initialized by the application when needed. It stores task records, including the task ID, task type, status, and creation timestamp.

The local database is intended for development and testing. It should not be committed to version control.

## Current Limitations

C2-Lab is a learning project, and its current implementation is intentionally small.

- The agent runs locally within the same Python application.
- Task types are predefined in the executor.
- Task results are simulated rather than collected from the operating system.
- The application uses a local SQLite database rather than a remote task service.
- It does not implement authentication, networking between separate agents and controllers, or concurrent task execution.
- The test scripts are simple Python scripts rather than a full test suite using a framework such as `pytest`.

## Learning Objectives

This project has helped me practise:

- Python functions, imports, and module separation.
- SQLite connections, queries, and persistent records.
- Task queues and retrieval of pending tasks.
- State transitions and input validation.
- Exception handling using `try` and `except`.
- Writing assertions to check expected behavior.
- Using Git and GitHub to track and publish changes.

## Future Improvements

Potential improvements include:

- Expand automated tests to cover more database edge cases.
- Improve error messages and logging.
- Add clearer test reporting.
- Separate application configuration from business logic.
- Introduce a dedicated test framework as the project grows.

## License

No license has been specified yet. Unless a license is added to the repository, others should not assume they have permission to redistribute or modify the project.
