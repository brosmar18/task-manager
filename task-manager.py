import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("400x400")

    style = ttk.Style()
    style.theme_use('classic')

    # Create custom checkbutton style
    style.configure('CustomCheckbutton.TCheckbutton',
                    background='white', foreground='black')
    style.map('CustomCheckbutton.TCheckbutton',
              indicatorcolor=[('selected', 'black')],
              background=[('!disabled', 'white')])

    task_frame = create_task_frame(root)
    create_input_and_add_button(root, task_frame)

    # Load tasks from the file.
    load_tasks(root, "tasks.txt")


    root.mainloop()

def load_tasks(root, file_name):
    try:
        with open(file_name, 'r') as file:
            for task_text in file:
                # Remove the newline character.
                task_text = task_text.strip()

                if task_text:
                    # Create a new task in the task manager with the task manager with the task text.
                    add_task(root, task_text)
    except FileNotFoundError:
        # if the file doesn't exist, create an empty one.
        open(file_name, 'w').close()

    except Exception as e:
        print(f"Error while loading tasks from file: {e}")

def save_tasks(file_name, task_status):
    with open(file_name, 'a') as file:
        file.write(f"{task_status}:\n")
        for task_container in root.winfo_children():
            if isinstance(task_container, ttk.Frame):
                task = task_container.winfo_children()[0]
                if isinstance(task, ttk.Checkbutton):
                    task_text = task.cget("text")
                    file.write(f"{task_text}\n")
        file.write("\n")

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
    # If task_entry is an Entry widget, get the entered text.
    if isinstance(task_entry, ttk.Entry):
        task_text = task_entry.get()
    else:
        task_text = task_entry

    if task_text:
        task_container = ttk.Frame(root)

        task_var = tk.BooleanVar(value=False)

        task = ttk.Checkbutton(
            task_container, text=task_text, variable=task_var, style='CustomCheckbutton.TCheckbutton')

        task.grid(row=0, column=0, sticky=tk.W)

        delete_button = ttk.Button(
            task_container, text="Delete", command=lambda: delete_task(task_container))

        delete_button.grid(row=0, column=1, padx=5, sticky=tk.W)

        task_container.grid(sticky=(tk.W, tk.E))

        if isinstance(task_entry, ttk.Entry):
            task_entry.delete(0, tk.END)

        # Save tasks to a separate file with the "Added" status
        save_tasks("task_status.txt", "Added")


def delete_task(task_container):
    task_container.destroy()

    # Save tasks to a separate file with the "Deleted" status.
    save_tasks("task_status.txt", "Deleted")


if __name__ == "__main__":
    main()
