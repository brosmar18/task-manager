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


def save_tasks(file_name, section_name, task_text):
    task_sections = {}

    with open(file_name, 'r') as file:
        current_section = None

        for line in file:
            line = line.strip()

            if line in ['Loaded:', 'Added:', 'Completed:', 'Deleted:']:
                current_section = line[:-1]

                if current_section not in task_sections:
                    task_sections[current_section] = []

            else:
                task_sections[current_section].append(line)

    if section_name not in task_sections:
        task_sections[section_name] = []

    task_sections[section_name].append(task_text)

    with open(file_name, 'w') as file:
        for section_name, section_tasks in task_sections.items():
            file.write(f"{section_name}:\n")
            for task in section_tasks:
                file.write(f"{task}\n")
            file.write("\n")



def clear_task_status_file(file_name):
    with open(file_name, 'w') as file:
        file.truncate()
