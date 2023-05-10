import tkinter as tk
from tkinter import ttk
from .tasks import add_task, delete_task


def create_task_frame(root):
    task_frame = ttk.Frame(root, padding="10")
    task_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    return task_frame


def create_input_and_add_button(root, task_frame, add_task_function):
    task_entry = ttk.Entry(task_frame, width=20)
    task_entry.grid(row=0, column=0, padx=5, pady=5)

    add_task_button = ttk.Button(
        task_frame, text="Add task", command=lambda: add_task_function(root, task_entry, "Added"))

    add_task_button.grid(row=0, column=1, padx=5, pady=5)
