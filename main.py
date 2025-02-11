from tkinter import *
from ui import setup_ui

# Initialize the Tkinter window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Set up the UI
setup_ui(window)

# Start the Tkinter event loop
window.mainloop()


