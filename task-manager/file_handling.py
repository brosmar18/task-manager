def load_tasks(root, file_name, add_task_func):
    try:
        with open(file_name, 'r') as file:
            for task_text in file:
                task_text = task_text.strip()

                if task_text:
                    add_task_func(root, task_text, task_status="Loaded")
    except FileNotFoundError:
        open(file_name, 'w').close()

    except Exception as e:
        print(f"Error while loading tasks from file: {e}")


def save_tasks(file_name, task_status, task_text):
    with open(file_name, 'a') as file:
        file.write(f"{task_status}:\n")
        file.write(f"{task_text}\n")
        file.write("\n")


def clear_task_status_file(file_name):
    with open(file_name, 'w') as file:
        file.truncate()
