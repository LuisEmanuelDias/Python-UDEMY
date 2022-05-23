from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, width_screen, height_screen):
        super().__init__()
        self.position = position  # left or right
        self.width_screen = width_screen / 2
        self.height_screen = height_screen / 2
        self.paddle = [Turtle("square"), Turtle("square"), Turtle("square"), Turtle("square")]
        i = 0
        for parts in self.paddle:
            parts.speed("fastest")
            parts.pu()
            parts.clear()
            parts.color("white")
            if position == "left":
                parts.setposition((-9 / 10) * self.width_screen, (-20 * i) + 20)
            elif position == "right":
                parts.setposition((9 / 10) * self.width_screen, (-20 * i) + 20)
            i += 1
            parts.shapesize(1, 1)

    def follow(self, first_pos, head_tail):
        if head_tail == "head":
            for part in self.paddle[1:len(self.paddle)]:
                second_pos = part.pos()
                part.setposition(first_pos)
                first_pos = second_pos
        elif head_tail == "tail":
            for m in range(len(self.paddle) - 2, -1, -1):
                second_pos = self.paddle[m].pos()
                self.paddle[m].setposition(first_pos)
                first_pos = second_pos

    def move_up(self):
        prev = self.paddle[0].pos()
        self.paddle[0].setposition(prev[0], prev[1] + 20)
        self.follow(first_pos=prev, head_tail="head")
        prev = self.paddle[0].pos()
        self.paddle[0].setposition(prev[0], prev[1] + 20)
        self.follow(first_pos=prev, head_tail="head")

    def move_back(self):
        prev = self.paddle[3].pos()
        self.paddle[3].setposition(prev[0], prev[1] - 20)
        self.follow(first_pos=prev, head_tail="tail")
        prev = self.paddle[3].pos()
        self.paddle[3].setposition(prev[0], prev[1] - 20)
        self.follow(first_pos=prev, head_tail="tail")
