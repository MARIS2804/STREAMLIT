import streamlit as st

tasks = ["Buy groceries", "Clean the house"]
completed_tasks = []

new_task = st.text_input("Add a new task:")

if new_task:
    tasks.append(new_task)

for i, task in enumerate(tasks):
    completed = st.checkbox(f"{i+1}. {task}", key=i)
    if completed:
        completed_tasks.append(task)
        tasks.remove(task)

if tasks:
    st.subheader("Remaining Tasks:")
    st.write(tasks)

if completed_tasks:
    st.subheader("Completed Tasks:")
    st.write(completed_tasks)

