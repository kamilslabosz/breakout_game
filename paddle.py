from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -220)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
