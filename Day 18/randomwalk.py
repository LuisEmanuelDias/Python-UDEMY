from turtle import Turtle, Screen, colormode
from random import choice, randint
angles = [0, 90, 180, 270]
tim = Turtle()
tim.shape("circle")
tim.pensize(15)
tim.speed("fastest")
colormode(255)

for n in range(1000):
    tim.color(randint(1, 255), randint(1, 255),randint(1, 255))
    #tim.lt(choice(angles))
    tim.lt(randint(0,359))
    tim.fd(50)

my_screen = Screen()
my_screen.exitonclick()
