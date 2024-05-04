"""main.py"""

import tkinter as tk
from home import HomePage

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
