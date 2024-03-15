from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class SnakeClass:

    def __init__(self):
        self.lst = []
        self.create_snake()
        self.head = self.lst[0]
        self.head.color('green')

    def create_snake(self):
        for item in STARTING_POSITIONS:
            self.add_segment(item)

    def add_segment(self, position):
        new_item = Turtle('square')
        new_item.color('white')
        new_item.penup()
        new_item.goto(position)
        self.lst.append(new_item)

    def refresh(self):
        for seg in self.lst:
            seg.goto(1000, 1000)
        self.lst.clear()
        self.create_snake()
        self.head = self.lst[0]
        self.head.color('green')

    def extend(self):
        self.add_segment(self.lst[-1].position())

    def move(self):
        for num in range(len(self.lst) - 1, 0, -1):
            self.lst[num].goto(x=self.lst[num - 1].xcor(), y=self.lst[num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
