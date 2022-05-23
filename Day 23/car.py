from turtle import Turtle
from random import randint


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.pu()
        self.shapesize(stretch_len=2.5, stretch_wid=1)
        self.velocity = randint(5, 30)
        self.setposition(300, randint(-230, 230))

    def move_fd(self):
        self.fd(self.velocity)

    def reset_cars(self):
        self.shape("square")
        self.setheading(180)
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.pu()
        self.shapesize(stretch_len=2.5, stretch_wid=1)

