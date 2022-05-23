from turtle import Turtle, Screen, colormode
from random import randint
angles = [0, 90, 180, 270]
tim = Turtle()
tim.shape("circle")
tim.pu()
#tim.goto(0, -200)
tim.pd()

tim.speed("fastest")
colormode(255)

l=0.9
for _ in range(int(360/l)):
    tim.color(randint(1, 255), randint(1, 255),randint(1, 255))
    tim.circle(100)
    tim.setheading(tim.heading() + l)

my_screen = Screen()
my_screen.exitonclick()
