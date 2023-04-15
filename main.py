from tkinter import *
from random import *
from tkinter import messagebox
import pyperclip

SEPARATOR = " | "
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """
    Generates a random password with between 8 and 10 letters, 2 and 4 symbols
    and 2 and 4 numbers
    """
    # Vars
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # Generate paswword
    pass_list = []
    passw_entry.delete(0, END)
    pass_list = [choice(letters) for _ in range(randint(8, 10))]
    pass_list += [choice(numbers) for _ in range(randint(2, 4))]
    pass_list += [choice(symbols) for _ in range(randint(2, 4))]
    # Shuffle it
    shuffle(pass_list)
    # Concatenate into a string
    password = ""
    for n in pass_list:
        password += n
    # Show in Entry
    passw_entry.insert(0, password)
    pyperclip.copy(passw_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """
    Save the data in a file
    """
    # Vars
    web = web_entry.get()
    user = user_entry.get()
    passw = passw_entry.get()

    # Some validation
    if len(web) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Empty fields",
                            message="Don't leave any fields empty please.")
    else:
        # Double check
        if messagebox.askokcancel(title=web, message=f"Data entered: \nEmail: {user}\nPassword: {passw}"
                                  f"\nSave data?"):
            # Save to file
            with open("data.txt", "a") as data_file:
                data_file.write(web + SEPARATOR + user +
                                SEPARATOR + passw + "\n")
            web_entry.delete(0, END)
            passw_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
name_label = Label(text="Email/Username:")
name_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Inputs
web_entry = Entry(width=43)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")
web_entry.focus()
user_entry = Entry(width=43)
user_entry.grid(column=1, row=2, columnspan=2, sticky="w")
user_entry.insert(0, "yusepah@gmail.com")
passw_entry = Entry(width=23)
passw_entry.grid(column=1, row=3, sticky="w")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=1, row=3, columnspan=2, sticky="e")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
