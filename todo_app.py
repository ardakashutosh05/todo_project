import tkinter as tk
from tkinter import messagebox
import os

TODO_FILE = "todo.txt"

print("🔁 Starting To-Do App...")

# Load tasks from file
def load_tasks():
    print("📄 Loading tasks from todo.txt...")
    if not os.path.exists(TODO_FILE):
        print("❗ todo.txt not found. Starting with empty task list.")
        return []
    with open(TODO_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    print(f"✅ Loaded {len(tasks)} tasks.")
    return tasks

# Save tasks to file
def save_tasks():
    print("💾 Saving tasks to todo.txt...")
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("✅ Tasks saved.")

def add_task():
    task = entry.get()
    if task:
        print(f"➕ Adding task: {task}")
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Empty Field", "Please enter a task!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        print(f"🗑️ Deleting task: {task}")
        tasks.remove(task)
        listbox.delete(index)
        save_tasks()
    else:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        if not task.endswith(" ✅"):
            print(f"✔️ Marking task as done: {task}")
            task += " ✅"
            tasks[index] = task
            listbox.delete(index)
            listbox.insert(index, task)
            save_tasks()
    else:
        messagebox.showwarning("Select Task", "Please select a task to mark as done.")

# GUI Setup
print("🪟 Setting up GUI window...")
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x450")
root.config(padx=10, pady=10)

tasks = load_tasks()

# Entry Field
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Add Button
add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 12))
listbox.pack(pady=10)

# Load existing tasks
print("🔁 Displaying tasks in listbox...")
for task in tasks:
    listbox.insert(tk.END, task)

# Buttons
done_btn = tk.Button(root, text="Mark Done", width=15, command=mark_done)
done_btn.pack(pady=2)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=2)

print("✅ App is running. GUI should now be visible.")
root.mainloop()
