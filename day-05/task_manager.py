import json
import os

class Task:
    def __init__(self, title, description, done=False):
        self.title = title
        self.description = description
        self.done = done

    def mark_complete(self):
        self.done = True

    def mark_incomplete(self):
        self.done = False

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["description"], data.get("done", False))

    def __str__(self):
        status = "[✓]" if self.done else "[X]"
        return f"{status} {self.title} - {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks
    
    def get_completed_tasks(self):
        return [task for task in self.tasks if task.done]
    
    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.done]

    def save_tasks(self, filepath="tasks.json"):
        try:
            with open(filepath, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=4)
            print(f"Tasks successfully saved to {filepath}.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self, filepath="tasks.json"):
        if os.path.exists(filepath):
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        self.tasks = [Task.from_dict(item) for item in data]
                    else:
                        self.tasks = []
            except Exception as e:
                print(f"Error loading tasks from {filepath}: {e}")
                self.tasks = []
        else:
            self.tasks = []


def display_menu():
    print("       --- TASK MANAGER ---       ")
    print("1. Add Task")
    print("2. List All Tasks")
    print("3. Mark Task as Complete")
    print("4. Save and Exit")


def main():
    manager = TaskManager()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "tasks.json")

    # Load existing tasks
    manager.load_tasks(db_path)

    while True:
        display_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            print("\n--- Add New Task ---")
            title = input("Enter task title: ").strip()
            if not title:
                print("Task title cannot be empty!")
                continue
            description = input("Enter task description: ").strip()
            new_task = Task(title, description)
            manager.add_task(new_task)
            print(f"Task '{title}' added successfully.")

        elif choice == '2':
            print("\n--- Your Tasks ---")
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks found. Add a task to get started!")
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")

        elif choice == '3':
            print("\n--- Mark Task as Complete ---")
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks to mark complete.")
                continue

            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            
            try:
                task_idx = int(input("\nEnter task number to mark complete: ")) - 1
                if 0 <= task_idx < len(tasks):
                    tasks[task_idx].mark_complete()
                    print(f"Task '{tasks[task_idx].title}' marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("\nSaving tasks and exiting. Goodbye!")
            manager.save_tasks(db_path)
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
