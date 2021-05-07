from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        # self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, -30)
        self.write(f"Your Score: {self.score}", font=("Courier", 25, "bold"))

    def add_point(self, score):
        self.score = score
        # self.update_scoreboard()
