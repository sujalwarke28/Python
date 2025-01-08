tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task(task_no):
    if 0 < task_no <= len(tasks):
        removed = tasks.pop(task_no - 1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions: 1. Add 2. View 3. Remove 4. Quit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_task(input("Enter task: "))
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task(int(input("Enter task number to remove: ")))
    elif choice == '4':
        break
    else:
        print("Invalid choice!")