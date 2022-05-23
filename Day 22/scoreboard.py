from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self,scorei,scored):
        super().__init__()
        self.scorei = scorei
        self.scored = scored
        self.pu()
        self.hideturtle()
        self.setposition(0, 100)
        self.color("white")
        self.write(f"{scorei}  {scored}", False, align="center", font=("Modern", 100, "normal"))
        self.setheading(270)
        self.setposition(0, 250)
        while self.pos()[1] > -250:
            self.pd()
            self.fd(20)
            self.pu()
            self.fd(20)

    def write_score(self,who):
        self.pu()
        self.setposition(0, 100)
        self.clear()
        if who == "left":
            self.scorei +=1
        elif who == "right":
            self.scored +=1
        self.write(f"{self.scorei}  {self.scored}", False, align="center", font=("Modern", 100, "normal"))
        self.setposition(0, 250)
        while self.pos()[1] > -250:
            self.pd()
            self.fd(20)
            self.pu()
            self.fd(20)

