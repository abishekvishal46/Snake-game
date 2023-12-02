from turtle import Turtle
class Score(Turtle):
    def __init__(self):

        super().__init__()

        self.score=0
        with open("datas.txt", mode="w") as datas:
            datas.write("0")

        with open("datas.txt", mode="r") as datas:
          self.highscore=int(datas.read())
        self.penup()
        self.goto(-200,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score{self.highscore}",False,"center",("Arial", 8, "normal"))
    def high(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("datas.txt", mode="w") as datas:
                datas.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()

    def increase(self):

        self.score+=1
        self.update_scoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", font=("Arial", 8, "normal"))
