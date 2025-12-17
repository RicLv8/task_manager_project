# User interface
from tasks.task_manager import TaskManager
import sys
    
def display_menu():
    print("\n--- 📝 TASK MANAGER ---")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("-----------------------")

def main():
    manager = TaskManager()
    print("--- Task Manager ---")

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            tasks = manager.list_tasks()
            if not tasks:
                print("\nYour task list is empty!")
            else:
                print("\nYOUR TASKS:")
                for idx, task in enumerate(tasks):
                    status = "✅" if task['completed'] else "❌"
                    print(f"{idx}. [{status}] {task['title']}: {task['description']}")

        elif choice == '2':
            title = input("Enter task title: ")
            desc = input("Enter task description: ")
            manager.add_task(title, desc)
            print("Task added successfully!")

        elif choice == '3':
            try:
                idx = int(input("Enter the task number to complete: "))
                manager.complete_task(idx)
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == '4':
            try:
                idx = int(input("Enter the task number to delete: "))
                manager.delete_task(idx)
                print("Task deleted!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == '5':
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
