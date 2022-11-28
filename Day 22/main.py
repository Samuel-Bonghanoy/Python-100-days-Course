from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#Screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Creating a line
line = Turtle()
line.color("white")
line.hideturtle()
line.pensize(5)
line.right(90)
line.forward(300)
line.backward(600)

#Paddle Initializations
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#Ball initialization
ball = Ball()

#Scoreboard initialization
scoreboard = Scoreboard()

#Screen listening to keyboard commands
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    ball.movement()
    time.sleep(ball.move_speed)
    screen.update()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.wall_bounce()
    
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()

























screen.exitonclick()