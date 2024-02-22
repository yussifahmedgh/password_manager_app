import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
#__________________________________ generate password _______________________________________
def password_generator():
    
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #this will allow us to generate random range of 8, 20 for letters and 2, 4 for number and symbols
    # password_letter = random.randint(8, 10)
    # password_number = random.randint(2, 4)
    # password_symbol = random.randint(2, 4)

    ran_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    ran_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    ran_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = ran_letter + ran_symbol + ran_number
    random.shuffle(password_list)

    # password = " "
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



#__________________________________ save password _____________________________________________
def save():
    
    website = web_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Sorry, you can't leave a blank field")
        
    else:
         
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)       
        else:
             # Update the existing data with the new data
            data.update(new_data)  

             # Write the updated data back to the file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)



#__________________________________ Search PASSWORD  ___________________________________________
def search():
    website = web_entry.get()

    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= "Error", message="No Data fiel found")
    else:
        if website in data:
            #create an email and find the email in data
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\npassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"The {website} website info does not exist")
    
   

#__________________________________ UI SETUP  _______________________________________



window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file=("/Users/yussifahmed/Desktop/password manager/new password/logo.png"))
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=2, column=0)

email_label = Label(text="Username/Email:")
email_label.grid(row=3, column=0)

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)


#entries
web_entry = Entry(width=27)
web_entry.grid(row=2, column=1)
web_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(row=3, column=1, columnspan=3)
email_entry.insert(0, "yussifahmedgh@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(row=4, column=1)


#buttons
search_button = Button(text="Search", width=13, command= search)
search_button.grid(row=2, column=3, columnspan=2)
                   
generate_password_button = Button(text="Generate password", command=password_generator)
generate_password_button.grid(row=4, column=3)

add_password_button = Button(text="Add password", width=42, command=save)
add_password_button.grid(row=5, column=1, columnspan=3)

window.mainloop()


