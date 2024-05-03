import tkinter as tk
from tkinter import ttk
from searchandfilter import SearchAndFilter
from tkinter.scrolledtext import ScrolledText
import pandas as pd


class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Future Laptop Price Advisor")
        # # Add your home page widgets here
        # home_label = ttk.Label(self.root, text="Welcome to Future Laptop Price Advisor !!!")
        # home_label.pack(pady=20)
        self.init_component()  # Initialize components

    def init_component(self):
        # Create a frame to contain the widgets
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Add a button or link to the home page
        self.home_button = ttk.Button(self.frame, text="Search And Filter", command=self.go_to_filter_page)
        self.home_button.grid(column=0, row=1, padx=10, pady=10)

        self.home_button = ttk.Button(self.frame, text="Search And Filter", command=self.go_to_filter_page)
        self.home_button.grid(column=0, row=1, padx=10, pady=10)

    def go_to_filter_page(self):
        # Destroy the current frame and create a new home page
        self.frame.destroy()
        filter_page = SearchAndFilter(self.root)  # Create FilterPage using grid layout

    def run(self):
        self.root.mainloop()
