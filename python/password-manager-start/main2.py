from tkinter import * 
from tkinter import messagebox
import random
import json
# import pyperclip
WHITE = "#FFFFFF"




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():



    entryp.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_symbols +password_letters+ password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    entryp.insert(0,string=f"{password}")

    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entryw.get()
    email = entrye.get()
    password = entryp.get()
    new_data = {
        website:{
            "email" : email,
            "password":password,

        }
    }
    #messagebox.showinfo(title ="Title",message="Message")
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.askretrycancel(title="Oops",message="Please dont leave any fileds empty!")
        is_ok = False
    else:        
        is_ok = messagebox.askokcancel(title=website,message=f"These are the detailes entered: \nEmail:{email}"
                                    f"\n password : {password}\n Is it ok to save?")
        if is_ok:
            try:
                with open("password-manager-start/data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            
            except FileNotFoundError:
                with open("password-manager-start/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            
            else:
                with open("password-manager-start/data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
     
                entrye.delete(0, END)
                entryp.delete(0, END)
            
    #messagebox.showinfo(title ="Title",message="Message")

#<----------------------------- Password Extract ---------------------------------- #
def find_password():
    website = entryw.get()
    try:
        with open("password-manager-start/data.json",mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword: {password}")     
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")
        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager ")
window.config(padx=50,pady=50,bg=WHITE)



canvas = Canvas(width=200,height=200,bg=WHITE,highlightthickness=0)
lock = PhotoImage(file ="password-manager-start/logo.png")
canvas.create_image(100,100,image = lock)
canvas.grid(row = 0,column=1)

labelw = Label(text="Website:",font=("bold"),bg=WHITE,highlightthickness=0)
labelw.grid(row = 1,column =0 )


labele = Label(text="Email/Username:",font=("bold"),bg=WHITE,highlightthickness=0)
labele.grid(row=2,column = 0)

labelp = Label(text="Password:",font=("bold"),bg=WHITE,highlightthickness=0)
labelp.grid(row=3,column = 0)


entryw = Entry(width=21)
entryw.grid(row=1,column=1)
entryw.focus()

entrye = Entry(width=35)
entrye.grid(row=2,column=1,columnspan=2)
entrye.insert(0,"xyz@gmail.com")

entryp = Entry(width=21)
entryp.grid(row = 3,column=1)

buttonp = Button(text="Generate Password",command=generate)
buttonp.grid(row = 3,column=2)

buttona = Button(text="Add",font=("bold"),command=save)
buttona.config(width=36)
buttona.grid(row=4,column=1,columnspan=2)

buttons = Button(text="Search",font=("bold"),command=find_password)
buttons.config(width=14)
buttons.grid(row = 1,column=2)

window.mainloop()
