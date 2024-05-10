"""My home page."""

import tkinter as tk
from tkinter import ttk
import pandas as pd


class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Future Laptop Price Advisor")
        self.init_component()  # Initialize components

    def init_component(self):
        # Create a frame to contain the widgets
        self.frame = ttk.Frame(self.root, padding="20", style="Background.TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.name_frame = ttk.Frame(self.frame, style="NameFrame.TFrame")
        self.name_frame.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

        self.data_frame = ttk.Frame(self.frame, style="DataFrame.TFrame", padding=20)
        self.data_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky="nsew")

        self.button_frame = ttk.Frame(self.frame, style="ButtonFrame.TFrame", padding=20)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=20, sticky="nsew")

        # Configure row and column weights for resizing
        self.frame.grid_columnconfigure(0, weight=1)
        self.name_frame.grid_columnconfigure(0, weight=1)

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)
        self.button_frame.grid_columnconfigure(4, weight=1)

        self.data_frame.grid_rowconfigure(0, weight=1)
        self.data_frame.grid_columnconfigure(0, weight=1)
        self.data_frame.grid_columnconfigure(1, weight=1)

        # Style for buttons
        button_style = ttk.Style()
        button_style.configure("TButton", font=("Helvetica", 14))

        # Add a label for the title
        title_label = ttk.Label(self.name_frame, text="Welcome to Future Laptop Price Advisor",
                                font=("Helvetica", 28, "bold"), anchor=tk.CENTER)
        # title_label.grid(row=0, column=0, columnspan=1, padx=25, pady=25, sticky="nsew", ipadx=50, ipady=30)
        title_label.pack(padx=25, pady=25, ipadx=300, ipady=30, side=tk.TOP)

        search_filter_button = ttk.Button(self.button_frame, text="Search and Filter", command=self.go_to_filter_page,
                                          style="TButton", padding=5)

        comparison_button = ttk.Button(self.button_frame, text="Comparison Tool", command=self.go_to_comparison_page,
                                       style="TButton", padding=5)

        rating_button = ttk.Button(self.button_frame, text="User Ratings", command=self.go_to_rating_page,
                                   style="TButton", padding=5)

        visualization_button = ttk.Button(self.button_frame, text="Statistics", command=self.go_to_visualization_page,
                                          style="TButton", padding=5)

        exit_button = ttk.Button(self.button_frame, text="Exit", command=self.exit,
                                 style="TButton", padding=5)

        # Create a Treeview widget for displaying data
        self.tree = ttk.Treeview(self.data_frame)

        # Create scrollbars for the Treeview widget
        self.scrollbar_y = ttk.Scrollbar(self.data_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar_x = ttk.Scrollbar(self.data_frame, orient="horizontal", command=self.tree.xview)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.scrollbar_x.grid(row=1, column=0, sticky="ew")

        # Configure the Treeview widget to use scrollbars
        self.tree.config(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Load data from CSV file into the Treeview widget
        self.load_data_from_csv()

        search_filter_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        comparison_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        rating_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        visualization_button.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        exit_button.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

        # Set background color for each frame style
        style = ttk.Style()
        style.configure('Background.TFrame', background='#4f4f4f')  # Dark grey for main frame
        style.configure('NameFrame.TFrame', background='#CC33FF')  # Purple for name frame
        style.configure('ButtonFrame.TFrame', background='#CC33FF')  # Purple for button frame
        style.configure('DataFrame.TFrame', background='#ffffff')  # White for data frame

    def clean_model_name(self, model_name):
        return model_name.split('(')[0].strip()  # Remove content within parentheses and leading/trailing spaces

    def load_data_from_csv(self):
        try:
            # Read data from CSV file
            df = pd.read_csv('laptops.csv')

            # Clean the Model column
            df['Model'] = df['Model'].apply(self.clean_model_name)

            # Drop columns that are not required
            columns_to_drop = ['brand', 'num_cores', 'num_threads', 'secondary_storage_type',
                               'secondary_storage_capacity', 'gpu_type', 'resolution_width',
                               'resolution_height', 'year_of_warranty', 'is_touch_screen']
            df = df.drop(columns=columns_to_drop)

            # Display data in the Treeview widget
            self.display_data(df)
        except FileNotFoundError:
            print("File not found.")

    def display_data(self, df):
        # Set columns for the Treeview
        self.tree["columns"] = list(df.columns)

        # Suppress the first identifier column
        self.tree["show"] = "headings"

        # Create headings for each column
        for column in df.columns:
            self.tree.heading(column, text=column, anchor=tk.CENTER)  # Set anchor to center for all columns

        # Insert data into the Treeview
        for index, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

        # Set the width of each column
        for column in df.columns:
            if column == "Model":
                self.tree.column(column, width=len(column) * 65, anchor=tk.CENTER)
            else:
                self.tree.column(column, width=len(column) * 10, anchor=tk.CENTER)

    def go_to_filter_page(self):
        from searchandfilterpage import SearchAndFilterPage
        # Destroy the current frame and create a new SearchAndFilter page
        self.frame.destroy()
        SearchAndFilterPage(self.root)
        # pass

    def go_to_comparison_page(self):
        from comparison import ComparisonPage
        # Destroy the current frame and create a new Comparison page
        self.frame.destroy()
        ComparisonPage(self.root)
        # pass

    def go_to_rating_page(self):
        from rating import UserRatingsPage
        # Destroy the current frame and create a new UserRatingsPage page
        self.frame.destroy()
        UserRatingsPage(self.root)
        # pass

    def go_to_visualization_page(self):
        from visualization import VisualizationPage
        # Destroy the current frame and create a new VisualizationPage page
        self.frame.destroy()
        VisualizationPage(self.root)
        # pass

    def exit(self):
        self.root.destroy()
