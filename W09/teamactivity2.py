# Create a program that allows the user to manage a list of tasks.
#The user can add tasks, remove tasks, edit tasks, change the order in witch
#they appear on the list. with each task numbererd starting from 1

#1. Create a list named 'tasks' with some initial tasks
#2. Display the list with each task numbered
# 3. Ask the user what action they want to perform: add a task, remove a task, edit, change task order, or quit.
# 4. If 'add', prompt for the task description and add it to the end of the list.
# 5. If 'remove', prompt for the task number and remove the corresponding task.
# 6. If 'edit', prompt for the new task content.
# 7. If 'change order', prompt for the current task number and the new position number, then move the task.
# 8. Repeat the process until the user decides to quit the program.
# 9. Show the current tasks after each action.
# 10. When the user quits, thanks the user for using your program.

tasks = ["Task 1", "Task 2", "Task 3"]

while True:
    print("\nCurrent tasks:")
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

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
