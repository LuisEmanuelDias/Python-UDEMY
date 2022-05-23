from body import *
from turtle import Screen
from food import *
from colision_controller import *
from scoreboard import Scoreboard

# Partir problema en pedazos para el juego de la serpiente:

# Crear la serpiente, bloques que se mueven juntos, cada vez que come aumenta un cuadrado
# body es una clase que contiene los atributos largo, posiciones del cuerpo y el movimiento del mismo(cada cuadraddo
# debe seguir al anterior)
# Food es una clase para generar comida
# Colision controller, tiene como atributo el ancho y largo de la ventana, además de el diccionario con las
# posiciones del cuerpo

screen = Screen()
screen.bgcolor("black")
screen.title("My snake game")
screen.setup(500, 500)
screen.listen()
snake = Body()
food = Food(500, 500)
collision = CollisionController(500, 500, snake.snake)
screen.tracer(0)
scoreboard = Scoreboard()
game_over = False


def movement():
    snake.move_fd()
    screen.update()
    screen.onkey(lambda: snake.move_right(), 'd')
    screen.onkey(lambda: snake.move_left(), 'a')
    screen.onkey(lambda: snake.reset(), 'r')
    global game_over
    if not collision.collision():
        game_over = True
    if collision.food_collision(food.food.pos()):
        food.remove_create()
        snake.new_part()
        scoreboard.update_score()

    screen.update()
    if not game_over:
        screen.ontimer(lambda: movement(), 100)


movement()

screen.exitonclick()
