# To-Do-List-Application
Build a simple to-do list application with tkinter.


# To-Do List Application

A simple **To-Do List** application built with Python's `tkinter` library. The app allows users to add, delete, and clear tasks with an intuitive GUI, featuring a motivational message to encourage task completion.

## Features

- **Add Tasks**: Users can input tasks via an entry field and add them to the list by clicking the "Add Task" button.
- **Delete Tasks**: Users can select a task from the list and delete it by clicking the "Delete Task" button.
- **Clear All Tasks**: Users can clear all tasks from the list with the "Clear All" button, after confirming the action.
- **Motivational Message**: A dynamic motivational message appears at the top of the app, encouraging the user to stay productive.
- **Task List**: The tasks are displayed in a `Listbox` with a numbered format, making it easier to track the order of tasks.


## How to Use

1. **Add a Task**: 
   - Type the task in the text input field at the top of the app.
   - Click the "Add Task" button to add the task to your list.
   
2. **Delete a Task**: 
   - Select a task from the list by clicking on it.
   - Click the "Delete Task" button to remove the selected task.
   
3. **Clear All Tasks**: 
   - Click the "Clear All" button to remove all tasks from the list. A confirmation dialog will appear before clearing the list.

4. **Motivational Message**: 
   - The app will display a motivational message that updates based on the number of tasks in the list. If there are no tasks, it will show, "Great start! Add some tasks to get going."

## Screenshots

Included some screenshots here like - how to look to-do list app, added some tasks and deleted a task.

## Example of How the App Looks

- **Add Task**: A text entry box and button to add tasks.
- **Tasks List**: A listbox showing added tasks, each with a numbered format.
- **Delete & Clear All**: Buttons for deleting a selected task or clearing the entire list.

## Code Explanatio

### Key Components:

- **Motivational Message**: The message dynamically changes based on the number of tasks in the list.
  - **`motivation_label`**: This label displays the motivational message at the top of the app.
  - The message changes to encourage the user to continue adding tasks.
  
- **Task Listbox**: The `Listbox` widget displays the tasks in a numbered list format.
  
- **Buttons**:
  - **Add Task**: Adds a new task to the list.
  - **Delete Task**: Deletes the selected task.
  - **Clear All**: Clears all tasks from the list after confirming the action.

### Functions:

- **`add_task()`**: Adds a task to the list when the "Add Task" button is clicked.
- **`delete_task()`**: Deletes the selected task from the list when the "Delete Task" button is clicked.
- **`clear_tasks()`**: Clears all tasks when the "Clear All" button is clicked, after asking for confirmation.

### Conclusion

The **To-Do List App** is a simple task manager built with Python's `tkinter`. It allows users to add, delete, and clear tasks, while displaying a motivational message. The app offers a clean and easy-to-use interface, making it a useful tool for staying organized and productive.
