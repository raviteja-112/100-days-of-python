from tkinter import *
import pandas 
import random
BACKGROUND_COLOR = "#B1DDC6"
df = {}


#<------------------reading from file----------------->
try:
    data = pandas.read_csv("flash-card-project-start/data/to learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project-start/data/french_words.csv")
    df = original_data.to_dict(orient="records")

else:
    df = data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image,image = white)
    current_card  = random.choice(df)
    canvas.itemconfig(card_title,text="French",fill = "black")
    canvas.itemconfig(card_word,text = current_card["French"],fill = "black")
    flip_timer = window.after(3000,func=back_card)
    
def know():
    df.remove(current_card)
    data1 = pandas.DataFrame(df)
    data1.to_csv("flash-card-project-start/data/to learn.csv",index=False)
    next_card() 




def back_card():
    canvas.itemconfig(canvas_image,image=green)
    canvas.itemconfig(card_title,text="English",fill = "white")
    canvas.itemconfig(card_word,text = current_card["English"],fill = "white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=back_card)


canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
white = PhotoImage(file ="flash-card-project-start/images/card_front.png")
green = PhotoImage(file = "flash-card-project-start/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=white)
# title_text = canvas.create_text(400,150,text="Title",font = ("Ariel",40,"italic"))
# word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
card_title = canvas.create_text(400,150,text="Title",font = ("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))

canvas.grid(row=0,column=0,columnspan=2)

#<------------------randomizing the data----------------->
# def random_word():
#     global word
#     global title_text
#     values = random.choice(df)
#     text_french = values["French"]
#     canvas.delete(word)
#     canvas.delete(title_text)
#     title_text = canvas.create_text(400,150,text="French",font = ("Ariel",40,"italic"))
#     word = canvas.create_text(400, 263, text=text_french, font=("Arial", 60, "italic"))



    

right = PhotoImage(file="flash-card-project-start/images/right.png")
right_button = Button(image=right,highlightthickness=0,command=know)
right_button.grid(row=1,column=1)

wrong = PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong,highlightthickness=0,command=next_card)
wrong_button.grid(row =1,column=0)

next_card()

window.mainloop()