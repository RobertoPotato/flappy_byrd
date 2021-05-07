from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("blue")
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.goto(x=0, y=0)

    def flap(self):
        new_y = self.ycor() + 15
        self.goto(x=self.xcor(), y=new_y)

    def fall(self, play_speed):
        new_y = self.ycor() - play_speed
        self.goto(x=self.xcor(), y=new_y)
