'''
Created on Jun. 15, 2024

Author: sachinpurewal
'''

tasks = []

while True:
    print("\n===== To-DO List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print()
        m_task = int(input("How many tasks do you want to add: "))
        
        for i in range(m_task):
            task = input("Enter your task: ")
            tasks.append({"task": task, "done": False})
            print("Task added!")
            
    elif choice == 2:
        print("\nTasks:")
        for index, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} [{status}]")
    
    elif choice == 3:
        print("\nTasks:")
        for index, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} [{status}]")
        
        task_no = int(input("Enter the task number to mark as done: "))
        if 0 < task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    
    elif choice == 4:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")