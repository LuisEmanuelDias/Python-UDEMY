from turtle import Turtle
from random import randint


class Food:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.food = Turtle()
        self.food.shape("circle")
        self.food.shapesize(0.3, 0.3)
        self.food.color("white")
        self.food.pu()
        self.food.speed("fastest")
        self.food.hideturtle()
        self.food.setposition(randint(-width / 2, width / 2), randint(-height / 2, height / 2))
        self.food.showturtle()

    def remove_create(self):
        self.food.hideturtle()
        self.food.setposition(randint(int(-self.width / 2) + 20, int(self.width / 2) - 20),
                              randint(int(-self.height / 2) + 20, int(self.height / 2) - 20))
        self.food.showturtle()
