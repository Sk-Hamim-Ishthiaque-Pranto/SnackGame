from turtle import Turtle
FONT = ('Arial', 12, 'normal')
ALIGN = 'center'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=370)
        self.score = 0
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='Game Over', move=False, align=ALIGN, font=('Arial', 30, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

