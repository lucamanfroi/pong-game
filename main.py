from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


def restart():
    scoreboard.refresh()
    ball.x_move = 5
    ball.y_move = 5
    ball.restart()


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.bgcolor('black')
l_paddle = Paddle(-370)
r_paddle = Paddle(360)
screen.tracer(1)
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')

game_on = True
y = 0.01
while game_on:
    time.sleep(0.01)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect if the ball hits the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect if someone has scored
    if ball.xcor() > 400:
        scoreboard.l_score += 1
        restart()
        ball.bounce_x()
    elif ball.xcor() < -400:
        scoreboard.r_score += 1
        restart()

screen.exitonclick()
