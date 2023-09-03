# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to view all tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to remove a task from the list
def remove_task(task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
    else:
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed successfully!")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            view_tasks()
            task_index = int(input("Enter the task number to remove: "))
            remove_task(task_index)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
