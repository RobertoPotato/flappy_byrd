from turtle import Turtle

FLAP_STRENGTH = 15


class Player(Turtle):
    def __init__(self, image):
        super().__init__()
        self.penup()
        self.image = image
        self.shape(self.image)
        self.color("blue")
        self.shapesize(stretch_len=0.2, stretch_wid=0.2)
        self.goto(x=0, y=0)

    def flap(self):
        new_y = self.ycor() + FLAP_STRENGTH
        self.goto(x=self.xcor(), y=new_y)

    def dive(self):
        new_y = self.ycor() - FLAP_STRENGTH
        self.goto(x=self.xcor(), y=new_y)

    def fall(self, play_speed):
        new_y = self.ycor() - play_speed
        self.goto(x=self.xcor(), y=new_y)
