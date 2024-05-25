import cv2
import tkinter as tk
import numpy as np
import mediapipe as mp
import os
from tkinter import messagebox, ttk
from threading import Thread
import pyttsx3

# Define global variables
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
left_flag = None
left_count = 0
right_flag = None
right_count = 0

# Define file paths for both modes
visually_challenged_files = [
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\cruch.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\highknee.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\kneetoelbow.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\pushup.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\sidebend.py"
]

helper_files = [
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\curls2.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\jj.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\lunges.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\sidecrunch.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\situps.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\toetouch.py",
    r"C:\Users\sc\OneDrive\Desktop\exercise\ai exercises\Final\wipers.py"
]

def run_file(file_path, globals_dict):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            exec(code, globals_dict)
    except Exception as e:
        messagebox.showerror("Error", f"Error running file: {str(e)}")

def on_hover(event, text):
    engine.say(text)
    engine.runAndWait()

def on_click(file_path):
    global left_count, right_count, left_flag, right_flag
    # Run the selected file in a separate thread
    Thread(target=run_file, args=(file_path, globals())).start()

def on_right_click(event):
    root.quit()

def update_file_list(option):
    for widget in frame.winfo_children():
        widget.destroy()

    file_list = visually_challenged_files if option == "For the Visually Challenged" else helper_files

    for i, file_path in enumerate(file_list):
        row, col = divmod(i, 2)
        
        file_name = os.path.basename(file_path).replace(".py", "")
        label = tk.Label(frame, text=file_name, width=30, height=3)
        label.grid(row=row, column=col, padx=10, pady=10)
        
        # Bind events
        label.bind("<Enter>", lambda event, name=file_name: on_hover(event, name))
        label.bind("<Button-1>", lambda event, path=file_path: on_click(path))

# Create Tkinter window
root = tk.Tk()
root.title("File Runner")

# Increase window size
root.geometry("550x550")

# Create a dropdown menu
options = ["For the Visually Challenged", "For the Helper of the Visually Challenged"]
selected_option = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=selected_option, values=options, state="readonly")
dropdown.set("Select Mode")
dropdown.pack(pady=10)

# Create a frame to hold the file labels
frame = tk.Frame(root)
frame.pack(pady=20)

# Bind dropdown selection event
dropdown.bind("<<ComboboxSelected>>", lambda event: on_hover(event, selected_option.get()))
dropdown.bind("<<ComboboxSelected>>", lambda event: update_file_list(selected_option.get()))

# Bind right-click event to end execution
root.bind("<Button-3>", on_right_click)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Start Tkinter event loop
root.mainloop()
