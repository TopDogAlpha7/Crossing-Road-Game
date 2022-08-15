from turtle import Turtle, distance
import random
import turtle

colours = ["red", "orange", "yellow", "green", "blue",
"violet", "aqua", "aquamarine", "midnight blue"
]
y_positions = [0, 80, 160, 240, -80, -160, -240]

car_speeds = [12, 15, 20, 22, 24, 30, 37, 43, 27]

MOVE_SPEED = 10

class Cars():
    def __init__(self):
        self.new_car = []
        self.movement = 0.1

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            t = Turtle()
            t.shape("square")
            t.shapesize(stretch_len=2, stretch_wid=1)
            t.color(random.choice(colours))
            t.penup()
            t.goto(x=320, y=(random.choice(y_positions)))
            self.new_car.append(t)
       
    def move(self):
        for car in self.new_car:
            car.backward(MOVE_SPEED)

    def new_level(self):
        self.movement *= 1.2
           

            


