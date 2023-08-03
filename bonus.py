import json
import datetime


def display_todos(todos):
    print("Your To-Do List:")
    for i, todo in enumerate(todos):
        done = 'DONE' if todo['done'] else 'NOT DONE'
        print(f"{i + 1}- {todo['title']} - {todo['date']} - {done}")


def modify_todos(todos, operation):
    if operation == 'mark done':
        print("Enter the number of the task you want to mark as Done:")
    elif operation == 'search':
        print("Enter the title of the task you want to search for:")

    choice = input()
    if operation == 'mark done':
        try:
            index = int(choice) - 1
            if index >= 0 and index < len(todos):
                todos[index]['done'] = True
                print(f"{todos[index]['title']} is marked as Done.")
                save_todos(todos)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")
    elif operation == 'search':
        found = [todo for todo in todos if choice.lower() in todo['title'].lower()]
        for todo in found:
            done = 'DONE' if todo['done'] else 'NOT DONE'
            print(f"{todo['title']} - {todo['date']} - {done}")
        if not found:
            print("No matching tasks found.")


def save_todos(todos):
    with open("to_do.json", "w") as f:
        json.dump(todos, f)


def load_todos():
    try:
        with open("to_do.json") as f:
            todos = json.load(f)
    except FileNotFoundError:
        todos = []
    return todos


def main():
    todos = load_todos()
    while True:
        print("Do you want to add a new To-Do item? (y/n/exit)")
        choice = input().lower()
        if choice == 'y':
            todo = {
                'title': input("Enter To-Do item: "),
                'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'done': False
            }
            todos.append(todo)
            save_todos(todos)
        elif choice == 'n':
            display_todos(todos)
            for operation in ['mark done', 'search']:
                print(f"Do you want to {operation} a task? (y/n)")
                choice = input().lower()
                if choice == 'y':
                    modify_todos(todos, operation)
        elif choice == 'exit':
            break
        else:
            print("Invalid input. Please enter 'y', 'n', or 'exit'.")
    print("Thank you for using the To-Do program, come back again soon!")


if __name__ == "__main__":
    main()