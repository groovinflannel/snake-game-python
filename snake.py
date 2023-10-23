from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
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
        for position in STARTING_POSITIONS:
            self.add_body_segment(position)

    def add_body_segment(self, position):
        turt = Turtle(shape="square")
        turt.speed("fastest")
        turt.color("white")
        turt.penup()
        turt.goto(position)
        self.body.append(turt)

    def extend_body(self):
        self.add_body_segment(self.body[-1].position())

    def move(self):

        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)

        self.body[0].forward(MOVEMENT_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading():
            self.head.setheading(LEFT)
