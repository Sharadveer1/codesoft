import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    status = "✔" if task["done"] else "✗"
                    print(f"{i}. [{status}] {task['task']}")

        elif choice == "2":
            new_task = input("Enter a new task: ").strip()
            if not new_task:
                print("Task cannot be empty.")
                continue
            tasks.append({"task": new_task, "done": False})
            save_tasks(tasks)
            print("Task added.")

        elif choice == "3":
            if not tasks:
                print("No tasks to mark complete.")
                continue
            try:
                task_num = int(input("Enter task number to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            if not tasks:
                print("No tasks to delete.")
                continue
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Deleted task: {removed['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
