import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

serpent = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(serpent.up, "Up")
screen.onkey(serpent.down,"Down")
screen.onkey(serpent.left,"Left")
screen.onkey(serpent.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    serpent.move()


    #Detect collision with food
    if serpent.head.distance(food) < 15:
        food.refresh()
        serpent.extend()
        scoreboard.add_score()

    #Detect collision with wall

    if serpent.head.xcor() > 280 or serpent.head.xcor() < -280 or serpent.head.ycor() > 280 or serpent.head.ycor() < -280:
        scoreboard.reset()
        serpent.reset()

    #Detect collision with tail
    for t in serpent.t_list[1:]:
        if serpent.head.distance(t) < 10:
            scoreboard.reset()
            serpent.reset()







screen.exitonclick()