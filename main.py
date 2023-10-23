from turtle import Turtle, Screen

from food import Food
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
food = Food()

# listen for keyboard input

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move snake body

is_game_running = True
while is_game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision

    if snake.head.distance(food) < 15:
        food.spawn_food()


screen.exitonclick()
