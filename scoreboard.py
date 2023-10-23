from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 10, "normal"))

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 10, "normal"))
