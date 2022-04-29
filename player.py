from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.reset_position()

    def reset_position(self):
        self.goto(0, -280)

    def move(self):
        self.goto(0, self.ycor()+10)

