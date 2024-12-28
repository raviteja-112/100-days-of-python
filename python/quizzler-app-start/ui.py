THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window =  Tk() 
        self.window.title("Quizzler")
        self.window.config(padx=20,pady = 20,bg=THEME_COLOR)

        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text="sample text",fill=THEME_COLOR,
                                font=("arial",20,"italic"),
                                width = 280
                                )
        self.canvas.grid(row = 1,column= 0,columnspan=2)

        wrong_image = PhotoImage(file="quizzler-app-start/images/false.png") 
        self.wrong_button = Button(image=wrong_image,highlightthickness=0,command=self.right)
        self.wrong_button.grid(row=2,column=1)

        right_image = PhotoImage(file="quizzler-app-start/images/true.png") 
        self.right_button = Button(image=right_image,highlightthickness=0,command=self.wrong)
        self.right_button.grid(row=2,column=0)

        self.label = Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)
        self.get_next_question()

        


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="you have reached the end of quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    
    def right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def wrong(self):
       is_right =  self.quiz.check_answer("False")
       self.give_feedback(is_right)
    
    def give_feedback(self,is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        