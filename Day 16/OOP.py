'''
AN OBJECT HAS 2 PARTS: WHAT IS HAS AND WHAT IT DOES
OBJECT WITH ATTRIBUTES AND METHODS
AN ATTRIBUTE IS A TYPE OF VARIABLE ASSOCIATED WITH AN OBJECT
A METHOD IS A FUNCTION SPECIFIC TO A PARTICULAR OBJECT

A CLASS IS THE DEFINITION AND AN OBJECT IS AN INDIVIDUAL ENTITY OF THE CLASS
U CAN USE CLASS BLUEPRINTS TO CREATE AN OBJECT

an object is the actual thing used in code

when creating a new object it looks like this 
car = CarBlueprint()
it is written in pascal case wherein the first letter of every word is capitalized rather than separated by underscores
'''
import turtle
import random
# import matplotlib

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("coral")

# timmy.forward(100)
# timmy.backward(100)
while True:
    timmy.setheading(random.randint(0, 270))
    timmy.forward(random.randint(0, 300))
    timmy.circle(100)

screen = turtle.Screen()
print(screen.canvheight)
screen.exitonclick()