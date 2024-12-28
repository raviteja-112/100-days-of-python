from tkinter import *

window = Tk()
window.title("Mile to KM convertor")
window.minsize(width=500,height=500)
window.config(padx=100,pady=100)

entry = Entry(width=10)
entry.grid(column=2,row=1)


label1 = Label(text = "Miles",font=("Arial",20,"bold"))
label1.grid(column= 3,row = 1)
label1.config(padx=20,pady=20)



label2 = Label(text = " is equal to ",font=("Arial",20,"bold"))
label2.grid(column= 1,row = 2)
label2.config(padx=20,pady=20)

text = Text(height= 1,width=10)
text.insert(END,"")
text.grid(column=2,row=2)
text.config(padx=20,pady=5)

label3 = Label(text = "KM",font=("Arial",20,"bold"))
label3.grid(column= 3,row = 2)
label3.config(padx=20,pady=20)

def calculate():
    text.delete("1.0",END)
    miles = int(entry.get())
    km = miles * 1.60934
    text.insert(END,f"{km}")

button = Button(text="Calculate",command= calculate)
button.grid(column=2,row= 3)
button.config(padx=20,pady=5)





window.mainloop()