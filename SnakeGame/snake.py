from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SEGMENTS = []
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a new snake object."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a segment at specified position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extends the snake at the last segment."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward in the direction of set heading."""
        # start at last segment, get x and y coordinates of next segment,
        # move segment to coordinates of next segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # move first segment forward because range function is not inclusive
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Changes the snakes heading to point north if not turning on itself."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes the snakes heading to point south if not turning on itself."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes the snakes heading to point west if not turning on itself."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes the snakes heading to point east if not turning on itself."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
