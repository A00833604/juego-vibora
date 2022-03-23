"""Snake, classic arcade game.
Exercises
1.La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana.
2. Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.
"""

from contextlib import redirect_stderr
from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def comparar(comparador):
    if comparador==1:
        color= "blue"
    elif comparador==2:
        color= "green"
    elif comparador==3:
        color = "pink"
    elif comparador==4:
        color= "orange"
    elif comparador==5:
        color = "purple" 
    return color
    
def elegirColor(opcion):
        color= comparar(opcion)
        return color

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()

    for body in snake:
        square(body.x, body.y, 9, color_snake)
    square(food.x, food.y, 9, color_comida)
    update()
    ontimer(move, 100)

#Definir el color de la serpiente
while 1==1:
    comparador_snake=randrange(1,5)
    comparador_comida=randrange(1,5)
    if comparador_snake != comparador_comida:
        break
color_snake=elegirColor(comparador_snake)
color_comida=elegirColor(comparador_comida)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
