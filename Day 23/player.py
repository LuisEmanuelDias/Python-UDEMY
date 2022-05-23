from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.setposition(0, -275)
        self.setheading(90)
        self.shape("turtle")

    def reset_pos(self):
        self.hideturtle()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.setposition(0, -275)
        self.showturtle()

