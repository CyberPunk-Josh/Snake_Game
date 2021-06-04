from turtle import Turtle

ARG = "Score"
MOVE = False
ALIGN = "center"
FONT = ("Verdana", 15, "normal")
SCORE = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", move=False, align="center",
                   font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center",
                   font=("Arial", 25, "normal"))

