import csv
import os

FILENAME = "tasks.csv"

# Load tasks from CSV file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Avoid empty rows
                    task, status = row
                    tasks.append({"task": task, "completed": status == "True"})
    return tasks

# Save tasks to CSV file
def save_tasks(tasks):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for t in tasks:
            writer.writerow([t["task"], t["completed"]])

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        print("\n--- Your Tasks ---")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                status = " Done" if t["completed"] else " Pending"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        task_no = int(input("Enter task number to mark completed: "))
        if 0 < task_no <= len(tasks):
            tasks[task_no-1]["completed"] = True
            save_tasks(tasks)
            print(" Task marked as completed!")
        else:
            print(" Invalid task number.")

    elif choice == "4":
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no-1)
            save_tasks(tasks)
            print(f" Task '{removed['task']}' deleted.")
        else:
            print(" Invalid task number.")
            

    elif choice == "5":
        print(" Exiting To-Do List. Goodbye!")
        break

    else:
        print(" Invalid choice, try again.")
