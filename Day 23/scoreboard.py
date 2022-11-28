FONT = ("Courier", 16, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update()
    
    def point(self):
        self.score +=1
        self.update()

    def update(self):
        self.clear()
        self.goto(-270, 300)
        self.write((f"Level: {self.score}"), align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write
        self.write((f"GAME OVER"), align="center", font=FONT)
        