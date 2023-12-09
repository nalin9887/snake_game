from turtle import Turtle
import random
STARTING_POSITION=[(0, 0), (-20, 0), (-40, 0)]
Move=20
count=1
Color=["Red","White"]
class Snake:



    def __init__(self):

        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):

        for position in STARTING_POSITION:
            self.add_seg(position)


    def add_seg(self,position):

         tim=Turtle()
         tim.shape("square")

         tim.color(random.choice(Color))

         tim.penup()
         tim.goto(position)
         self.segment.append(tim)

    def expand(self):
        self.add_seg(self.segment[-1].position())


    def move(self):
        for seg in range(len(self.segment)-1,0,-1):

            n_seg_x=self.segment[seg-1].xcor()
            n_seg_y=self.segment[seg-1].ycor()
            self.segment[seg].goto(n_seg_x,n_seg_y)
        self.segment[0].forward(Move)
    def up(self):
        if self.segment[0].heading() != 270:
         self.segment[0].setheading(90)
    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)
    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)
    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]
