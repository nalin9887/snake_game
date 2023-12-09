from turtle import Turtle
FONT=("Courier",18,"bold")
ALIGN="center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("Data.txt") as data:
            self.highscore = int(data.read())
        self.color("White")
        self.ht()
        self.penup()

        self.goto(0,260)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} high score: {self.highscore}",align=ALIGN,font=FONT)
    def reset(self):
        if self.score>self.highscore:
         self.highscore=self.score
         with open("Data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0

        self.update_score()
    def incscore(self):
        self.clear()
        self.score+=1
        # self.write(f" Final Score is : {self.score} Highest Score is : {self.highscore} ",False,align=ALIGN,font=FONT)
        self.update_score()



    def gameover(self):
         self.clear()
         self.goto(0,0)
         self.write(f"       Game Over!! \n Your Final Score is : {self.score} ",False,align=ALIGN,font=FONT)
         self.write(" \n\n\n\n\n\n\n\n\n\n \n\n\n\n\n \n\n\n\n\n        TRY AGAIN!!! ",False,align=ALIGN,font=("Courier",12,"bold"))
