from turtle import Turtle, Screen
from turtle import * #use this to import everything in that module
import turtle as t #use t as the alias name

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkRed")


timmy.pensize(10)
timmy.width(5)

# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# while True:
#     timmy.forward(100)
#     timmy.penup()
#     timmy.forward(100)
#     timmy.pendown()
#     timmy.forward(100)
#     timmy.right(90)

for n in range (3):
    timmy.forward(100)
    timmy.right(120)

for n in range (5):
    timmy.forward(100)
    if n == 4:
        break
    else:
        timmy.right(90)

for n in range (5):
    timmy.right(72)
    timmy.forward(100)

for n in range (6):
    timmy.right(60)
    timmy.forward(100)

for n in range (7):
    timmy.right(51.42)
    timmy.forward(100)

for n in range (8):
    timmy.right(45)
    timmy.forward(100)

for n in range (9):
    timmy.right(40)
    timmy.forward(100)

# timmy.left(90)
# timmy.forward(100)

# for n in range (3):
#     timmy.forward(100)
#     timmy.right(120)

# for n in range (5):
#     timmy.forward(100)
#     if n == 4:
#         break
#     else:
#         timmy.right(90)

# for n in range (5):
#     timmy.right(72)
#     timmy.forward(100)

# for n in range (6):
#     timmy.right(60)
#     timmy.forward(100)

# for n in range (7):
#     timmy.right(51.42)
#     timmy.forward(100)

# for n in range (8):
#     timmy.right(45)
#     timmy.forward(100)

# for n in range (9):
#     timmy.right(40)
#     timmy.forward(100)





screen = Screen()
screen.exitonclick()