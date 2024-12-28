from turtle import Turtle
from random import random
tim = Turtle()

def draw(sides):
    angle = 360 / sides
    color_r = random()
    color_g = random()
    color_b = random()
    for i in range(sides):
        tim.pencolor((color_r,color_g,color_b))
        tim.forward(100)
        tim.right(angle)



for i in range(3,11):
    draw(i)
    

    
