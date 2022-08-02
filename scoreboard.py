from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Verdana', 55)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.write(arg=f'{self.l_score}         {self.r_score}', align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.write(arg=f'{self.l_score}         {self.r_score}', align=ALIGNMENT, font=FONT)
