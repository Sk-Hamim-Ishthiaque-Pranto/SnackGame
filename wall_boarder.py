from turtle import Turtle

POS_BOARDER = 370
NEG_BOARDER = -370


class WallBoarder(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor('red')
        self.pensize(5)

    def create_boarder(self):
        self.goto(NEG_BOARDER, POS_BOARDER)
        self.pendown()
        self.goto(NEG_BOARDER, NEG_BOARDER)
        self.goto(POS_BOARDER, NEG_BOARDER)
        self.goto(POS_BOARDER, POS_BOARDER)
        self.goto(NEG_BOARDER, POS_BOARDER)

