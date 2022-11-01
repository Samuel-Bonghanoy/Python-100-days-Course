from turtle import Turtle, Screen
from turtle import * #use this to import everything in that module
import turtle as t #use t as the alias name
import random


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkRed")
timmy.speed("fastest")


# timmy.pensize(10)
# timmy.width(5)

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =  (r,g,b)
    return random_color

rgb = random_color()
timmy.penup()
timmy.right(90)
timmy.forward(200)
timmy.left(90)
timmy.backward(200)

for x in range(10):

    for n in range(10):
        rgb = random_color()
        timmy.dot(20, rgb)
        if not n == 9:
            timmy.forward(50)

    if x % 2 == 0:
        timmy.left(90)
        timmy.circle(120, 360)
        timmy.forward(50)
        timmy.left(90)
    else:
        timmy.right(90)
        timmy.circle(120, 360)
        timmy.forward(50)
        timmy.right(90)
        
    