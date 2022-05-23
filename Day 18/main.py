from turtle import Turtle, Screen,colormode
import turtle
from random import randint
tim = Turtle()
tim.shape("circle")
tim.pu()
tim.goto(-100, -200)
tim.pd()
colormode(255)

for n in range(3, 12):
    tim.color(randint(1, 255), randint(1, 255),randint(1, 255))
    for x in range(n):
        tim.fd(100)
        tim.lt(360/n)

my_screen = Screen()
my_screen.exitonclick()
