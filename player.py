from turtle import Turtle,Screen


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.tiltangle(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.pendown()



    def up(self):

        self.penup()
        self.goto(0,self.ycor()+MOVE_DISTANCE)
        self.pendown()
    
    def finish(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

    def start(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.pendown()

