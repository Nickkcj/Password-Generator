from tkinter import messagebox
import json

def save_password(data, website):
    if data[website] == "" or data[website]["password"] == "":
        messagebox.showwarning(title="Error", message="Please make sure you haven't left any fields empty!")
        return False

    try:
        with open("data.json", "r") as file:
            content = file.read()
            new_data = json.loads(content) if content.strip() else {}
    except (FileNotFoundError, json.JSONDecodeError):
        new_data = {}  

    new_data.update(data)

    with open("data.json", "w") as file:
        json.dump(new_data, file, indent=4)

    messagebox.showinfo(title="Success", message="Added into the database!")
    return True
    

