# Simple To-Do List Program

todo_list = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        print("Exiting... Have a productive day!")
        break

    else:
        print("Invalid choice. Please try again.")