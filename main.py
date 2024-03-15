from turtle import Screen
from snake import SnakeClass
from food import Food
from scoreBoard import ScoreBoard
from wall_boarder import WallBoarder
import time

POS_BOARDER = 365
NEG_BOARDER = -365

sc = Screen()
sc.setup(width=800, height=800)
sc.bgcolor('black')
sc.title('Snake Game')
sc.listen()
sc.tracer(0)

my_snack = SnakeClass()
food = Food()
score_board = ScoreBoard()
wall = WallBoarder()

wall.create_boarder()
condition = True
while condition:
    sc.update()
    time.sleep(0.1)

    my_snack.move()

    sc.onkey(key='Up', fun=my_snack.up)
    sc.onkey(key='Right', fun=my_snack.right)
    sc.onkey(key='Left', fun=my_snack.left)
    sc.onkey(key='Down', fun=my_snack.down)

    # detect collision with food.
    if my_snack.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        my_snack.extend()

    # detect collision with wall.
    if (my_snack.lst[0].xcor() > POS_BOARDER or my_snack.lst[0].xcor() < NEG_BOARDER or my_snack.lst[0].ycor() > POS_BOARDER or
            my_snack.lst[0].ycor() < NEG_BOARDER):
        score_board.refresh()
        my_snack.refresh()

    # detect collision with wall.
    for segment in my_snack.lst[2:]:
        if my_snack.head.distance(segment) < 10:
            score_board.refresh()
            my_snack.refresh()

sc.exitonclick()
