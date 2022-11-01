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

# while True:
#     rgb = random_color()
#     timmy.color(rgb)
#     timmy.setheading(random.choice(directions))
#     timmy.forward(40)

angle = 0
for n in range(180):
    rgb = random_color()
    timmy.color(rgb)
    timmy.circle(120, 360)
    timmy.setheading(angle)
    angle += 2

timmy.forward(300)

angle = 0
for n in range(180):
    rgb = random_color()
    timmy.color(rgb)
    timmy.circle(120, 360)
    timmy.setheading(angle)
    angle += 2

timmy.left(180)
timmy.forward(600)

for n in range(180):
    rgb = random_color()
    timmy.color(rgb)
    timmy.circle(120, 360)
    timmy.setheading(angle)
    angle += 2