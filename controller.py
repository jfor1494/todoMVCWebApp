import model
import datetime
import streamlit as st

def add_todo(todos):
    # Obtiene la fecha y hora actuales
    now = datetime.datetime.now()
    # Formatea la fecha y hora en el formato deseado
    timestamp = now.strftime("%d/%m/%Y a las %I:%M%p")

    todo = st.session_state["new_todo"]
    # Agrega la fecha y hora de creación al 'todo'
    todo_with_timestamp = f"{todo} creado el {timestamp}\n"

    # Verifica si el 'todo' ya existe en la lista
    if todo_with_timestamp in todos:
        # Si el 'todo' ya existe, muestra un mensaje al usuario
        st.warning("¡Este 'todo' ya está en tu lista!")
        return todos, "¡Este 'todo' ya está en tu lista!"
    else:
        # Si el 'todo' no existe, lo agrega a la lista
        todos.append(todo_with_timestamp)
        model.write_todos(todos)
        return todos, ""
