from turtle import Turtle, Screen

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Perry the Python (Snake Game)")

# create initial snake body
snake = []
for turtle in range(0, 3):
    turt = Turtle(shape="square")
    turt.color("white")
    snake.append(turt)
    current_index = snake.index(turt)
    left_spacing = -20;
    turt.setx(current_index * left_spacing)


screen.exitonclick()
