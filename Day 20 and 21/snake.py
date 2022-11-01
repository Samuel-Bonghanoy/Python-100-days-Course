from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self): #what happens every time a snake object is created
        self.segments = []
        self.create_snake()
        self.move()
        self.head = self.segments[0]#positioning. it would not work if it was the first attribute

    def create_snake(self):
        for position in STARTING_POSITIONS:
            if position == (0,0):
                new_segment = Turtle("circle")
            else:
                new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        previous_segment = len(self.segments) - 1
        new_x = self.segments[previous_segment].xcor()
        new_y = self.segments[previous_segment].ycor()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)
        
    def up(self):  
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):  
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):  
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):  
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    
