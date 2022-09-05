from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

STARTING_POSITION_RIGHT = (350, 0)
STARTING_POSITION_LEFT = (-350, 0)

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Arcade Game")
screen.tracer(0)

paddle_right = Paddle(STARTING_POSITION_RIGHT)
paddle_left = Paddle(STARTING_POSITION_LEFT)
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(paddle_right.move_paddle_up, "8")
screen.onkey(paddle_right.move_paddle_down, "2")
screen.onkey(paddle_left.move_paddle_up, "w")
screen.onkey(paddle_left.move_paddle_down, "s")

play_game = True
while play_game:
    ball.move_speed = 0.1
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.add_right()
        score.update_scoreboard()
    elif ball.xcor() > 380:
        ball.reset_pos()
        score.add_left()
        score.update_scoreboard()
    if score.score_right == 10 or score.score_left == 10:
        play_game = False

screen.exitonclick()
