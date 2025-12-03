import os

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("\n------ Your Tasks ------")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("------------------------\n")

# Add a new task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"Deleted task: {removed}\n")
    except:
        print("Invalid input!\n")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number completed: "))
        tasks[task_no - 1] = tasks[task_no - 1] + " ✔ (Completed)"
        print("Task marked as completed!\n")
    except:
        print("Invalid input!\n")

# Main Program
def main():
    tasks = load_tasks()
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task Completed")
        print("5. Exit")
        print("===========================\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting program.")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run program
main()
