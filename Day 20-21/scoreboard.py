from turtle import *


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.start()

    def update_score(self):
        self.score += 1
        self.clear()
        self.start()

    def start(self):
        self.penup()
        self.color("#303030")
        self.goto(0, -200)
        self.hideturtle()
        self.speed(0)
        self.write(arg=f"{self.score}", align="center", font=("Arial", 300, "bold"))