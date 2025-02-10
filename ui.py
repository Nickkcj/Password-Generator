from tkinter import *
from password_generator import generate_password
from file_manager import save_password
import pyperclip
import os

def setup_ui(window):
    # Construct the path to logo.png
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    logo_path = os.path.join(base_dir, "logo.png")  # Construct the full path to logo.png

    # Store the PhotoImage object in a persistent variable
    global logo_image  # Make it global to prevent garbage collection
    logo_image = PhotoImage(file=logo_path)  # Load the image

    # Putting the image
    canvas = Canvas(width=200, height=200)
    canvas.create_image(100, 100, image=logo_image)  # Use the image
    canvas.grid(column=1, row=0)

    # Creating the labels
    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)

    email_user_label = Label(text="Email/Username:")
    email_user_label.grid(column=0, row=2)

    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    # Creating the entries
    website_entry = Entry(width=35)
    website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
    website_entry.focus()

    email_entry = Entry(width=35)
    email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
    email_entry.insert(0, "teste@email.com")

    password_entry = Entry(width=21)
    password_entry.grid(column=1, row=3, sticky="EW")

    # Function to handle password generation
    def generate_and_insert_password():
        password = generate_password()
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)

    # Function to handle saving data
    def save_data():
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if save_password(website, email, password):
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    # Creating the buttons
    generate_password_button = Button(text="Generate Password", command=generate_and_insert_password)
    generate_password_button.grid(column=2, row=3, sticky="EW")

    add_button = Button(text="Add", width=35, command=save_data)
    add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

    # Configure column weights
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)