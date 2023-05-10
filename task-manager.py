import tkinter as tk
from tkinter import ttk


def main():
    clear_task_status_file("task_status.txt")

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
    create_input_and_add_button(root, task_frame)

    load_tasks(root, "tasks.txt")

    root.mainloop()


def load_tasks(root, file_name):
    try:
        with open(file_name, 'r') as file:
            for task_text in file:
                task_text = task_text.strip()

                if task_text:
                    add_task(root, task_text, task_status="Loaded")
    except FileNotFoundError:
        open(file_name, 'w').close()

    except Exception as e:
        print(f"Error while loading tasks from file: {e}")


def save_tasks(file_name, task_status, task_text):
    with open(file_name, 'a') as file:
        file.write(f"{task_status}:\n")
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
        task_frame, text="Add task", command=lambda: add_task(root, task_entry, "Added"))

    add_task_button.grid(row=0, column=1, padx=5, pady=5)


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
            save_tasks("task_status.txt", task_status, task_text)


def complete_task(task_status, task_var, task_text):
    if task_var.get():
        task_status = "Completed"
        save_tasks("task_status.txt", task_status, task_text)



def delete_task(root, task_container, task_status):
    task = task_container.winfo_children()[0]
    if isinstance(task, ttk.Checkbutton):
        task_text = task.cget("text")
        task_container.destroy()

    # Save tasks to a separate file with the "Deleted" status.
    save_tasks("task_status.txt", task_status, task_text)


def clear_task_status_file(file_name):
    with open(file_name, 'w') as file:
        file.truncate()


if __name__ == "__main__":
    main()
