from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


#initial setup. This must be done outside the function or the screen
#first instantiates as a large white screen before snapping into place
#as black and small. I think this is due to objects being created upon
#it
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

#turn off screen refeshing to do it manually instead
screen.tracer(0)

game_is_on = True
the_snake = Snake()
food = Food()
scoreboard = Scoreboard()

#screen controls setup
screen.listen()
screen.onkey(the_snake.up,"Up")
screen.onkey(the_snake.down, "Down")
screen.onkey(the_snake.left, "Left")
screen.onkey(the_snake.right, "Right")

while game_is_on:
    time.sleep(0.07)
    the_snake.move_forward()
    screen.update()

    #detect if snake hit food, and trigger food location move if so
    if the_snake.head.distance(food) < 19:
        print("nom nom nom")
        scoreboard.score += 1
        food.refresh()
        scoreboard.refresh()
        the_snake.add_segment()

    #check for collision with the wall
    if (the_snake.head.xcor() > 290 or the_snake.head.xcor() < -290 or 
    the_snake.head.ycor() > 290 or the_snake.head.ycor() < -290):
        scoreboard.reset()
        the_snake.reset()
        food.refresh()
        #food.reset()
    #check for collision with our tail
    #segment slice skips checking position of the head
    for segment in the_snake.body[1:]:
        if the_snake.head.distance(segment) < 10:
            scoreboard.reset()
            the_snake.reset()    
            food.refresh()
            #food.reset()

screen.exitonclick()