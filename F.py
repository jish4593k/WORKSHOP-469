import pickle
import tkinter as tk
from tkinter import messagebox
import torch

def add_to_bring(new_todo):
    if new_todo:
        brung.append(("Unknown", new_todo))
        with open('brung.pkl', 'wb') as pf:
            pickle.dump(brung, pf)

def show_choped_items():
    result_label.config(text="Items already chopped:")
    if brung:
        for item in brung:
            item_label = tk.Label(root, text=item[0] + " *bringing* " + item[1])
            item_label.pack()

def show_potluck_items():
    name_label = tk.Label(root, text="Enter your name:")
    name_label.pack()
    entry_name.pack()

def add_to_potluck(name, todos):
    if name and todos:
        brung.append((name, todos))
        with open('brung.pkl', 'wb') as pf:
            pickle.dump(brung, pf)

def show_additional_items():
    new_todo_label = tk.Label(root, text="Enter a new potluck item:")
    new_todo_label.pack()
    entry_new_todo.pack()
    add_todo_button.pack()

def on_add_todo():
    new_todo = entry_new_todo.get()
    add_to_bring(new_todo)
    messagebox.showinfo("Added", f"Item '{new_todo}' added to the list.")
    entry_new_todo.delete(0, tk.END)

def main():
    global root, brung, entry_new_todo

    root = tk.Tk()
    root.title("Shabu Potluck")

    with open('brung.pkl', 'rb') as fp:
        brung = pickle.load(fp)

    show_choped_items()
    show_potluck_items()

  
    root.mainloop()

if __name__ == "__main__":
    main()
