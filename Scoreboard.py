from turtle import Turtle

score = Turtle




class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True):
        super().__init__()
        self.score=0
        with open("data.txt", mode="r") as file:
            self.highscore = score_file = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align="center", font=("Arial", 22, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write ("GAME OVER", align="center", font=("Arial", 22, "normal"))




    def increase_score(self):
        self.score +=1
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align="center", font=("Arial", 22, "normal"))


