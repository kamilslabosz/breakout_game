from turtle import Screen, Turtle

from brick_manager import BrickManager
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Breakout!")
screen.tracer(0)

brick_manager = BrickManager()
paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_is_on = True

brick_manager.create_brick_wall()
while game_is_on:
    screen.update()
    ball.move()

    for brick in brick_manager.all_bricks:
        if ball.distance(brick) < 20:
            brick.goto(0, -320)
            ball.bounce_y()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() < -200:
        ball.bounce_y()

    if ball.ycor() < -280:
        game_is_on = False
        game_over = Turtle()
        game_over.penup()
        game_over.ht()
        game_over.goto(0, 0)
        game_over.write('Game Over', align="center", font=("Courier", 80, "normal"))

screen.exitonclick()
