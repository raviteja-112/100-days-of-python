MOV_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARINGPOSTION = [(0,0) ,(-20,0),(-40,0)]
from turtle import Turtle
class Snake:
    
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        

    def create_snake(self):
        
        for i in STARINGPOSTION:
            self.add_turtle(i)
            
    
    def add_turtle(self,position):

        tim = Turtle()
        tim.color("white")
        tim.speed("fastest")
        tim.shape("square")
        tim.penup()
        tim.goto(position)

        self.turtles.append(tim)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())





    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
            xcor = self.turtles[i-1].xcor()
            ycor = self.turtles[i-1].ycor()
            self.turtles[i].goto(xcor,ycor)
        self.turtles[0].forward(MOV_DISTANCE)


    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)
    

    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)
    

    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
    

    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
    

