import tkinter as tk
from tkinter import ttk
import pandas as pd


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

        # Add a title label
        title_label = ttk.Label(self.frame, text="Laptop Comparison Tool", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Create a listbox to display available laptops
        self.laptop_listbox = tk.Listbox(self.frame, selectmode=tk.MULTIPLE)
        self.laptop_listbox.grid(row=1, column=0, rowspan=5, padx=10)

        # Populate the listbox with laptop names from the dataset
        for laptop in self.laptops_data['Model']:
            self.laptop_listbox.insert(tk.END, laptop)

        # Add a button to compare selected laptops
        compare_button = ttk.Button(self.frame, text="Compare", command=self.compare_laptops)
        compare_button.grid(row=1, column=1, padx=10, pady=5)

        # Add a button to go back to the HomePage
        back_button = ttk.Button(self.frame, text="Back to Home", command=self.go_to_home_page)
        back_button.grid(row=2, column=1, padx=10, pady=5)

        # Create a text widget to display comparison results
        self.result_text = tk.Text(self.frame, width=50, height=20)
        self.result_text.grid(row=2, column=2, rowspan=4, padx=10, pady=5)

    def compare_laptops(self):
        # Clear the previous comparison results
        self.result_text.delete('1.0', tk.END)

        # Get the indices of selected laptops
        selected_indices = self.laptop_listbox.curselection()

        # Display specifications and prices of selected laptops
        for index in selected_indices:
            laptop = self.laptops_data.iloc[index]
            self.result_text.insert(tk.END, f"Model: {laptop['Model']}\n")
            self.result_text.insert(tk.END, f"Brand: {laptop['Brand']}\n")
            self.result_text.insert(tk.END, f"Price: {laptop['Price']}\n")
            # Add more specifications as needed
            self.result_text.insert(tk.END, "-" * 30 + "\n")

    def go_to_home_page(self):
        from home import HomePage
        # Destroy the current frame and create a new home page
        self.frame.destroy()
        home_page = HomePage(self.root)  # Create HomePage
