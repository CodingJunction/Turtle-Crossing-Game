from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all=[]
        self.speed=STARTING_MOVE_DISTANCE
        self.create()
     
        

    def create(self):
        r=random.randint(1,6)
        if r==6:

            t=Turtle("square")
            t.shapesize(1,2)
            t.color(random.choice(COLORS))
            t.penup()
            t.goto(300,random.randint(-250,250))
            t.pendown()
            self.all.append(t)

    def move(self):

        for i in self.all:
            i.penup()
            i.backward(self.speed)
            i.pendown()

    def level(self):
        self.speed+=10


