# Task Manager 📝 — CLI Task Management System

This python project is made by Riccardo Gaglio, Unimi Data Science student.

## 📝 Task Manager
Task Manager is a modular Command Line Interface (CLI) application designed to help users organize their daily activities. 
The app focuses on clean **Object-Oriented Programming (OOP)** principles and persistent data storage, allowing users to create, track, and manage tasks across different sessions.

## 📌 Main Features
✔ Persistent JSON Storage (Data remains after closing)  
✔ Task Status Tracking (Pending vs. Completed)  
✔ Modular Package Architecture  
✔ Simple & Intuitive CLI Menu

## 📁 Project Structure
```
Task-Manager-Python/  
│  
├── main.py
├── requirements.txt
├── tasks.json 
├── .gitignore 
│ 
└── tasks/
    ├── init.py
    ├── task.py
    ├── task_data.py
    └── task_manager.py
```

## 🧠 How It Works

1. **Object Modeling** The `tasks/task.py` file defines the `Task` class. Every task is an object with a title, description, and completion status, making the code highly scalable and easy to maintain.

2. **Data Persistence** `tasks/task_data.py` acts as the Data Access Layer. It ensures that whenever a task is added or modified, the changes are written to `tasks.json`. This ensures user data is never lost between sessions.

3. **Logic Management** The `TaskManager` class in `tasks/task_manager.py` manages the list of tasks in memory. It bridges the gap between the raw JSON data and the user's actions, handling the indexing and state updates.

4. **User Interface** The `main.py` script provides a loop-based menu where users can interact with their task list using simple numeric inputs.

## 📦 Specific Requirements
```
colorama==0.4.6
```
You can install them via:
```
pip install -r requirements.txt
```
This project is using **Python version 3.13.0**

## 🚀 Running the App

1. **Clone the Repository**
```
git clone https://github.com/RicLv8/task_manager_project.git cd task_manager_project
```

2. **Setup Virtual Environment (Recommended)**
```
python -m venv .venv source .venv/bin/activate
```
3. **Run the Application**
```
python3 main.py
```

## 💾 Data Storage (Important Note)
The application uses a file named `tasks.json` in the root directory. 
- If the file does not exist, the app will create it automatically upon the first task entry.
- **Do not manually edit** the JSON file unless you are familiar with the format, as it may cause loading errors.

# 📘 Functions Reference
The project logic is divided into different files and folders to maintain the **Single Responsibility Principle**:

### `tasks/task.py`
* `to_dict()`: Converts a Task object into a dictionary format compatible with JSON storage.

### `tasks/task_data.py`
* `load_tasks()`: Reads the `tasks.json` file and returns a list of dictionaries. Handles file-not-found errors by returning an empty list.
* `save_tasks(tasks)`: Writes the current task list to the JSON file with indentation for readability.

### `tasks/task_manager.py`
* `add_task(title, description)`: Creates a new Task instance, appends it to the list, and triggers a save.
* `list_tasks()`: Returns all currently stored tasks for display in the UI.
* `complete_task(index)`: Marks a specific task as "Completed" based on its position in the list.
* `delete_task(index)`: Removes a task from the list and updates the storage.

### `main.py`
* `display_menu()`: Prints the available options to the terminal.
* `main()`: The main execution loop that captures user input and calls the appropriate TaskManager methods.