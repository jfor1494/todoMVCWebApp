# controller.py (Controlador)
import model
import datetime

def add_todo(todos, todo):
    now = datetime.datetime.now()
    timestamp = now.strftime("%d/%m/%Y a las %I:%M%p")
    todo_with_timestamp = f"{todo} creado el {timestamp}\n"
    if todo_with_timestamp in todos:
        return todos, "¡Este 'todo' ya está en tu lista!"
    else:
        todos.append(todo_with_timestamp)
        model.write_todos(todos)
        return todos, ""
