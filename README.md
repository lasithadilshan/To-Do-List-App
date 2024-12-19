---

# To-Do List Streamlit App

A simple, interactive **To-Do List** application built using **Streamlit**. This app allows users to add, complete, and delete tasks. The tasks are stored in the session state, making it easy to manage tasks during the session. The app ensures that duplicate tasks are not added and provides an intuitive interface for managing the task list.

## Features

- **Add Tasks**: Add new tasks to your to-do list.
- **Mark Tasks as Complete**: Mark tasks as completed, visually indicated by a strike-through effect.
- **Delete Tasks**: Remove tasks from the list.
- **Task Duplication Prevention**: Prevent adding the same task twice.
- **Session Persistence**: Tasks persist throughout the session using Streamlit's session state.
- **User-Friendly Interface**: Clean layout with interactive buttons for task actions (Add, Complete, Delete).

## Requirements

To run this app, you will need Python and the following dependencies:

- [Streamlit](https://streamlit.io/)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/lasithadilshan/to-do-list-app.git
    cd to-do-list-app
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**:
    ```bash
    streamlit run app.py
    ```

5. **Visit the app**: After running the command, Streamlit will display a local URL (usually `http://localhost:8501`) where you can access the app in your web browser.

## How to Use

1. **Add Tasks**: Type your task in the input box and click the "Add Task" button.
2. **Mark Tasks as Complete**: Click on the "✅ Complete" button next to a task to mark it as completed. The task will have a strike-through effect.
3. **Delete Tasks**: Click the "❌ Delete" button next to a task to remove it from the list.
4. **Task Duplication Prevention**: If you try to add a task that's already on the list, the app will notify you and prevent adding the same task again.

## File Structure

```
to-do-list-app/
├── app.py                # Main Streamlit app file
├── requirements.txt      # Python dependencies file
├── README.md             # Project documentation
└── .gitignore            # Git ignore file (optional)
```

### Requirements (`requirements.txt`)

Ensure that the `requirements.txt` includes Streamlit:

```
streamlit
```

## Contributing

If you would like to contribute to the project, feel free to fork the repository and submit a pull request. When contributing, please follow the following guidelines:

- Write clean and readable code.
- Add test cases if applicable.
- Provide detailed descriptions for your changes.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Notes:

- Replace `"https://github.com/lasithadilshan/to-do-list-app.git"` with the actual URL of your GitHub repository.
- If you have other dependencies in the app, don't forget to add them to `requirements.txt`.
- The instructions above assume that your project is structured as described. If your folder structure differs, adjust the commands accordingly.

Let me know if you need any other changes!
