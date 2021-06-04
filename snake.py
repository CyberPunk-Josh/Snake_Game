from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # creating snake
    def create_snake(self):
        # creating block of snake:
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # moving snake
    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # moving up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # moving right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # moving left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # moving down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
