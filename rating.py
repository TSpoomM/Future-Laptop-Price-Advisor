import tkinter as tk
from tkinter import ttk
import pandas as pd
from home import HomePage  # Importing the HomePage class


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

        # Add a button to navigate back to the home page
        back_button = ttk.Button(self.root, text="Back to Home", command=self.go_to_home_page)
        back_button.pack(pady=10)

    def preprocess_model_name(self, model):
        # Function to remove data within parentheses in the model name
        return model.split(" (")[0]

    def display_ratings(self):
        # Display existing ratings in a table or list
        rating_table = ttk.Treeview(self.root, columns=("Model", "Rating"), show="headings")
        rating_table.heading("Model", text="Model")
        rating_table.heading("Rating", text="Rating")
        rating_table.column("Model", width=500)
        rating_table.column("Rating", anchor="center")

        for index, row in self.ratings_data.iterrows():
            model_name = self.preprocess_model_name(row["Model"])
            rating_table.insert("", "end", values=(model_name, row["Rating"]))
        rating_table.pack(fill="both", expand=True)

    def go_to_home_page(self):
        # Navigate back to the home page
        self.root.destroy()
        home_page = HomePage(tk.Tk())  # Create a new instance of the HomePage class
