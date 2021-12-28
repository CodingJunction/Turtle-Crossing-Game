from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,266)
        self.pendown()
        self.write(f"Level : {self.level}",font=FONT)

    def update(self):
        self.level+=1
        self.clear()
        self.write(f"Level : {self.level}",font=FONT)

    def end(self):
        self.clear()
        self.penup()
        self.goto(-30,0)
        self.pendown()
        self.write(f"GAME OVER.",font=FONT)


