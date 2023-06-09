import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    my_todo = st.session_state["new_todo"] + "\n"
    todos.append(my_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todoapp")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key='new_todo' )



