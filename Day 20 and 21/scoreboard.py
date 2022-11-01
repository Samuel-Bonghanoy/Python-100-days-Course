from tkinter import CENTER
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.color("white")
        self.write(arg="Score: " + str(self.current_score), move=False, align="center", font=("Courier", 14, "bold"))

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.write(arg="Score = " + str(self.current_score), move=False, align="center", font=("Courier", 14, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER" , move=False, align="center", font=("Courier", 14, "bold"))