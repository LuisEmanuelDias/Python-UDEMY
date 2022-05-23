from random import randint


class Collision():
    def __init__(self, ball, height_screen, width_screen, ipaddle, dpaddle):
        self.ipaddle = ipaddle
        self.dpaddle = dpaddle
        self.ball = ball
        self.height = height_screen / 2
        self.width = width_screen / 2

    def check_collision(self):
        for paddlei_part in self.ipaddle.paddle:
            if self.ball.distance(paddlei_part.pos()) < 30 and abs(self.ball.xcor()) < (9 / 10) * self.width:
                if 270 > self.ball.heading() >= 90:
                    self.ball.setheading(-self.ball.heading() + 180 + randint(-10, 10))
                    return True

        for paddled_part in self.dpaddle.paddle:
            if self.ball.distance(paddled_part.pos()) < 30 and abs(self.ball.xcor()) < (9 / 10) * self.width:
                if 90 >= self.ball.heading() >= 0 or 360 >= self.ball.heading() >= 270 :
                    self.ball.setheading(-self.ball.heading() + 180 + randint(-10, 10))
                    return True

        if self.ball.ycor() > self.height - 20 and 180 > self.ball.heading() > 0:
            self.ball.setheading(360 - self.ball.heading())

        if self.ball.ycor() < 20 - self.height and 360 > self.ball.heading() > 180:
            self.ball.setheading(360 - self.ball.heading())

    def check_score(self):
        if abs(self.ball.xcor()) > self.width - 10:
            return True
