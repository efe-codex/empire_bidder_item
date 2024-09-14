import tkinter as tk
from tkinter import messagebox
import json
import os

# Load JSON data from file
def load_items():
    if os.path.exists('items.json'):
        with open('items.json', 'r') as f:
            return json.load(f)
    return {}

# Save JSON data to file
def save_items(items):
    with open('items.json', 'w') as f:
        json.dump(items, f, indent=4)

# Add item function
def add_item():
    item_name = item_entry.get()
    try:
        item_price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Price must be a number.")
        return
    
    if item_name and item_price > 0:
        items[item_name] = {"price": item_price}
        save_items(items)
        load_items_into_listbox()
        item_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Item name or price is invalid.")

# Remove item function
def remove_item():
    selected = item_listbox.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select an item to remove.")
        return
    
    item_text = item_listbox.get(selected[0])
    item_name = item_text.split(":")[0]
    
    if item_name in items:
        del items[item_name]
        save_items(items)
        load_items_into_listbox()

# Load items into the listbox
def load_items_into_listbox():
    item_listbox.delete(0, tk.END)
    for item, details in items.items():
        item_listbox.insert(tk.END, f"{item}: {details['price']}")

# Main GUI setup
items = load_items()
root = tk.Tk()
root.title("Item Editor")

# Organizing the layout

# Create a frame for the input fields and buttons
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

# Item Name
tk.Label(input_frame, text="Item Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
item_entry = tk.Entry(input_frame, width=30)
item_entry.grid(row=0, column=1, padx=5, pady=5)

# Price
tk.Label(input_frame, text="Price $:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
price_entry = tk.Entry(input_frame, width=30)
price_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons for adding and removing items
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, padx=10, pady=10)

add_button = tk.Button(button_frame, text="Add Item", command=add_item, width=20)
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = tk.Button(button_frame, text="Remove Item", command=remove_item, width=20)
remove_button.grid(row=0, column=1, padx=5, pady=5)

# Adjusted listbox size for longer texts and placing it below
listbox_frame = tk.Frame(root)
listbox_frame.grid(row=2, column=0, padx=10, pady=10)

item_listbox = tk.Listbox(listbox_frame, width=50, height=15)  # Increased width and height
item_listbox.pack()

# Load items into the listbox
load_items_into_listbox()

# Start the main loop
root.mainloop()
