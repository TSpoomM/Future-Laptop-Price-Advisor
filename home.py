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

        # Add a button to navigate to the Search and Filter page
        search_filter_button = ttk.Button(self.frame, text="Search And Filter", command=self.go_to_filter_page)
        search_filter_button.grid(row=1, column=0, padx=10, pady=10)

        # Add a button to navigate to the Comparison page
        comparison_button = ttk.Button(self.frame, text="Comparison Tool", command=self.go_to_comparison_page)
        comparison_button.grid(row=2, column=0, padx=10, pady=10)

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
