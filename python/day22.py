from turtle import Screen,Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
screen.tracer(0)


paddle = Turtle()
screen.listen()

paddle.penup()

paddle.goto(350,0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1,stretch_wid=5)

def Up():
    new_y = paddle.ycor()+20
    paddle.goto(paddle.xcor(),new_y)

def Down():
    new_y = paddle.ycor()-20
    paddle.goto(paddle.xcor(),new_y)
screen.onkey(Up,"Up")
screen.onkey(Down,"Down")


gameison = True
while gameison:
    screen.update()

screen.exitonclick()