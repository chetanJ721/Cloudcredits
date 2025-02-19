# Simple To-Do List in Python
# List to store tasks
tasks = []

def add_task():
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"✅ Task '{task}' added successfully!")

def mark_completed():
    """Mark a task as completed."""
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print(f"✔ Task '{tasks[index]['task']}' marked as completed!")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("📌 No tasks available.")
    else:
        print("\n📋 To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['task']} - {status}")
    print()

def main():
    """Main function to run the To-Do List."""
    while True:
        print("\n📌 To-Do List Menu:")
        print("1️⃣ Add Task")
        print("2️⃣ Mark Task as Completed")
        print("3️⃣ View Tasks")
        print("4️⃣ Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            mark_completed()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("🚀 Exiting To-Do List. Have a productive day!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
