import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="To-Do List App", layout="centered")
st.title("✅ To-Do List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []  # Initialize tasks as an empty list

# Function to add a new task
def add_task(task):
    if task.strip():  # Check for non-empty task
        st.session_state["tasks"].append({"Task": task, "Completed": False})
        st.success("Task added!")
    else:
        st.warning("Task cannot be empty. Please enter a valid task.")

# Function to mark a task as complete
def complete_task(index):
    st.session_state["tasks"][index]["Completed"] = True
    st.success(f"Task '{st.session_state['tasks'][index]['Task']}' marked as completed!")

# Function to delete a task
def delete_task(index):
    task_name = st.session_state["tasks"][index]["Task"]
    del st.session_state["tasks"][index]  # Delete task from session state
    st.success(f"Task '{task_name}' deleted!")
    st.experimental_rerun()  # Refresh app after task deletion

# Input form for adding tasks
with st.form("task_form", clear_on_submit=True):
    new_task = st.text_input("Add a new task", placeholder="Enter your task here...")
    submitted = st.form_submit_button("Add Task")
    if submitted:
        add_task(new_task)

# Display tasks
if st.session_state["tasks"]:
    st.subheader("Your Tasks")
    for i, task in enumerate(st.session_state["tasks"]):
        col1, col2, col3 = st.columns([6, 2, 2])  # Define layout for task display
        with col1:
            if task["Completed"]:
                st.markdown(f"~~{task['Task']}~~")  # Strike-through for completed tasks
            else:
                st.markdown(task["Task"])
        with col2:
            if not task["Completed"] and st.button("✅ Complete", key=f"complete_{i}"):
                complete_task(i)
        with col3:
            if st.button("❌ Delete", key=f"delete_{i}"):
                delete_task(i)  # Delete task and refresh app
else:
    st.info("No tasks yet. Add a task to get started!")

# Footer
st.write("---")
st.caption("Made with ❤️ using Streamlit")
