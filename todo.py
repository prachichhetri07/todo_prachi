def display_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []
    
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
