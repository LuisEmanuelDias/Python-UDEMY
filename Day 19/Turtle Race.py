from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.bgcolor('lightblue')
screen.setup(500, 500)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for n in range(0, 6):
    turtle1 = Turtle(shape="turtle")
    turtle1.pu()
    turtle1.color(colors[n])
    turtle1.goto(-230, -100 + 30*n)
    turtles += [turtle1]


bet = ""
bet = screen.textinput("Make your bet", "Who will win the race? Enter a colour: ").lower()

race_on = True

while race_on:
    for turtX in turtles:
        if turtX.xcor() > 200:
            if turtX.color()[0] == bet:
                print("You WIN!!")
            else:
                print(f"You lose! {turtX.color()[0].upper()} turtle win the race")
            race_on = False
        else:
            turtX.fd(randint(0, 10))
