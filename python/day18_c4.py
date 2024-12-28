from turtle import Turtle
from random import *

tim = Turtle()


def walk():
    steps = randint(10,100)
    size = randint(1,10)
    for i in range(steps):
        tim.pencolor((random(),random(),random()))
        size = size+0.25
        tim.pensize(size)
        tim.speed(randint(1,10))
        distance = randint(10,100)
        tim.forward(distance)
        if(distance %2 == 0):
            tim.right(randint(10,360))
        else:
            tim.left(randint(10,360))
        
walk()