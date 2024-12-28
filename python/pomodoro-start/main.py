from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    label1.config(text="Timer",fg = GREEN)
    mark =""
    tick.config(text = mark)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        if reps % 8 == 0:
            count_down(long_break_sec)
            label1.config(text="Break",font=(FONT_NAME,45),fg=RED,bg=YELLOW)
            window.attributes('-topmost', True)
        else:
            count_down(short_break_sec)
            label1.config(text="Break",font=(FONT_NAME,45),fg=PINK,bg=YELLOW)
            window.attributes('-topmost', True)
            
    else:
        count_down(work_sec) 
        label1.config(text="Work",font=(FONT_NAME,45),fg=GREEN,bg=YELLOW)
        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer =  window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file = "pomodoro-start/tomato.png")
canvas.create_image(100,112,image = tomato)
timer_text = canvas.create_text(100,142,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))

canvas.grid(column=1,row=1)

label1 = Label(text="Timer",font=(FONT_NAME,45),fg=GREEN,bg=YELLOW)
label1.grid(column=1,row=0)

tick = Label(text="",font=(FONT_NAME,24),fg=GREEN,bg=YELLOW)
tick.grid(row = 4,column=1)

start = Button(text="Start",command=start_timer)
start.grid(row =2,column = 0)

reset = Button(text="reset",command=reset_timer)
reset.grid(row =2,column = 2)

window.mainloop()