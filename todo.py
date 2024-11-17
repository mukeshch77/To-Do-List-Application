import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        # Add a numbered format to the task
        task_listbox.insert(tk.END, f"{task_listbox.size() + 1}. {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Do you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")  
root.resizable(False, False)


root.config(bg="#eeeeee")  # Light gray background

# Motivational message above the typing area with purple text
motivation_label = tk.Label(root, text="“Great start! Add some tasks to get going.”", 
                            font=("Arial", 12, "italic"), fg="#9c27b0", bg="#f3e5f5", justify=tk.CENTER)
motivation_label.pack(pady=20)

# Entry widget for task input with a white background and gray border
task_entry = tk.Entry(root, width=30, font=("Arial", 14), borderwidth=2, relief="solid", bg="#ffffff", fg="#333333")
task_entry.pack(pady=10)

# Add button with purple background and white text
add_button = tk.Button(root, text="Add Task", command=add_task, width=20, font=("Arial", 12, "bold"), bg="#9c27b0", fg="white", relief="raised")
add_button.pack(pady=10)

# Listbox to display tasks with white background and gray text
task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE, font=("Arial", 12), bd=2, relief="sunken", bg="#ffffff", fg="#333333", selectbackground="#e1bee7", selectforeground="black")
task_listbox.pack(pady=10)

# Frame for the Delete and Clear buttons side by side
button_frame = tk.Frame(root, bg="#f3e5f5")
button_frame.pack(pady=10)

# Delete button with purple background and white text
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=15, font=("Arial", 12, "bold"), bg="#9c27b0", fg="white", relief="raised")
delete_button.pack(side=tk.LEFT, padx=10)

# Clear all tasks button with purple background and white text
clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks, width=15, font=("Arial", 12, "bold"), bg="#9c27b0", fg="white", relief="raised")
clear_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()
