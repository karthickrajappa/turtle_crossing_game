import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
game_is_on = True

screen.listen()
screen.onkey(fun=player.move, key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_care()
    car_manager.move()

    if player.ycor() >= 290:
        player.reset_position()
        scoreboard.level_up()
        car_manager.level_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
