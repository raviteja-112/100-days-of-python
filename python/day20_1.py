from turtle import Screen,Turtle
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer()
screen.title("My Snake Game")

turtles = []
x = 0


screen.update()

gameison = True
while gameison:
    screen.update()
    time.sleep(0.1)
    for i in range(len(turtles)-1,0,-1):
        xcor = turtles[i-1].xcor()
        ycor = turtles[i-1].ycor()
        turtles[i].goto(xcor,ycor)
    turtles[0].forward(20)


screen.exitonclick()