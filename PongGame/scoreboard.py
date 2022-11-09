from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        self.hideturtle()

    def increase_left_score(self):
        """Increases left player's score."""
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        """Increases right player's score."""
        self.right_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the score board."""
        self.clear()
        self.write(f"Score: {self.left_score} - {self.right_score}", font=FONT, align=ALIGNMENT)

    def print_winner(self):
        """Prints the winner of the game."""
        winner = Turtle()
        winner.color("white")
        if self.left_score == 6:
            winner.write("LEFT Player Wins!", font=FONT, align=ALIGNMENT)
        elif self.right_score == 6:
            winner.write("RIGHT Player Wins!", font=FONT, align=ALIGNMENT)
