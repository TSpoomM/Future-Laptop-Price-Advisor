import tkinter as tk
from tkinter import ttk
import pandas as pd
from home import HomePage


class ComparisonPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Laptop Comparison Tool")
        self.laptops_data = pd.read_csv("laptops.csv")
        self.init_component()

    def init_component(self):
        # Create a frame to contain the widgets
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create left and right frames
        self.left_frame = ttk.Frame(self.frame, borderwidth=2, relief="groove")
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.right_frame = ttk.Frame(self.frame, borderwidth=2, relief="groove")
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Add a title label
        title_label = ttk.Label(self.left_frame, text="Laptop Comparison Tool", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Create a listbox to display available laptops
        self.laptop_listbox = tk.Listbox(self.left_frame, selectmode=tk.MULTIPLE, width=65, height=20)
        self.laptop_listbox.grid(row=1, column=0, rowspan=5, padx=(10, 5),
                                 sticky='nsew')  # Adjust padx here

        # Populate the listbox with laptop names from the dataset
        for laptop in self.laptops_data['Model']:
            laptop_name = laptop.split("(", 1)[0]
            self.laptop_listbox.insert(tk.END, laptop_name)

        # Add a button to compare selected laptops
        compare_button = ttk.Button(self.left_frame, text="Compare", command=self.compare_laptops)
        compare_button.grid(row=1, column=1, padx=10, pady=5, sticky=tk.N)

        # Create a Treeview widget to display comparison results
        self.tree = ttk.Treeview(self.right_frame)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Define columns
        self.tree["columns"] = ("Brand", "Model", "Processor Brand", "Processor Tier", "Primary Storage Type",
                                "Primary Storage Capacity", "Display Size", "OS", "Price")

        # Format columns
        self.tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column
        self.tree.column("Brand", width=100, anchor=tk.W)
        self.tree.column("Model", width=200, anchor=tk.W)
        self.tree.column("Processor Brand", width=100, anchor=tk.W)
        self.tree.column("Processor Tier", width=100, anchor=tk.W)
        self.tree.column("Primary Storage Type", width=120, anchor=tk.W)
        self.tree.column("Primary Storage Capacity", width=150, anchor=tk.W)
        self.tree.column("Display Size", width=100, anchor=tk.W)
        self.tree.column("OS", width=100, anchor=tk.W)
        self.tree.column("Price", width=80, anchor=tk.W)

        # Headings
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Brand", text="Brand", anchor=tk.W)
        self.tree.heading("Model", text="Model", anchor=tk.W)
        self.tree.heading("Processor Brand", text="Processor Brand", anchor=tk.W)
        self.tree.heading("Processor Tier", text="Processor Tier", anchor=tk.W)
        self.tree.heading("Primary Storage Type", text="Primary Storage Type", anchor=tk.W)
        self.tree.heading("Primary Storage Capacity", text="Primary Storage Capacity", anchor=tk.W)
        self.tree.heading("Display Size", text="Display Size", anchor=tk.W)
        self.tree.heading("OS", text="OS", anchor=tk.W)
        self.tree.heading("Price", text="Price", anchor=tk.W)

        # Add a button to go back to the HomePage
        back_button = ttk.Button(self.right_frame, text="Back to Home", command=self.go_to_home_page)
        back_button.pack(side=tk.BOTTOM, pady=10)

    def compare_laptops(self):
        # Clear previous comparison results
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get the indices of selected laptops
        selected_indices = self.laptop_listbox.curselection()

        # Display specifications and prices of selected laptops
        for index in selected_indices:
            laptop = self.laptops_data.iloc[index]
            self.tree.insert("", "end", text="",
                             values=(laptop['brand'],
                                     laptop['Model'],
                                     laptop['processor_brand'],
                                     laptop['processor_tier'],
                                     laptop['primary_storage_type'],
                                     laptop['primary_storage_capacity'],
                                     laptop['display_size'],
                                     laptop['OS'],
                                     laptop['Price']))

    def go_to_home_page(self):
        # Destroy the current frame and create a new home page
        self.frame.destroy()
        home_page = HomePage(self.root)  # Create HomePage
