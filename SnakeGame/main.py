import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# start listening for specified keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game stays on until game ending event
game_is_on = True
while game_is_on:

    # update the screen every 1/10th of a second
    screen.update()
    time.sleep(0.1)

    # move the snake forward
    snake.move()

    # if snake head comes in contact with food object:
    # generate new food piece, increase score, and extend the length of the snake
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # if head of snake reaches outer bounds then game is over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # if snake head collides with any segment of its body other than the head, trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
