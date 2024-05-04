"""My visualization page."""

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class VisualizationPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Laptop Visualization Tool")
        self.laptops_data = pd.read_csv("laptops.csv")
        self.init_component()

    def init_component(self):
        # Create GUI components and display visualizations
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Add buttons for each visualization
        self.button_descriptive_stats = ttk.Button(self.frame, text="Descriptive Statistics",
                                                   command=self.calculate_descriptive_statistics)
        self.button_descriptive_stats.grid(row=0, column=0, padx=10, pady=5)

        self.button_correlation = ttk.Button(self.frame, text="Correlation Analysis",
                                             command=self.calculate_correlation)
        self.button_correlation.grid(row=1, column=0, padx=10, pady=5)

        self.button_distribution = ttk.Button(self.frame, text="Distribution Graph",
                                              command=self.create_distribution_graph)
        self.button_distribution.grid(row=2, column=0, padx=10, pady=5)

        self.button_other_graphs = ttk.Button(self.frame, text="Other Graphs", command=self.create_other_graphs)
        self.button_other_graphs.grid(row=3, column=0, padx=10, pady=5)

        self.scrolltext = ScrolledText(self.frame, width=50, height=10, wrap=tk.WORD)
        self.scrolltext.grid(row=0, column=1, rowspan=2, padx=10, pady=5, sticky=(tk.W, tk.N, tk.E, tk.S))

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.scrolltext.yview)
        self.scrollbar.grid(row=0, column=2, rowspan=2, sticky=(tk.N, tk.S))
        self.scrolltext.config(yscrollcommand=self.scrollbar.set)

        # Add button to go back to home page
        self.button_back = ttk.Button(self.frame, text="Back to Home", command=self.go_to_home_page)
        self.button_back.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

    def calculate_descriptive_statistics(self):
        # Calculate descriptive statistics for Price and Rating columns
        price_stats = self.laptops_data['Price'].describe()
        rating_stats = self.laptops_data['Rating'].describe()

        # Display statistics on the GUI
        stats_text = f"Price Statistics:\n{price_stats}\n\nRating Statistics:\n{rating_stats}"
        self.display_text(stats_text)

    def calculate_correlation(self):
        # Define a mapping dictionary for label encoding of 'processor_tier'
        processor_tier_mapping = {
            'core i3': 1,
            'core i5': 2,
            'core i7': 3,
            'core i9': 4,
            'ryzen 3': 5,
            'ryzen 5': 6,
            'ryzen 7': 7,
            'ryzen 9': 8,
            'm1': 9,
            'm2': 10,
            'm3': 11,
            'celeron': 12,
            'pentium': 13,
            'core ultra 7': 14,
            'other': 15
        }

        # Apply label encoding to the 'processor_tier' column
        self.laptops_data['processor_tier_encoded'] = self.laptops_data['processor_tier'].map(processor_tier_mapping)

        # Calculate correlation coefficients
        correlations = self.laptops_data[['processor_tier_encoded', 'ram_memory', 'Price']].corr()

        # Update text widget with correlation matrix
        self.scrolltext.delete('1.0', tk.END)  # Clear previous text
        self.scrolltext.insert(tk.END, "Correlation matrix:\n")
        self.scrolltext.insert(tk.END, correlations)

    def display_text(self, text):
        self.scrolltext.delete('1.0', tk.END)  # Clear previous text
        self.scrolltext.insert(tk.END, text)

    def create_distribution_graph(self):
        # Create histogram of laptop prices
        plt.figure(figsize=(8, 6))
        sns.histplot(self.laptops_data['Price'], bins=20, kde=True)
        plt.title("Distribution of Laptop Prices")
        plt.xlabel("Price ($)")
        plt.ylabel("Frequency")
        plt.show()

    def create_other_graphs(self):
        # Create bar chart of laptop brands
        plt.figure(figsize=(8, 6))
        sns.countplot(data=self.laptops_data, y='brand')
        plt.title("Distribution of Laptop Brands")
        plt.xlabel("Count")
        plt.ylabel("Brand")
        plt.show()

        # Create pie chart of primary storage type
        plt.figure(figsize=(8, 6))
        storage_counts = self.laptops_data['Primary Storage Type'].value_counts()
        plt.pie(storage_counts, labels=storage_counts.index, autopct='%1.1f%%')
        plt.title("Distribution of Primary Storage Type")
        plt.show()

        # Create line graph of display size over the years
        plt.figure(figsize=(8, 6))
        sns.lineplot(data=self.laptops_data, x='Year', y='display_size')
        plt.title("Trend of Average Display Size Over the Years")
        plt.xlabel("Year")
        plt.ylabel("Display Size (inches)")
        plt.show()

    def go_to_home_page(self):
        from home import HomePage
        self.frame.destroy()
        home_page = HomePage(self.root)
