from turtle import Screen, onkey
import time
from animal import Animal
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("white")
screen.tracer(0)

animal = Animal()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(animal.Up, "Up")
screen.onkey(animal.Left, "Left")
screen.onkey(animal.Right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(cars.movement)

    cars.create_car()
    cars.move()
    
    if animal.ycor() > 320:
        animal.Refresh()
        scoreboard.update()
        cars.new_level()
        

    for car in cars.new_car:
        if car.distance(animal) < 20:
            game_on = False
            scoreboard.game_over()





screen.exitonclick()