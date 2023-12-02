
from snake import Snake
from turtle import Screen
from scoreboard import Score
import time
from food import *



s=Screen()
s.bgcolor("black")
s.setup(600,600)
s.tracer(0)
go = Snake()
foodie=Food()
sc=Score()









s.listen()
s.onkey(key="Up",fun=go.up)
s.onkey(key="Right",fun=go.right)
s.onkey(key="Left",fun=go.left)
s.onkey(key="Down",fun=go.down)


start=True

while start:
    s.update()
    time.sleep(0.1)
    go.move()
    if go.snakes[0].distance(foodie)<15:

        foodie.refresh()
        go.extend()
        sc.increase()
    if go.snakes[0].xcor()>320 or  go.snakes[0].xcor()<-320:
        start = False
        sc.gameover()
        sc.high()



    if go.snakes[0].ycor() >320 or go.snakes[0].ycor()<-320:
        start = False
        sc.gameover()
        sc.high()


    for i in go.snakes:
        if i==go.snakes[0]:
            pass
        elif go.snakes[0].distance(i) <5:
            start = False
            sc.gameover()





s.exitonclick()