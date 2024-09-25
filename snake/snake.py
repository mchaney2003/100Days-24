from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    """
    The main game character. 
    """
    def __init__(self):
        
        self.body = []
        self.create_snake()

    def create_snake(self):
        #initialize the head
        self.body.append(Turtle(shape="square"))
        self.head = self.body[0]
        self.head.color("white")
        self.head.penup()
        #initialize the body
        self.add_segment()
        self.add_segment()
    
    def add_segment(self):
        """
        Adds another Turtle segment to the end of snake
        """
        #pass it a list of turtles
        self.body.append(Turtle(shape="square"))
        self.body[-1].color("white")
        self.body[-1].penup()
        self.body[-1].setx(self.body[-2].xcor() - 20)
    
    def move_forward(self):
        """
        Move the entire snake body forward and update the screen
        """
        for segment in range(len(self.body) - 1, 0, -1):
            aheads_pos = self.body[segment - 1].pos()
            self.body[segment].setpos(aheads_pos)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:    
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def reset(self):
        for a_turtle in self.body:
            a_turtle.reset()
        self.body.clear()
        self.create_snake()
