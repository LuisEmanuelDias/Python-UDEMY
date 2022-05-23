import colorgram
from turtle import Turtle, Screen, colormode
from random import randint

colors = colorgram.extract('damian.jpg', 25)
tim = Turtle()
colormode(255)
tim.hideturtle()

#print(colors[0].rgb)
i = 0
for x in range(-5, 5):
    for y in range(-5, 5):
        tim.color(colors[randint(0, len(colors)-1)].rgb)
        tim.pu()
        tim.setposition(x*40, y*40)
        tim.pd()
        tim.dot(15)


my_screen = Screen()
my_screen.exitonclick()