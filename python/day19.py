from turtle import Turtle,Screen
import random

isgameon = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red","orange","yellow","green","blue","purple"]
tims = []

user_bet = screen.textinput(title="Make your bet",prompt="Which one will win the race? Enter the color:")
y = -100
for turtle_index in range(0,6):
    tim = Turtle("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y)
    y += 50
    tims.append(tim)

if user_bet:
    isgameon = True

while isgameon:
    for turtle in tims:
        if turtle.xcor() > 230:
            isgameon = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won the rae with {user_bet} color!")
            else:
                print(f"you have lost the game with {user_bet} color turtle!")
        distance = random.randint(0,10)
        turtle.forward(distance)