import streamlit as st
import model
import controller

todos = model.get_todos()

st.title("My todo App")
st.subheader("This is my todo app.")
st.write("this app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        model.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

new_todo = st.text_input(label="", placeholder="Add new todo...", key="new_todo")
if new_todo:
    todos, message = controller.add_todo(todos)
    if message:
        st.warning(message)
    else:
        st.session_state["new_todo"] = ""
        st.experimental_rerun()
