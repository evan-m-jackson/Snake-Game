from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.t_list = []
        self.create_snake()
        self.head = self.t_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.t_list.append(t)

    def reset(self):
        for t in self.t_list:
            t.goto(1000,1000)
        self.t_list.clear()
        self.create_snake()
        self.head = self.t_list[0]

    def extend(self):
        self.add_segment(self.t_list[-1].position())

    def move(self):
        for t_num in range(len(self.t_list) - 1, 0, -1):
            new_x = self.t_list[t_num - 1].xcor()
            new_y = self.t_list[t_num - 1].ycor()
            self.t_list[t_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)