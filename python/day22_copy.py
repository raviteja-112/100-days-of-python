from turtle import Screen,Turtle
from day22_paddle import Paddle
from day22_ball import Ball
from day22_scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.Up,"Up")
screen.onkey(r_paddle.Down,"Down")

screen.onkey(l_paddle.Up,"w")
screen.onkey(l_paddle.Down,"s")


gameison = True
while gameison:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    if ball.xcor() > 340 :
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -340:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()