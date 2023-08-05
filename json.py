import json
from datetime import datetime 

def load_data():
    try:
        with open('to_do.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open('to_do.json', 'w') as f:
        json.dump(data, f)

class TaskManager:
    def __init__(self):
        self.data = load_data()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        save_data(self.data)

    def add_task(self, title, date_time):
        self.data.append({'title': title, 'date_time': date_time, 'done': False})

    def display_tasks(self):
        for i, task in enumerate(self.data):
            status = 'DONE' if task['done'] else 'NOT DONE'
            print(f"{i+1}- {task['title']} - {task['date_time']} - {status}")

    def mark_task_done(self, task_num):
        self.data[task_num-1]['done'] = True