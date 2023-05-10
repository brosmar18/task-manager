import tkinter as tk
from tkinter import ttk
from .file_handling import load_tasks, clear_task_status_file
from .tasks import add_task, delete_task
from .ui import create_task_frame, create_input_and_add_button
import os


def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)

    clear_task_status_file("data/task_status.txt")

    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("400x400")

    style = ttk.Style()
    style.theme_use('classic')

    style.configure('CustomCheckbutton.TCheckbutton',
                    background='white', foreground='black')
    style.map('CustomCheckbutton.TCheckbutton',
              indicatorcolor=[('selected', 'black')],
              background=[('!disabled', 'white')])

    task_frame = create_task_frame(root)
    create_input_and_add_button(root, task_frame, add_task)

    load_tasks(root, "data/tasks.txt", add_task)


    root.mainloop()


if __name__ == "__main__":
    main()
