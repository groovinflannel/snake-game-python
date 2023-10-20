from turtle import Turtle, Screen
from snake import Snake
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Perry the Python (Snake Game)")
screen.tracer(0)

# create initial snake body

snake = Snake()

# move snake body

is_game_running = True
while is_game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
