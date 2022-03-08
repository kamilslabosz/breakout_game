from turtle import Turtle

COLORS = ["red", "yellow", "green", "blue", "purple"]


class BrickManager:

    def __init__(self):
        self.all_bricks = []

    def create_brick_wall(self):
        for num in range(0, 50):
            new_brick = Turtle('square')
            new_brick.shapesize(stretch_wid=1, stretch_len=2)
            new_brick.penup()
            if num <= 9:
                new_brick.color(COLORS[0])
            elif num <= 19:
                new_brick.color(COLORS[1])
            elif num <= 29:
                new_brick.color(COLORS[2])
            elif num <= 39:
                new_brick.color(COLORS[3])
            else:
                new_brick.color(COLORS[4])

            row = num % 10

            new_brick.goto(x=-230+(row*50), y=150+25*(num//10))
            self.all_bricks.append(new_brick)

