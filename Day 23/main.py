from turtle import Screen
from car import *
from random import randint
from player import *
from scoreboard import *

screen = Screen()
screen.setup(600, 600)
screen.title("TURTLE CROSS THE STREET")
screen.colormode(255)
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()

player = Player()
probability = 90
cars = [Car(), Car()]
game_over = False
level = 1


def movement():
    screen.update()
    global cars
    global game_over
    global probability
    global player
    global level

    indices = list()
    if randint(0, 100) > probability:
        cars += [Car()]
    if len(cars) != 0:
        for x in range(0, len(cars)):
            cars[x].move_fd()
            if cars[x].xcor() < -400 and cars[x].heading() == 180:
                cars[x].setheading(0)
            if cars[x].xcor() > 330 and cars[x].heading() == 0:
                indices += [x]

            if player.distance(cars[x]) < 20:
                game_over = True
    i = 0
    for m in indices:
        cars.pop(m - i)
        i += 1

    screen.onkeypress(lambda: player.forward(20), 'w')
    screen.onkeypress(lambda: player.backward(20), 's')
    screen.onkeypress(lambda: player.setpos(player.xcor() + -20, player.ycor()), 'a')
    screen.onkeypress(lambda: player.setpos(player.xcor() + 20, player.ycor()), 'd')

    if player.ycor() > 270:
        probability -= 2
        player.reset_pos()
        scoreboard.new_score()

    if game_over:
        scoreboard.reset_score()
        probability = 90
        player.reset_pos()
        game_over = False
        screen.ontimer(lambda: movement(), 50)
    else:
        screen.ontimer(lambda: movement(), 50)


movement()

screen.exitonclick()
