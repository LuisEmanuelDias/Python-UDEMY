from turtle import Turtle
from random import randint, choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        number = randint(0, 60)
        self.setheading(choice([number, 360 - number, 180 - number, 180 + number]))
        self.shape("circle")
        self.color("white")
        self.pu()
        self.speed("fastest")

    def new_pos(self,win):
        self.setpos(0, 0)
        number = randint(0, 60)
        if win == "left":
            self.setheading(choice([number, 360 - number]))
        else:
            self.setheading(choice([180 - number, 180 + number]))
