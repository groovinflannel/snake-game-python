import turtle
from turtle import Turtle

MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]

    def create_body(self):
        for turtle in range(0, 3):
            turt = Turtle(shape="square")
            turt.color("white")
            turt.penup()
            self.body.append(turt)
            current_index = self.body.index(turt)
            left_spacing = -20
            turt.setx(current_index * left_spacing)

    def move(self):

        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)

        self.body[0].forward(MOVEMENT_DISTANCE)


    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def right(self):
        self.head.setheading(RIGHT)

    def left(self):
        self.head.setheading(LEFT)
