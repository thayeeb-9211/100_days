# Project 3: Simple To-Do List
# Description: Create a simple command-line to-do list application where users can add, remove, and view tasks.

def display_menu():
    print("\n1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No tasks in the list.")

def todo_list():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

todo_list()
