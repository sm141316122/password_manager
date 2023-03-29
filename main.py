from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbol

    shuffle(password_list)

    gen_password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, gen_password)


def add():
    website = web_input.get().title()
    user_name = user_name_input.get()
    password = password_input.get()

    if website and user_name and password != "":
        with open("data.txt", "a") as file:
            file.write(f"{website} | {user_name} | {password}\n")
        messagebox.showinfo("Successful !", "已加入清單")
    else:
        messagebox.showwarning("Failed", "未輸入完成, 請重新輸入")

    web_input.delete(0, END)
    user_name_input.delete(0, END)
    user_name_input.insert(0, "123456@gmail.com")
    password_input.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=190)
canvas.create_image(100, 95, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.config(pady=10)
web_label.grid(row=1, column=0)
user_name_label = Label(text="Email/Username:")
user_name_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.config(pady=10)
password_label.grid(row=3, column=0)

web_input = Entry(width=45)
web_input.grid(row=1, column=1, columnspan=2)
user_name_input = Entry(width=45)
user_name_input.insert(0, "123456@gmail.com")
user_name_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=28)
password_input.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password", command=generate_password, bg="white", highlightthickness=0)
gen_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=add, bg="white", highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
