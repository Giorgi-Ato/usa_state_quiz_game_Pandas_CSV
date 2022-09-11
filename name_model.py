from turtle import Turtle


class NameTurtle(Turtle):

    def __init__(self, name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f'{name}')
