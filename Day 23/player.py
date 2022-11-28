from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 350


class Player(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.start()
        self.right(-90)
    
    def move(self):
        self.forward(10)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start(self):
        self.goto(0, -300)
