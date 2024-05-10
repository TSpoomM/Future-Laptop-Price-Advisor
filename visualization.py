import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns


class VisualizationPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Laptop Visualization Tool")
        self.laptops_data = pd.read_csv("laptops.csv")
        self.init_component()

    def init_component(self):
        # Create GUI components and display visualizations
        self.frame = ttk.Frame(self.root, padding="20", style="Background.TFrame")
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Set background color for each frame style
        style = ttk.Style()
        style.configure('Background.TFrame', background='#4f4f4f')  # Dark grey for main frame

        # Add buttons for each visualization
        self.button_descriptive_stats = ttk.Button(self.frame, text="Show Descriptive Statistics",
                                                   command=self.show_descriptive_statistics)
        self.button_descriptive_stats.grid(row=0, column=0, padx=10, pady=5)

        self.button_correlation = ttk.Button(self.frame, text="Show Correlation Analysis",
                                             command=self.show_correlation_analysis)
        self.button_correlation.grid(row=0, column=1, padx=10, pady=5)

        self.button_all_graphs = ttk.Button(self.frame, text="Show Graphs",
                                            command=self.show_all_graphs)
        self.button_all_graphs.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Scrolltext for displaying descriptive statistics and correlation analysis
        self.scrolltext_descriptive = tk.Text(self.frame, wrap=tk.WORD, width=50, height=6)
        self.scrolltext_descriptive.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.scrolltext_correlation = tk.Text(self.frame, wrap=tk.WORD, width=50, height=6)
        self.scrolltext_correlation.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        # Add button to go back to home page
        self.button_back = ttk.Button(self.frame, text="Back to Home", command=self.go_to_home_page)
        self.button_back.grid(row=2, column=2, padx=10, pady=5)

        # Configure row and column weights to make them stretch evenly when resized
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def show_descriptive_statistics(self):
        # Calculate descriptive statistics for Price and Rating columns
        price_stats = self.laptops_data['Price'].describe()
        rating_stats = self.laptops_data['Rating'].describe()

        # Display statistics on the scrolltext
        stats_text = f"Price Statistics:\n{price_stats}\n\nRating Statistics:\n{rating_stats}"
        self.scrolltext_descriptive.delete(1.0, tk.END)
        self.scrolltext_descriptive.insert(tk.END, stats_text)

    def show_correlation_analysis(self):
        # Define a mapping dictionary for label encoding of 'processor_tier'
        processor_tier_mapping = {
            'core i3': 1, 'core i5': 2, 'core i7': 3, 'core i9': 4, 'ryzen 3': 5, 'ryzen 5': 6, 'ryzen 7': 7,
            'ryzen 9': 8,
            'm1': 9, 'm2': 10, 'm3': 11, 'celeron': 12, 'pentium': 13, 'core ultra 7': 14, 'other': 15
        }

        # Apply label encoding to the 'processor_tier' column
        self.laptops_data['processor_tier_encoded'] = self.laptops_data['processor_tier'].map(processor_tier_mapping)

        # Calculate correlation coefficients
        correlations = self.laptops_data[['processor_tier_encoded', 'ram_memory', 'Price']].corr()

        # Display correlation matrix on the scrolltext
        self.scrolltext_correlation.delete(1.0, tk.END)
        self.scrolltext_correlation.insert(tk.END, "Correlation matrix:\n")
        self.scrolltext_correlation.insert(tk.END, correlations)

    def show_all_graphs(self):
        # Clear any previous graphs
        for widget in self.frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        # Create histogram of laptop prices
        plt.figure(figsize=(4, 4))  # Adjust figure size here
        sns.histplot(self.laptops_data['Price'], bins=20, kde=True)
        plt.title("Distribution of Laptop Prices", fontsize=10)
        plt.xlabel("Price ($)", fontsize=8)
        plt.ylabel("Frequency", fontsize=8)
        canvas1 = FigureCanvasTkAgg(plt.gcf(), master=self.frame)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=0, column=2, padx=10, pady=5)

        # Create bar chart of laptop brands
        plt.figure(figsize=(4, 4))  # Adjust figure size here
        sns.countplot(data=self.laptops_data, y='brand')
        plt.title("Distribution of Laptop Brands", fontsize=10)
        plt.xlabel("Count", fontsize=8)
        plt.ylabel("Brand", fontsize=8)
        canvas2 = FigureCanvasTkAgg(plt.gcf(), master=self.frame)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=0, column=3, padx=10, pady=5)

        # Create pie chart of primary storage type
        plt.figure(figsize=(4, 4))  # Adjust figure size here
        storage_counts = self.laptops_data['primary_storage_type'].value_counts()
        plt.pie(storage_counts, labels=storage_counts.index, autopct='%1.1f%%')
        plt.title("Distribution of Primary Storage Type", fontsize=10)
        canvas3 = FigureCanvasTkAgg(plt.gcf(), master=self.frame)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=1, column=2, padx=10, pady=5)

        # Create line graph of display size over the years
        plt.figure(figsize=(4, 4))  # Adjust figure size here
        sns.lineplot(data=self.laptops_data, x='Rating', y='display_size')
        plt.title("Trend of Display Size", fontsize=10)
        plt.xlabel("Rating", fontsize=8)
        plt.ylabel("Display Size (inches)", fontsize=8)
        canvas4 = FigureCanvasTkAgg(plt.gcf(), master=self.frame)
        canvas4.draw()
        canvas4.get_tk_widget().grid(row=1, column=3, padx=10, pady=5)

    def go_to_home_page(self):
        from home import HomePage
        self.root.destroy()  # Destroy the current window
        home_page = HomePage(self.root)
