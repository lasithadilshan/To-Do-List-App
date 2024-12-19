import streamlit as st
import pandas as pd

# Set page title
st.title("To-Do List App")

# Load existing tasks or initialize an empty list
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# Input for adding a new task
new_task = st.text_input("Add a new task", key="new_task_input")

# Add task button
if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state["tasks"].append({"Task": new_task, "Completed": False})
        st.success("Task added!")
    else:
        st.warning("Task cannot be empty.")

# Display tasks in a table
if st.session_state["tasks"]:
    st.subheader("Your Tasks")
    tasks_df = pd.DataFrame(st.session_state["tasks"])
    for i, task in enumerate(st.session_state["tasks"]):
        col1, col2 = st.columns([4, 1])
        with col1:
            if task["Completed"]:
                st.write(f"~~{task['Task']}~~")
            else:
                st.write(task["Task"])
        with col2:
            if st.button("✅", key=f"complete_{i}"):
                st.session_state["tasks"][i]["Completed"] = True
            if st.button("❌", key=f"delete_{i}"):
                st.session_state["tasks"].pop(i)
                st.experimental_rerun()
else:
    st.info("No tasks yet. Add a task to get started!")

# Footer
st.write("---")
st.write("💡 Use this app to manage your daily tasks.")
