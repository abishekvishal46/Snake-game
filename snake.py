import random
from turtle import Turtle
STARING_POS=[(0,0),(-20,0),(-40,0)]
COLOR=["red","yellow","blue","pink","green","orange"]

class Snake:
    def __init__(self):
        self.snakes=[]
        self.create_snake()

    def create_snake(self):
         for position in STARING_POS:
           self.add_snakes(position)
    def add_snakes(self,position):
        dan = Turtle(shape="square")

        dan.color(random.choice(COLOR))
        dan.penup()
        dan.goto(position)
        self.snakes.append(dan)
    def extend(self):
        self.add_snakes(self.snakes[-1].position())
    def move(self):

        for i in range(len(self.snakes)-1, 0, -1):
            x = self.snakes[i - 1].xcor()
            y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x, y)
        self.snakes[0].forward(20)
    def add(self):
        dan = Turtle(shape="square")
        dan.speed("slowest")
        dan.color("white")

        dan.penup()
        self.snakes.append(dan)
    def restart(self):
        self.snakes[0].goto(1000,1000)
        self.snakes.clear()
        self.create_snake()


    def up(self):
       if  self.snakes[0].heading()!=270:

         self.snakes[0].setheading(90)
    def left(self):
        if self.snakes[0].heading() != 0:
         self.snakes[0].setheading(180)
    def right(self):
        if self.snakes[0].heading() != 180:
         self.snakes[0].setheading(0)
    def down(self):
        if self.snakes[0].heading() != 90:
         self.snakes[0].setheading(270)

