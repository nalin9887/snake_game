from turtle import Turtle,Screen
import time
from food import Food
from score import Score
from snake import Snake

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("EAT THE TURTLE")
screen.tracer(0)

tim=Snake()
food=Food()
scor=Score()

screen.listen()
screen.onkey(tim.up,"w")
screen.onkey(tim.down,"s")
screen.onkey(tim.right,"d")
screen.onkey(tim.left,"a")

game_on=True

while game_on:

    tim.move()
    screen.update()
    time.sleep(0.1)
    if tim.head.distance(food)< 15:
        food.refresh()
        scor.incscore()

        tim.expand()

    for n in tim.segment[1:]:

            if tim.head.distance(n)<10:
                scor.reset()
                scor.gameover()
                tim.reset()
    if tim.head.xcor() >280 or  tim.head.xcor() < -280 or tim.head.ycor()>280 or tim.head.ycor()<-280:
        tim.reset()
        scor.reset()










screen.exitonclick()
