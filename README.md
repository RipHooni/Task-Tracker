# Task Manager
# https://roadmap.sh/projects/task-tracker
A simple command-line Task Manager built in Python that allows you to add, update, delete, list, and change the status of tasks. Tasks are stored in a JSON file (`tasks.json`).

## Features

- **Add Task:** Create and save new tasks.
- **Delete Task:** Remove tasks by ID.
- **List Tasks:** Display all tasks with details.
- **Update Task:** Modify the description of a task.
- **Mark In Progress:** Change a task's status to "In Progress".
- **Mark Done:** Mark a task as "Done".

## Setup & Usage

1. **Clone the Repo:**

   ```bash
   git clone https://github.com/yourusername/TaskManager.git
   cd TaskManager
   ```

2. **Run the Application:**

   Open a terminal in the project directory and run:

   ```bash
   python TaskManager.py
   ```

3. **Follow On-Screen Prompts:**

   After launching, you'll see a menu:
   - **1:** Add Task
   - **2:** Delete Task
   - **3:** List Tasks
   - **4:** Mark In Progress
   - **5:** Mark Done
   - **6:** Update Task
   - **7:** Exit

   Simply enter the corresponding number to select an option.

## How It Works

- **Task Storage:**  
  Tasks are saved in a JSON file (`tasks.json`). When the program starts, it loads existing tasks from the file. New tasks are appended and saved back to this file.

- **Task Structure:**  
  Each task is a dictionary with the following keys:
  - `id`: A unique identifier.
  - `description`: The description of the task.
  - `created_at`: Timestamp when the task was created.
  - `updatedAt`: Timestamp when the task was last updated.
  - `status`: The status of the task (e.g., "Incomplete", "In Progress", "Done").
