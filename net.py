from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize (stretch_len=0.5, stretch_wid=0.5)
        self.pensize(3)
        self.make_line()

    def make_line(self):
        self.penup()
        self.goto(0,-300)
        for _ in range(30):
            self.pendown()
            self.setheading(90)
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
