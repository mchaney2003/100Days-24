from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
GAMEOVERFONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("24/snake/data.txt", "r") as highscorefile:
            self.highscore = int(highscorefile.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.clear()
        self.write("score: {} High Score: {}".format(self.score, 
            self.highscore), align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAMEOVERFONT)

    def reset(self):
        if self.score > self.highscore:
            with open("24/snake/data.txt", "w") as highscorefile:
                highscorefile.write(str(self.score))    
            self.highscore = self.score
        self.score = 0
        self.refresh()