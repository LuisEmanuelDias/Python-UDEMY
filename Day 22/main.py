from turtle import Screen
from Paddle import *
from Ball import *
from collision import *
from scoreboard import *

ipaddle = Paddle(position="left", width_screen=700, height_screen=500)
dpaddle = Paddle(position="right", width_screen=700, height_screen=500)
screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(700, 500)
screen.listen()
screen.tracer(0)
ball = Ball()
collision = Collision(ball=ball, height_screen=500, width_screen=700, ipaddle=ipaddle, dpaddle=dpaddle)
velocity = 30
scoreboard = Scoreboard(scorei=0, scored=0)
mesage = Turtle()
mesage.hideturtle()
mesage.color("white")


def movement():
    screen.update()
    global velocity
    if collision.check_collision() and velocity > 5:
        velocity -= 2
    ball.fd(15)
    screen.onkey(lambda: ipaddle.move_up(), 'w')
    screen.onkey(lambda: ipaddle.move_back(), 's')
    screen.onkey(lambda: dpaddle.move_up(), 'Up')
    screen.onkey(lambda: dpaddle.move_back(), 'Down')
    if collision.check_score():
        if ball.xcor() > 240:
            scoreboard.write_score("left")
            ball.new_pos("right")
        elif ball.xcor() < -240:
            scoreboard.write_score("right")
            ball.new_pos("left")
        velocity = 30

    if scoreboard.scorei > 9 or scoreboard.scored > 9:
        winner = ""
        if scoreboard.scorei > 9:
            winner = "LEFT PLAYER"
        else:
            winner = "RIGTH PLAYER"
        mesage.write(winner+" WIN!!", False, align="center", font=("Courier", 30, "normal"))
    else:
        screen.ontimer(lambda: movement(), velocity)


movement()

screen.exitonclick()
