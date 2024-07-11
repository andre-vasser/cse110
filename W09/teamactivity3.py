program_running = True
tasks=["Computer Settings"]
print("add")
print("remove")
print("edit")
print("change_order")
print("quit")

while (program_running):
    action = input("What would you like to do?: ")
    
    if action == "add":
        task = input("What number do you want to add?: ")
        tasks.append(task)
    elif action == "remove":
        task = input("What task would you like to remove?")
        tasks.remove(task)
    elif action == "edit":
        old_task = input("What task would you like to edit?: ")
        new_task = input("Please Enter the new task: ")
        index = tasks.index(old_task)
        tasks[index] = new_task
        
    elif action == "change order":
        task_num_old = input("What number do you want to change? :")
        task_num_new = input("Enter the new number: ")
        task = 
    elif action == "quit":
        program_running = False
        
    for i in tasks:
        print(i)