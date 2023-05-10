import tkinter as tk
from tkinter import ttk
from .file_handling import save_tasks


def add_task(root, task_entry, task_status):
    if isinstance(task_entry, ttk.Entry):
        task_text = task_entry.get()
    else:
        task_text = task_entry

    if task_text:
        task_container = ttk.Frame(root)

        task_var = tk.BooleanVar(value=False)

        task = ttk.Checkbutton(
            task_container, text=task_text, variable=task_var, style='CustomCheckbutton.TCheckbutton', command=lambda: complete_task(task_status, task_var, task_text))

        task.grid(row=0, column=0, sticky=tk.W)

        delete_button = ttk.Button(
            task_container, text="Delete", command=lambda: delete_task(root, task_container, "Deleted"))

        delete_button.grid(row=0, column=1, padx=5, sticky=tk.W)

        task_container.grid(sticky=(tk.W, tk.E))

        if isinstance(task_entry, ttk.Entry):
            task_entry.delete(0, tk.END)

        if task_status is not None:
            save_tasks("data/task_status.txt", task_status, task_text)


def delete_task(root, task_container, task_status):
    task = task_container.winfo_children()[0]
    if isinstance(task, ttk.Checkbutton):
        task_text = task.cget("text")
        task_container.destroy()

    # Save tasks to a separate file with the "Deleted" status.
    save_tasks("data/task_status.txt", task_status, task_text)


def complete_task(task_status, task_var, task_text):
    if task_var.get():
        task_status = "Completed"
        save_tasks("data/task_status.txt", task_status, task_text)
