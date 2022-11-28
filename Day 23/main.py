import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("black")

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1 / scoreboard.score)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
       if car.distance(player) < 20:
          scoreboard.game_over()
          game_is_on = False
          

    if player.is_at_finish_line():
        player.start()
        scoreboard.point()


screen.exitonclick()