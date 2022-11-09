from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.paddle_bounces = 0
        self.move_speed = 0.1

    def move(self):
        """Moves the ball in direction set by x_move and y_move."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        """Simulates the ball bouncing off a wall by inverting its y_move value."""
        self.y_move *= -1

    def bounce_back(self):
        """Simulates the ball bouncing off a paddle by inverting its x_move value."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        """Places ball back at center of the screen, inverts its direction of movement, and resets speed."""
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.move()
        self.move_speed = 0.1
