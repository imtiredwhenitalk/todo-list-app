from .task import Task  

def save_tasks_to_file(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
           
            file.write(f"{task.title}|{task.description}|{task.completed}\n")

def load_tasks_from_file(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    title, description, completed = parts
                    tasks.append(Task(title, description, completed == 'True'))
    except FileNotFoundError:
        pass
    return tasks

def validate_task_input(input_text):
    return bool(input_text.strip())  

def format_task_display(task):
    status = "✔️" if task.completed else "❌"
    return f"{status} {task.title}: {task.description}"