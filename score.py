from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.score_left, align="center", font=('Arial', 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=self.score_right, align="center", font=('Arial', 80, 'normal'))

    def add_right(self):
        self.score_right += 1

    def add_left(self):
        self.score_left += 1
