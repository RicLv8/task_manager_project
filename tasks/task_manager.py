# Core logic functions
from .task import Task
from .task_data import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task.to_dict())
        save_tasks(self.tasks)

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            save_tasks(self.tasks)