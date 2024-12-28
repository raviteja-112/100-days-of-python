from turtle import Turtle
FONT = ("Arial", 16, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = -1
        self.penup()
        self.goto(-50,250)
        self.speed("fastest")
        self.color("White")
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.score += 1
        self.clear()
        self.penup()
        self.write(f"Score: {self.score}", font=FONT)
    
    def gameover(self):
        self.goto(0,0)
        self.write("Game over ",align=ALIGNMENT,font=FONT)

