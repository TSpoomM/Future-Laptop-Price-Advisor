import tkinter as tk
from tkinter import ttk
import pandas as pd
from home import HomePage  # Importing the HomePage class


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
        self.left_frame = ttk.Frame(self.frame)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.N, tk.E, tk.S))

        self.right_frame = ttk.Frame(self.frame)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky=(tk.W, tk.N, tk.E, tk.S))

        # Add a title label
        title_label = ttk.Label(self.left_frame, text="Laptop Comparison Tool", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Create a listbox to display available laptops
        self.laptop_listbox = tk.Listbox(self.left_frame, selectmode=tk.MULTIPLE, width=65, height=20)
        self.laptop_listbox.grid(row=1, column=0, rowspan=5, padx=(10, 5),
                                 sticky=(tk.W, tk.N, tk.E, tk.S))  # Adjust padx here

        # Populate the listbox with laptop names from the dataset
        for laptop in self.laptops_data['Model']:
            laptop_name = laptop.split("(", 1)[0]
            self.laptop_listbox.insert(tk.END, laptop_name)

        # Add a button to compare selected laptops
        compare_button = ttk.Button(self.left_frame, text="Compare", command=self.compare_laptops)
        compare_button.grid(row=1, column=1, padx=10, pady=5, sticky=tk.N)

        # Create a text widget to display comparison results
        self.result_text = tk.Text(self.right_frame, width=97, height=30)
        self.result_text.grid(row=1, column=0, padx=10, pady=5)

        # Add a button to go back to the HomePage
        back_button = ttk.Button(self.right_frame, text="Back to Home", command=self.go_to_home_page)
        back_button.grid(row=2, column=0, padx=10, pady=5)

    def compare_laptops(self):
        # Clear the previous comparison results
        self.result_text.delete('1.0', tk.END)

        # Get the indices of selected laptops
        selected_indices = self.laptop_listbox.curselection()

        # Display specifications and prices of selected laptops
        for index in selected_indices:
            laptop = self.laptops_data.iloc[index]
            self.result_text.insert(tk.END, f"Brand: {laptop['brand']}\n")
            self.result_text.insert(tk.END, f"Model: {laptop['Model']}\n")
            self.result_text.insert(tk.END, f"Processor Brand: {laptop['processor_brand']}\n")
            self.result_text.insert(tk.END, f"Processor Tier: {laptop['processor_tier']}\n")
            self.result_text.insert(tk.END, f"Number of Cores: {laptop['num_cores']}\n")
            self.result_text.insert(tk.END, f"Number of Threads: {laptop['num_threads']}\n")
            self.result_text.insert(tk.END, f"RAM Memory: {laptop['ram_memory']}\n")
            self.result_text.insert(tk.END, f"Primary Storage Type: {laptop['primary_storage_type']}\n")
            self.result_text.insert(tk.END, f"Primary Storage Capacity: {laptop['primary_storage_capacity']}\n")
            self.result_text.insert(tk.END, f"Secondary Storage Type: {laptop['secondary_storage_type']}\n")
            self.result_text.insert(tk.END, f"Secondary Storage Capacity: {laptop['secondary_storage_capacity']}\n")
            self.result_text.insert(tk.END, f"GPU Brand: {laptop['gpu_brand']}\n")
            self.result_text.insert(tk.END, f"GPU Type: {laptop['gpu_type']}\n")
            self.result_text.insert(tk.END, f"Touch Screen: {laptop['is_touch_screen']}\n")
            self.result_text.insert(tk.END, f"Display Size: {laptop['display_size']}\n")
            self.result_text.insert(tk.END, f"Resolution Width: {laptop['resolution_width']}\n")
            self.result_text.insert(tk.END, f"Resolution Height: {laptop['resolution_height']}\n")
            self.result_text.insert(tk.END, f"OS: {laptop['OS']}\n")
            self.result_text.insert(tk.END, f"Year of Warranty: {laptop['year_of_warranty']}\n")
            self.result_text.insert(tk.END, f"Price: {laptop['Price']}\n")
            # Add more specifications as needed
            self.result_text.insert(tk.END, "-" * 97 + "\n")

    def go_to_home_page(self):
        # Destroy the current frame and create a new home page
        self.frame.destroy()
        home_page = HomePage(self.root)  # Create HomePage
