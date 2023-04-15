from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
web = Entry(width=43)
web.grid(column=1, row=1, columnspan=2, sticky="w")
user = Entry(width=43)
user.grid(column=1, row=2, columnspan=2, sticky="w")
passw = Entry(width=21)
passw.grid(column=1, row=3, sticky="w")

# Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=1, row=3, columnspan=2, sticky="e")
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
