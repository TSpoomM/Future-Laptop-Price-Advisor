"""My search and filter page"""

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import pandas as pd


class SearchAndFilterPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Search and Filter Tool")
        self.laptops_data = pd.read_csv("laptops.csv")
        self.init_component()

    def init_component(self):
        # Create a frame to contain the widgets
        self.frame = ttk.Frame(self.root, padding="20", style="Background2.TFrame")
        self.search_frame = ttk.Frame(self.frame, style="Search.TFrame")
        self.filter_frame = ttk.Frame(self.frame, style="Filter.TFrame")

        self.frame.grid(column=0, row=0, sticky='nsew')

        # Configure grid row and column to resize with window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.search_frame.grid(column=0, row=0, columnspan=2, sticky='nsew', ipady=10)
        self.filter_frame.grid(column=0, row=1, sticky='nsew', pady=10, padx=10)

        # Style for buttons
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14))
        style.configure('Background2.TFrame', background='#4f4f4f')  # Dark grey for main frame

        # Create a label for search
        self.search_label = ttk.Label(self.search_frame, text="Search:", font=("Helvetica", 16))
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_laptops,
                                        style="TButton", padding=5)
        self.treeview = ttk.Treeview(self.frame, columns=self.laptops_data.columns, show="headings")
        self.home_button = ttk.Button(self.frame, text="Home", command=self.go_to_home_page,
                                      style="TButton", padding=5)

        self.search_label.grid(column=0, row=0, padx=5, pady=10)
        self.search_entry.grid(column=1, row=0, padx=5, pady=5)
        self.search_button.grid(column=2, row=0, padx=5, pady=5)

        self.create_filters()
        self.treeview.grid(column=0, row=2, padx=5, pady=5, sticky='nsew', columnspan=3)
        self.home_button.grid(column=0, row=3, padx=20, pady=10)

        # Configure grid row and column to resize with window
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)

    def create_filters(self):
        # Create filter labels and dropdown menus
        filter_labels = ["brand", "processor_brand", "processor_tier", "gpu_brand", "is_touch_screen", "display_size"]
        self.filter_vars = {label: tk.StringVar() for label in filter_labels}
        for i, label in enumerate(filter_labels):
            filter_label = ttk.Label(self.filter_frame, text=label + ":", font=("Helvetica", 10))
            filter_label.grid(column=0, row=i, sticky=tk.W)
            filter_menu = ttk.Combobox(self.filter_frame, textvariable=self.filter_vars[label])
            filter_menu.grid(column=1, row=i, padx=5, pady=5, sticky='ew')  # Add sticky='ew' for horizontal resize
            # Populate dropdown menus with unique values from the corresponding column in the laptops data
            values = self.laptops_data[label.lower()].unique().tolist()
            values.insert(0, "")  # Add blank option at the beginning
            filter_menu['values'] = values

        # Configure grid row and column to resize with window
        # self.filter_frame.grid_rowconfigure(0, weight=1)
        self.filter_frame.grid_columnconfigure(1, weight=1)

    def clean_model_name(self, model_name):
        return model_name.split('(')[0].strip()  # Remove content within parentheses and leading/trailing spaces

    def search_laptops(self):
        """Search laptops"""

        # Clear the previous search results
        self.treeview.delete(*self.treeview.get_children())

        # Get the search query
        search_query = self.search_entry.get().lower()

        # Filter the laptops data based on the search query
        filtered_laptops = self.laptops_data[
            self.laptops_data['Model'].str.lower().str.contains(search_query, na=False)]

        # Clean the Model column
        filtered_laptops['Model'] = filtered_laptops['Model'].apply(self.clean_model_name)

        # Display the heading of laptops data in the treeview
        self.treeview['columns'] = list(filtered_laptops.columns)
        for col in filtered_laptops.columns:
            self.treeview.heading(col, text=col)

        # Apply additional filters
        for label, var in self.filter_vars.items():
            if var.get():
                filtered_laptops = filtered_laptops[filtered_laptops[label.lower()] == var.get()]

        # Display the filtered laptops in the treeview
        for _, row in filtered_laptops.iterrows():
            self.treeview.insert('', 'end', values=row.tolist())

        # Adjust column widths
        for column in self.treeview['columns']:
            if column == "Model":
                self.treeview.column(column, width=len(column) * 65, anchor=tk.CENTER)
            else:
                self.treeview.column(column, width=len(column) * 10, anchor=tk.CENTER)

    def go_to_home_page(self):
        from home import HomePage
        # Destroy the current frame and create a new home page
        self.frame.destroy()
        home_page = HomePage(self.root)
