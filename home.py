"""My home page."""

import tkinter as tk
from tkinter import ttk


class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Future Laptop Price Advisor")
        self.init_component()  # Initialize components

    def init_component(self):
        # Create a frame to contain the widgets
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Style for buttons
        button_style = ttk.Style()
        button_style.configure("TButton", font=("Helvetica", 14))

        # Add a label for the title
        title_label = ttk.Label(self.frame, text="Welcome to Future Laptop Price Advisor",
                                font=("Helvetica", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Add buttons with custom styling
        search_filter_button = ttk.Button(self.frame, text="Search and Filter", command=self.go_to_filter_page,
                                          style="TButton")
        search_filter_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        comparison_button = ttk.Button(self.frame, text="Comparison Tool", command=self.go_to_comparison_page,
                                       style="TButton")
        comparison_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        rating_button = ttk.Button(self.frame, text="User Ratings", command=self.go_to_rating_page, style="TButton")
        rating_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        visualization_button = ttk.Button(self.frame, text="Statistics", command=self.go_to_visualization_page,
                                          style="TButton")
        visualization_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        exit_button = ttk.Button(self.frame, text="Exit", command=self.exit, style="TButton")
        exit_button.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew")

    def go_to_filter_page(self):
        from searchandfilterpage import SearchAndFilterPage
        # Destroy the current frame and create a new SearchAndFilter page
        self.frame.destroy()
        filter_page = SearchAndFilterPage(self.root)

    def go_to_comparison_page(self):
        from comparison import ComparisonPage
        # Destroy the current frame and create a new Comparison page
        self.frame.destroy()
        comparison_page = ComparisonPage(self.root)

    def go_to_rating_page(self):
        from rating import UserRatingsPage
        # Destroy the current frame and create a new UserRatingsPage page
        self.frame.destroy()
        rating_page = UserRatingsPage(self.root)

    def go_to_visualization_page(self):
        from visualization import VisualizationPage
        # Destroy the current frame and create a new VisualizationPage page
        self.frame.destroy()
        visualization_page = VisualizationPage(self.root)

    def exit(self):
        self.root.destroy()
