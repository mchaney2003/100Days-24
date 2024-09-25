from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.xcoord = random.randint(-280,280)
        self.ycoord = random.randint(-280,280)
        self.goto(self.xcoord, self.ycoord)