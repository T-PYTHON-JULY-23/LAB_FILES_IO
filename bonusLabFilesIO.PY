import json
import datetime
from toDoList import modifyToDoList

def load_tasks():
    try:
        file = open('ToDoList.json', 'r', encoding="utf-8")
        return json.load(file)
        file.close()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    file = open('ToDoList.json', 'r', encoding="utf-8")
    json.dump(tasks, file)
    file.close()

def create_task(title, date_time):
    return {"title": title, "date_time": str(date_time), "done": False}

def add_task(title, date_time, tasks):
    tasks.append(create_task(title, date_time))
    save_tasks(tasks)

def delete_task(index, tasks):
    del tasks[index]
    save_tasks(tasks)

def mark_task_done(index, tasks):
    tasks[index]["done"] = True
    save_tasks(tasks)

def display_tasks(tasks):
    for i, task in enumerate(tasks):
        done_text = "DONE" if task["done"] else "NOT DONE"
        print(f"{i+1}- {task['title']} - {task['date_time']} - {done_text}")

def search_tasks(title, tasks):
    for i, task in enumerate(tasks):
        if title.lower() in task["title"].lower():
            done_text = "DONE" if task["done"] else "NOT DONE"
            print(f"{i+1}- {task['title']} - {task['date_time']} - {done_text}")

def main():
    tasks = load_tasks()

    while True:
        print("To-Do List\n")
        print("1- Display tasks")
        print("2- Add task")
        print("3- Delete task")
        print("4- Mark task as done")
        print("5- Search tasks")
        print("6- Exit\n")

        choice = input("Please enter your choice: ")

        if choice == "1":
            if not tasks:
                print("No tasks yet.")
            else:
                display_tasks(tasks)

        elif choice == "2":
            title = input("Enter the task title: ")
            date_string = input("Enter the date in YYYY-MM-DD format: ")
            time_string = input("Enter the time in HH:MM format: ")
            date_time = datetime.datetime.strptime(f"{date_string} {time_string}", "%Y-%m-%d %H:%M")
            add_task(title, date_time, tasks)

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
            else:
                index = int(input("Enter the task index to delete: ")) - 1
                delete_task(index, tasks)

        elif choice == "4":
            if not tasks:
                print("No tasks to mark as done.")
            else:
                index = int(input("Enter the task index to mark as done: ")) - 1
                mark_task_done(index, tasks)

        elif choice == "5":
            title = input("Enter the task title to search: ")
            search_tasks(title, tasks)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.\n")

    print("Goodbye!")

if __name__ == '__main__':
    main()
modifyToDoList()