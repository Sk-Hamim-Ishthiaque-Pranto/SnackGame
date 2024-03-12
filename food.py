from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.7, stretch_wid=.7)
        self.color('red')
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-350, 350), y=random.randint(-350, 350))
