import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from home import HomePage
import pandas as pd


class SearchAndFilter:
    def __init__(self, root):
        self.root = root
        # self.root.title("Laptop Price Predictor")

        # Load the laptops data from the CSV file
        self.laptops_data = pd.read_csv("laptops.csv")
        self.init_component()

    def init_component(self):
        # Create a frame to contain the widgets
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create a search frame
        self.search_frame = ttk.Frame(self.frame)
        self.search_frame.grid(column=0, row=0, columnspan=2, sticky=(tk.W, tk.E))

        # Create a label for search
        self.search_label = ttk.Label(self.search_frame, text="Search:")
        self.search_label.grid(column=0, row=0, sticky=tk.W)

        # Create a search entry field
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.grid(column=1, row=0, padx=5, pady=5)

        # Create a button to apply filters
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_laptops)
        self.search_button.grid(column=2, row=0, padx=5, pady=5)

        # Create a filter frame
        self.filter_frame = ttk.Frame(self.frame)
        self.filter_frame.grid(column=0, row=1, sticky=(tk.W, tk.N))

        # Create filter options
        self.create_filters()

        # Create a scrollable text widget to display search results
        self.scrolltext = ScrolledText(self.frame, width=100, height=20, wrap=tk.WORD)
        self.scrolltext.grid(column=1, row=1, padx=5, pady=5, sticky=(tk.W, tk.N, tk.E, tk.S))

        # Add a button or link to the home page
        self.home_button = ttk.Button(self.frame, text="Home", command=self.go_to_home_page)
        self.home_button.grid(column=0, row=2, padx=20, pady=10)

    def create_filters(self):
        # Create filter labels and dropdown menus
        filter_labels = ["brand", "processor_brand", "processor_tier", "gpu_brand", "is_touch_screen", "display_size"]
        self.filter_vars = {label: tk.StringVar() for label in filter_labels}
        for i, label in enumerate(filter_labels):
            filter_label = ttk.Label(self.filter_frame, text=label + ":")
            filter_label.grid(column=0, row=i, sticky=tk.W)
            filter_menu = ttk.Combobox(self.filter_frame, textvariable=self.filter_vars[label])
            filter_menu.grid(column=1, row=i, padx=5, pady=5)
            # Populate dropdown menus with unique values from the corresponding column in the laptops data
            values = self.laptops_data[label.lower()].unique().tolist()
            values.insert(0, "")  # Add blank option at the beginning
            filter_menu['values'] = values

    def search_laptops(self):
        """Search laptops"""

        # Clear the previous search results
        self.scrolltext.delete('1.0', tk.END)

        # Get the search query
        search_query = self.search_entry.get().lower()

        # Filter the laptops data based on the search query
        filtered_laptops = self.laptops_data[
            self.laptops_data['Model'].str.lower().str.contains(search_query, na=False)]

        # Apply additional filters
        for label, var in self.filter_vars.items():
            if var.get():
                filtered_laptops = filtered_laptops[filtered_laptops[label.lower()] == var.get()]

        # Display the filtered laptops in the scrollable text widget
        self.scrolltext.insert(tk.END, "Search Results:\n")
        self.scrolltext.insert(tk.END, "-" * 100 + "\n")
        for _, row in filtered_laptops.iterrows():
            # Convert each row to a left-aligned string and insert it into the scroll text widget
            row_str = "".join(f"{col:<20}" for col in row)  # Left-align each column
            self.scrolltext.insert(tk.END, row_str + "\n")
            self.scrolltext.insert(tk.END, "-" * 100 + "\n")  # Add an underline after each row

    def go_to_home_page(self):
        # Destroy the current frame and create a new home page
        self.frame.destroy()
        home_page = HomePage(self.root)
