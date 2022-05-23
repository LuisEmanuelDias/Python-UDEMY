from turtle import Turtle
from math import *


class Body:
    def __init__(self):
        self.snake = [Turtle("square"), Turtle("square"), Turtle("square"), Turtle("square")]
        i = 0

        for x in self.snake:
            x.speed("fastest")
            x.pu()
            x.clear()
            x.color("white")
            x.setposition(-20 * i, 0)
            i += 1
            x.shapesize(1, 1)

    def new_part(self):
        self.snake += [Turtle("square")]
        self.snake[len(self.snake) - 1].hideturtle()
        self.snake[len(self.snake) - 1].shapesize(1, 1)
        self.snake[len(self.snake) - 1].color("white")
        self.snake[len(self.snake) - 1].pu()
        self.snake[len(self.snake) - 1].clear()
        self.snake[len(self.snake) - 1].speed("fastest")

        self.snake[len(self.snake) - 1].setposition(self.snake[len(self.snake) - 2].pos())
        self.snake[len(self.snake) - 1].showturtle()

    def follow_snake_parts(self, first_pos):

        for part in self.snake[1:len(self.snake)]:
            second_pos = part.pos()
            part.setposition(first_pos)
            first_pos = second_pos

    #    for m in range(1, len(self.snake)):
    #        second_pos = self.snake[m].pos()
    #        self.snake[m].setposition(first_pos)
    #        first_pos = second_pos

    def move_fd(self):
        prev = self.snake[0].pos()
        self.snake[0].fd(20)
        self.follow_snake_parts(first_pos=prev)

    def move_left(self):
        self.snake[0].lt(90)

    def move_right(self):
        self.snake[0].rt(90)

    def reset(self):

        self.snake[0].reset()
