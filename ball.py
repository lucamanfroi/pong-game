from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.speed(0)
        self.shapesize(0.5, 0.5)
        self.color('orange')
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.x_move *= 1.1
        self.y_move *= 1.1

    def restart(self):
        self.goto(0, 0)
