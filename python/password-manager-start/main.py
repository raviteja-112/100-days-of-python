from tkinter import * 
from tkinter import messagebox
import random
import json
# import pyperclip
WHITE = "#FFFFFF"
# nr_numbers = 1
# nr_letters = 1
# nr_symbols = 1

# def letter(value):
#     global nr_letters
#     nr_letters = int(value)
# def symbol(value):
#     global nr_symbols
#     nr_symbols = int(value)
# def number(value):
#     global nr_numbers
#     nr_numbers = int(value)  



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

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_symbols +password_letters+ password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    entryp.insert(0,string=f"{password}")

    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entryw.get()
    email = entrye.get()
    password = entryp.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.askretrycancel(title="Oops",message="Please dont leave any fileds empty!")
        is_ok = False
    else:        
        is_ok = messagebox.askokcancel(title=website,message=f"These are the detailes entered: \nEmail:{email}"
                                    f"\n password : {password}\n Is it ok to save?")
    
    if is_ok == True:
        with open("password-manager-start/data.txt",mode="a") as f:
            f.write(f"{website} | {email} | {password} \n")
            entryw.delete(0,END)
            entrye.delete(0,END)
            entryp.delete(0,END)
            f.close()
        
    #messagebox.showinfo(title ="Title",message="Message")
   
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


entryw = Entry(width=35)
entryw.grid(row=1,column=1,columnspan=2)
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

#extra functionality

# scalel = Scale(from_= 1 , to= 10,orient=HORIZONTAL,command=letter)
# scalel.grid(column = 1,row = 5,sticky="ew")

# scalen = Scale(from_= 1 , to= 10,orient=HORIZONTAL,command=number)
# scalen.grid(column = 1,row = 6,sticky="ew")

# scales = Scale(from_= 1 , to= 10,orient=HORIZONTAL,command=symbol)
# scales.grid(column = 1,row = 7,sticky="ew")

window.mainloop()
