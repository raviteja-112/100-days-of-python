from turtle import Screen
from day20_snake import Snake
from day20_food import Food
from day20_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer()
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


gameison = True
while gameison:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        scoreboard.gameover()
        gameison = False
    
    for turtle in snake.turtles[1:]:

        if snake.head.distance(turtle) < 10:
            gameison = False
            scoreboard.gameover()


screen.exitonclick()