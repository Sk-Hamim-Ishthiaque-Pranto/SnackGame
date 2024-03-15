from turtle import Turtle
FONT = ('Courier', 24, 'normal')
ALIGN = 'center'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=365)
        self.score = 0
        with open('high_score.text', 'r') as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def refresh(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('high_score.text', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
