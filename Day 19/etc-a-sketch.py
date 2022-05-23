from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor('yellow')

spaceship = Turtle()

wn.listen()

wn.onkeypress(lambda: spaceship.fd(1), 'w')
wn.onkey(lambda: spaceship.bk(190), 's')
wn.onkey(lambda: spaceship.rt(20), 'd')
wn.onkey(lambda: spaceship.lt(20), 'a')
wn.onkey(lambda: spaceship.clear(), 'c')

wn.exitonclick()


