from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Entera color?")

all_turtles = []

red = Turtle(shape="turtle")
red.color("red")
red.penup()
red.goto(x=-230, y= -100)
all_turtles.append(red)

blue = Turtle(shape="turtle")
blue.color("blue")
blue.penup()
blue.goto(x=-230, y= -50)
all_turtles.append(blue)

green = Turtle(shape="turtle")
green.color("green")
green.penup()
green.goto(x=-230, y= 0)
all_turtles.append(green)

purple = Turtle(shape="turtle")
purple.color("purple")
purple.penup()
purple.goto(x=-230, y= 50)
all_turtles.append(purple)

yellow = Turtle(shape="turtle")
yellow.color("yellow")
yellow.penup()
yellow.goto(x=-230, y= 100)
all_turtles.append(yellow)

orange = Turtle(shape="turtle")
orange.color("orange")
orange.penup()
orange.goto(x=-230, y= 150)
all_turtles.append(orange)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! the {winning_color} turtle won the race.")
            else:
                print(f"You have lost! the {winning_color} turtle won the race.")

        distance = random.randint(0,10)
        turtle.forward(distance)







screen.exitonclick()