from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-400, y=330)
        self.write(f"Level: {self.score}", align='Left', font=("Courier", 15, "normal"))
       
    def update(self):
        self.clear()
        self.score += 1
        self.penup()
        self.color("black")
        self.goto(x=-400, y=330)
        self.write(f"Level: {self.score}", align='Left', font=("Courier", 15, "normal"))
        
        
    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.write("GAME OVER", align='Center', font=("Courier", 20, "normal"))
        self.color("black")