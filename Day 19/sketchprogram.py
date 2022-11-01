from turtle import Turtle, Screen

kat = Turtle()
screen = Screen()

def move_forward():
    kat.forward(10)

def move_backward():
    kat.backward(10)

def move_right():
    kat.right(10)

def move_left():
    kat.left(10)

def clear_screen():
    kat.home()
    kat.clear()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()

