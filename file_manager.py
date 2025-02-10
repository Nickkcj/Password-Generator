from tkinter import messagebox

def save_password(website, email, password):
    if website == "" or password == "":
        messagebox.showwarning(title="Error", message="Please make sure you haven't left any fields empty!")
        return False

    decision = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                             f"\nPassword: {password} \nIs it ok to save?")
    if decision:
        with open("saved_passwords.txt", "a") as file:
            file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
        return True
    return False