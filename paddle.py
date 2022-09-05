from turtle import Turtle
from turtle import Screen
STARTING_POSITION_RIGHT = (380, 0)
screen = Screen()


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1.0, stretch_wid=5.0)
        self.goto(starting_position)

    def move_paddle_up(self):
        screen.tracer(0)
        if self.ycor() < 220:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        screen.update()

    def move_paddle_down(self):
        screen.tracer(0)
        if self.ycor() > -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        screen.update()

