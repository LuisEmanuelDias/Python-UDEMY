from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.hideturtle()
        self.setposition(-200, 265)
        self.write(f"Level {self.level}", False, align="center", font=("Courier", 20, "normal"))

    def new_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", False, align="center", font=("Courier", 20, "normal"))

    def reset_score(self):
        self.level = 1
        self.clear()
        self.write(f"Level {self.level}", False, align="center", font=("Courier", 20, "normal"))
