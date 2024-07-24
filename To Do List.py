class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: "{task}"')
    def update_task(self, task_number, new_task):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["task"] = new_task
            print(f'Task {task_number + 1} updated to: "{new_task}"')
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f'Task {task_number + 1} marked as completed.')
        else:
            print("Invalid task number.")

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f'{i}. {task["task"]} [{status}]')

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Update task")
        print("3. Complete task")
        print("4. List tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_number = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == "3":
            task_number = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.complete_task(task_number)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

