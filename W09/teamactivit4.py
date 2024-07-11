tasks = ["Task 1", "Task 2", "Task 3"]

while True:
    # Display the current tasks
    print("\nCurrent tasks:")
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

    # Ask the user for the action they want to perform
    print("\nOptions: add, remove, edit, change order, quit")
    action = input("What action would you like to perform? ").strip().lower()

    if action == "add":
        task_description = input("Enter the task description: ")
        tasks.append(task_description)
        print("Task added.")

    elif action == "remove":
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

    elif action == "edit":
        task_number = int(input("Enter the task number to edit: "))
        if 1 <= task_number <= len(tasks):
            new_task_description = input("Enter the new task description: ")
            tasks[task_number - 1] = new_task_description
            print("Task updated.")
        else:
            print("Invalid task number.")

    elif action == "change order":
        task_number = int(input("Enter the task number to move: "))
        new_position = int(input("Enter the new position for the task: "))
        if 1 <= task_number <= len(tasks) and 1 <= new_position <= len(tasks):
            task = tasks.pop(task_number - 1)
            tasks.insert(new_position - 1, task)
            print("Task order changed.")
        else:
            print("Invalid task number or position.")

    elif action == "quit":
        print("Thank you for using the task manager.")
        break

    else:
        print("Invalid option. Please try again.")
