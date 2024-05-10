import tkinter as tk
from tkinter import ttk
import pandas as pd
from home import HomePage


class UserRatingsPage:
    def __init__(self, root):
        self.root = root
        self.root.title("User Ratings")
        self.init_component()

    def init_component(self):
        # Read existing ratings data from laptops.csv
        self.ratings_data = pd.read_csv("laptops.csv").sort_values(by="Rating", ascending=False)

        # Display existing ratings in a table or list
        self.display_ratings()

        # Add buttons to sort ratings
        sort_high_to_low_button = ttk.Button(self.frame, text="Sort High to Low", command=self.sort_high_to_low)
        sort_high_to_low_button.pack(side="left", padx=10, pady=10)

        sort_low_to_high_button = ttk.Button(self.frame, text="Sort Low to High", command=self.sort_low_to_high)
        sort_low_to_high_button.pack(side="left", padx=10, pady=10)

        # Add a button to navigate back to the home page
        back_button = ttk.Button(self.frame, text="Back to Home", command=self.go_to_home_page)
        back_button.pack(side="right", padx=10, pady=10)

    def preprocess_model_name(self, model):
        # Function to remove data within parentheses in the model name
        return model.split(" (")[0]

    def display_ratings(self):
        # Create a frame to hold the treeview and scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # Create scrollbar
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Create treeview
        self.rating_table = ttk.Treeview(self.frame, columns=("Model", "Rating"), show="headings",
                                         yscrollcommand=scrollbar.set)
        self.rating_table.heading("Model", text="Model")
        self.rating_table.heading("Rating", text="Rating")
        self.rating_table.column("Model", width=500)
        self.rating_table.column("Rating", anchor="center")

        # Configure scrollbar to scroll the treeview
        scrollbar.config(command=self.rating_table.yview)

        for index, row in self.ratings_data.iterrows():
            model_name = self.preprocess_model_name(row["Model"])
            self.rating_table.insert("", "end", values=(model_name, row["Rating"]))

        self.rating_table.pack(fill="both", expand=True)

    def sort_high_to_low(self):
        # Sort ratings from high to low and redisplay
        self.ratings_data = self.ratings_data.sort_values(by="Rating", ascending=False)
        self.update_ratings()

    def sort_low_to_high(self):
        # Sort ratings from low to high and redisplay
        self.ratings_data = self.ratings_data.sort_values(by="Rating", ascending=True)
        self.update_ratings()

    def update_ratings(self):
        # Delete old data from treeview
        self.rating_table.delete(*self.rating_table.get_children())

        # Insert updated data into treeview
        for index, row in self.ratings_data.iterrows():
            model_name = self.preprocess_model_name(row["Model"])
            self.rating_table.insert("", "end", values=(model_name, row["Rating"]))

    def go_to_home_page(self):
        # Navigate back to the home page
        self.frame.destroy()
        home_page = HomePage(self.root)  # Create a new instance of the HomePage class
