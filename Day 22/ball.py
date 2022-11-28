from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction = [10, 10]
        self.move_speed = 0.1

    def movement(self):
        new_x = self.xcor() + self.direction[0]
        new_y = self.ycor() + self.direction[1]
        self.goto(new_x, new_y)

    def wall_bounce(self):
        new_y_direction = self.direction[1] * (-1)
        self.direction[1] = new_y_direction


    def paddle_bounce(self):
        new_x_direction = self.direction[0] * (-1)
        self.direction[0] = new_x_direction 
        self.move_speed *= 0.5
        
    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.paddle_bounce()