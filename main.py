import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager,COLORS
from scoreboard import Scoreboard
import random


s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

sc=Scoreboard()


c=CarManager()
p=Player()
s.listen()
s.onkey(p.up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    c.create()
    c.move()

    for i in c.all:
        if i.distance(p)<20:
            sc.end()
            game_is_on=False

    if p.finish():
        p.start()
        c.level()
        sc.update()
        

s.exitonclick()