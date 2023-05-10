import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("400x400")

    task_frame = create_task_frame(root)
    create_input_and_add_button(root, task_frame)
    root.mainloop()


def create_task_frame(root):
    task_frame = ttk.Frame(root, padding="10")
    task_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    return task_frame


def create_input_and_add_button(root, task_frame):
    task_entry = ttk.Entry(task_frame, width=20)
    task_entry.grid(row=0, column=0, padx=5, pady=5)

    add_task_button = ttk.Button(
        task_frame, text="Add task", command=lambda: add_task(root, task_entry))
    add_task_button.grid(row=0, column=1, padx=5, pady=5)


def add_task(root, task_entry):
    task_text = task_entry.get()
    if task_text:
        task_container = ttk.Frame(root)

        # create a BooleanVar to store the state of the checkbox
        task_var = tk.BooleanVar()

        # create the Checkbutton widget with the variable
        task = ttk.Checkbutton(
            task_container, text=task_text, variable=task_var)

        # add the Checkbutton to the task_container
        task.grid(row=0, column=0, sticky=tk.W)

        # create the Delete button with the command
        delete_button = ttk.Button(
            task_container, text="Delete", command=lambda: delete_task(task_container))

        # add the Delete button to the task_container
        delete_button.grid(row=0, column=1, padx=5, sticky=tk.W)

        # add the task_container to the root
        task_container.grid(sticky=(tk.W, tk.E))

        # clear the


        # clear the task entry
        task_entry.delete(0, tk.END)


def delete_task(task_container):
    task_container.destroy()


if __name__ == "__main__":
    main()
