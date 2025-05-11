import datetime
from datetime import datetime
import json

tasks = []
idPool = 0



# Define a task dictionary with default values
task = {
    "id": 0,
    "description": "Task description",
    "created_at": datetime.now().replace(microsecond=0),
    "updatedAt": datetime.now().replace(microsecond=0),
    "status": "Incomplete"
}

# Check if JSON file exists in current directory. If exists, load tasks from it else create a new one
try:
    with open('tasks.json', 'r') as file:
        data = json.load(file)
        for loadTasks in data:
            tasks.append(loadTasks)
            if loadTasks["id"] > idPool:
                idPool = loadTasks["id"] + 1
except FileNotFoundError:
    with open('tasks.json', 'w') as file:
        json.dump({}, file)
 
# Function to update task description
def update(task, description):
    task["description"] = description

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to mark task as in progress
def mark_inProgess(task):
    task["status"] = "In Progress"
    task["updatedAt"] = str(datetime.now().replace(microsecond=0))

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to mark task as done
def mark_Done(task):
    task["status"] = "Done"
    task["updatedAt"] = str(datetime.now().replace(microsecond=0))

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task and write to JSON file
def addTask():
    task["description"] = input("Enter a task: ")
    task["created_at"] = str(datetime.now().replace(microsecond=0))
    task["updatedAt"] = str(datetime.now().replace(microsecond=0))
    global idPool
    idPool += 1
    task["id"] = idPool
    newTask = task.copy()
    tasks.append(newTask)

    # Write the updated tasks list to the JSON file
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to delete a task by ID and delete from JSON file
def delete():
    taskId = int(input("Enter ID of task: "))
    for i in range(len(tasks)):
        print(i)
        if tasks[i]["id"] == taskId:
            tasks.pop(i)
            print("Task deleted!")
        
            # Write the updated tasks list to the JSON file
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
        break
    else:
        print("Task not found.")

# Function to list all tasks
def list():
    for i in range(len(tasks)):
      print(f"ID: {tasks[i]["id"]} | Description: {tasks[i]["description"]} | Status: {tasks[i]["status"]} | Created At: {tasks[i]["created_at"]} | Updated At: {tasks[i]["updatedAt"]}")

# Main function to display menu and handle user input
def main():
    while True:
        print("==== Task Manager ====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List Tasks")
        print("4. Mark In Progress")
        print("5. Mark Done")
        print("6. Update Task")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            addTask()
        elif choice == '2':
            delete()
        elif choice == '3':
            list()
        elif choice == '4':
            taskId = int(input("Enter ID of task: "))
            for i in range(len(tasks)):
                if tasks[i]["id"] == taskId:
                    mark_inProgess(tasks[i])
                    print("Task marked as In Progress!")
                    break
            else:
                print("Task not found.")
        elif choice == '5':
            taskId = int(input("Enter ID of task: "))
            for i in range(len(tasks)):
                if tasks[i]["id"] == taskId:
                    mark_Done(tasks[i])
                    print("Task marked as done!")
                    break
                else:
                    print("Task not found.")
        elif choice == '6':
            taskId = int(input("Enter ID of task: "))
            for i in range(len(tasks)):
                if tasks[i]["id"] == taskId:
                    newDescription = input("Enter new description: ")
                    update(tasks[i], newDescription)
                    print("Task updated!")
                    break
            else:
                print("Task not found.")

        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()