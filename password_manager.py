from tkinter import *
from tkinter import messagebox
import random
import pyperclip 
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_letters):
    #password_list.append(random.choice(letters))
    password_number = [random.choice(numbers) for number in range(nr_numbers)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_char = [random.choice(symbols) for symbol in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letter + password_number + password_char
    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def find_password():
    #check to see if website exist in loaded file
    website = web_entry.get()
    #open the file
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        #if website in data, then load email
        if website in data:
            #find the email and password and store them in variables below
            email = data[website]["email"]
            password = data[website]["password"]
            #add a messagebox
            messagebox.showinfo(title="Website", message=f"email:{email}\npassword:{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
#this function saves entries into a text file
def save():
    #use the get() to to call the entries
    website = web_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()
    #create new dictionary for json
    new_data = {
        website:{ "email": email,
                "password": password
                    }
    }

    #if any entries are empty, display an error message else, confirm if user is happy to continue
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You can't leave an empty field")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"You've entered: email: {email}\n and password: {password}\n Is it ok to save")
        # #if its ok, then save to a file
        # if is_ok:
        #     with open("data.txt", "a") as data_file:
        #         data_file.write(f"\nwebsite: {website} | email: {email} | password: {password}\n")
                #use delete() to delete all entries after the user click 'add' and define from beginning to END (0, END)
        try:
            with open("data.json", "r") as data_file:
                #load data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #update data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #write the data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="/Users/yussifahmed/Desktop/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", font=("Arial", 12, "bold"), bg="white")
web_label.grid(column=0, row=1)

user_name_label = Label(text="Email/Username:", font=("Arial", 12, "bold"), bg="white")
user_name_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 12, "bold"), bg="white")
password_label.grid(column=0, row=3)

web_entry = Entry(width=22)
web_entry.grid(column=1, row=1)
web_entry.focus()

user_name_entry = Entry(width=39)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "yussifahmedgh@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

search_button = Button(text="search", width=13, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="generate password", command=create_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="add", width=37, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()


