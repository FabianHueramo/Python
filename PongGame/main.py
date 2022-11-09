import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# set up screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
turtle.tracer(0)
screen.listen()

# create paddles and ball
r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
ball = Ball()
scoreboard = Scoreboard()

# start of game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_back()

    # detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_back()

    # detect collision with left wall
    if ball.xcor() < -380:
        scoreboard.increase_right_score()
        ball.reset_ball()

    # detect collision with right wall
    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        ball.reset_ball()

    # check if a player has reached the winning number of points
    if scoreboard.right_score == 6 or scoreboard.left_score == 6:
        scoreboard.print_winner()
        game_is_on = False

screen.exitonclick()
