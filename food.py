from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")


    def refresh(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x=x_position, y=y_position)



