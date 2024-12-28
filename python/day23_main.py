import time
from turtle import Screen
from day23_player import Player
from day23_car_manager import CarManager
from day23_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.allcars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    if player.isfinished():
        player.gotostart()
        car_manager.level_up()
       


screen.exitonclick()
        
