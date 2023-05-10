# Import the Tkinter library for creating the GUI
import tkinter as tk
# Import the ttk module from Tkinter for improved widgets
from tkinter import ttk


def main():
    # Create the main application window
    root = tk.Tk()
    # Set the title of the main window
    root.title("Task Manager")
    # Set the size of the main window (width x height)
    root.geometry("400x400")

    # Call other functions to create the app's components here

    # Start the main event loop for the application
    root.mainloop()


# Execute the main function when the script is run
if __name__ == "__main__":
    main()


def create_task_frame(root):
    # Create a Frame widget with padding to hold tasks
    task_frame = ttk.Frame(root, padding="10")
    # Place the task frame in the main window using the grid geometry manager
    task_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    # Return the created frame
    return task_frame
