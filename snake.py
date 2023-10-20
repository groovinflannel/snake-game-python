from turtle import Turtle

MOVEMENT_DISTANCE = 20

class Snake:

    def __init__(self):
        self.body = []
        self.create_body()

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
