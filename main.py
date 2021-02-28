from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input_password.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(choice(letters)) for char in range(randint(4, 6))]
    [password_list.append(choice(symbols))for char in range(randint(1, 2))]
    [password_list.append(choice(numbers)) for char in range(randint(1, 2))]

    shuffle(password_list)
    password = ''.join(password_list)

    print(f"Your password is: {password}")
    input_password.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    # print(input_website.get())
    website = input_website.get()
    password = input_password.get()
    email = input_emailUsername.get()

    if len(website) < 1:
        messagebox.showerror(message=f"Miss a paramether in website")
    elif len(password) < 1:
        messagebox.showerror(message=f"Miss a paramether in password")
    elif len(email) < 1:
        messagebox.showerror(message=f"Miss a paramether in email")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail:"
                                                              f"{email}\nPassword {password}\n Is it ok to save?")
        if is_ok:
            with open('database.txt', 'a') as database:
                database.write(f"{website} | {email} | {password} \n")
            input_website.delete(0, 'end')
            input_password.delete(0, 'end')
            input_website.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx="50", pady="50")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website")
label_website.grid(row=1, column=0)

input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2, sticky="EW")
input_website.focus()

label_emailUsername = Label(text="Email/Username")
label_emailUsername.grid(row=2, column=0)

input_emailUsername = Entry(width=35)
input_emailUsername.grid(row=2, column=1, columnspan=2, sticky="EW")
input_emailUsername.insert(0, "joaberochadel@gmail.com")

label_password = Label(text="Password")
label_password.grid(row=3, column=0)

input_password = Entry(width=21)
input_password.grid(row=3, column=1, sticky="EW")

button_GeneratePassword = Button(text="Generate Password", command=generate_password)
button_GeneratePassword.grid(row=3, column=2, sticky="EW")

button_add = Button(text="Add", width=35, command=add)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
