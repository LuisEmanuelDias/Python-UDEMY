from turtle import Turtle, Screen


class CollisionController:
    def __init__(self, height, width, snake):

        self.snake = snake
        self.height = height / 2
        self.width = width / 2

    def collision(self):
        counter = 0

        counter += 0 + (self.width - (abs(self.snake[0].pos()[0])) < 20) * 1
        counter += 0 + (self.height - (abs(self.snake[0].pos()[1])) < 20) * 1

        for part in self.snake[1:len(self.snake)]:
            counter += 0 + (self.snake[0].pos() == part.pos()) * 1

        return counter == 0

    def food_collision(self, pos_food):
        if self.snake[0].distance(pos_food) < 15:
            return True
