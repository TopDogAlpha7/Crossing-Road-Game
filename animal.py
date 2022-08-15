from turtle import Turtle

ANGLE = 90

class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.goto(x=0, y=-320)

    def Up(self):
        self.setheading(90)
        self.fd(10)

    def Left(self):
        self.setheading(180)
        self.fd(10)

    def Right(self):
        self.setheading(0)
        self.fd(10)

    def Refresh(self):
        self.goto(x=0, y=-320)