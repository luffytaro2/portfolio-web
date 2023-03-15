def main():
    task_list = []
    while True:
        print("Select an option:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Exit")
        choice = input("Enter choice (1, 2, 3, or 4): ")
        if choice == "1":
            task = input("Enter task: ")
            task_list.append(task)
            print("Task added.")
        elif choice == "2":
            print("Task List:")
            for task in task_list:
                print("- " + task)
        elif choice == "3":
            task_index = int(input("Enter task number to mark as complete: ")) - 1
            if task_index >= 0 and task_index < len(task_list):
                task_list.pop(task_index)
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()

