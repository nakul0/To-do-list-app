import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage

def add_task():
    task = task_entry.get()
    if task:
        # Prevent adding duplicate tasks
        if task not in task_listbox.get(0, tk.END):
            task_listbox.insert(tk.END, task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Info", "Task already exists!")
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")

def clear_all():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("500x500")
root.config(bg="#F0F4F8")  # Light background color

# Window icon
# Uncomment and add your own path if you have an icon
# root.iconphoto(False, PhotoImage(file='icon.png'))

# Custom styling
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 12),
                padding=10,
                background="#3498DB",
                foreground="white")
style.map("TButton",
          background=[("active", "#2980B9")])

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 24, "bold"), bg="#F0F4F8", fg="#2C3E50")
title_label.pack(pady=20)

# Frame for entry and buttons
input_frame = tk.Frame(root, bg="#F0F4F8")
input_frame.pack(pady=10)

# Entry for new tasks
task_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 14), bd=2, relief="solid")
task_entry.grid(row=0, column=0, padx=10)

# Buttons
add_button = ttk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=10)

clear_button = ttk.Button(root, text="Clear All", command=clear_all)
clear_button.pack(pady=10)

# Listbox with scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame, orient="vertical")
task_listbox = tk.Listbox(frame, width=50, height=10, font=("Helvetica", 12), yscrollcommand=scrollbar.set,
                          selectbackground="#3498DB", selectforeground="white", bg="#ECF0F1", bd=2, relief="solid")
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Run the application
root.mainloop()
