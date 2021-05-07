import random
from turtle import Turtle

HEIGHTS = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]


def draw_obstacle_piece(x_cord, y_cord, height):
    stretch = height / 8
    obstacle_piece = Turtle()
    obstacle_piece.penup()
    obstacle_piece.shape("square")
    obstacle_piece.color("green")
    obstacle_piece.shapesize(stretch_len=2, stretch_wid=stretch)
    obstacle_piece.goto(x_cord, y_cord)
    # DELETE THESE
    # obstacle_piece.xcor()
    # obstacle_piece.ycor()
    return obstacle_piece


class Obstacle:
    def __init__(self, x_cord):
        self.x_cord = x_cord
        self.top_height = random.choice(HEIGHTS)
        self.gap_height = 40
        self.bottom_height = 300 - (self.top_height + self.gap_height)
        self.upper_obstacle = draw_obstacle_piece(x_cord=self.x_cord, y_cord=300 - (self.top_height / 2), height=self.top_height)
        self.lower_obstacle = draw_obstacle_piece(x_cord=self.x_cord, y_cord=-300 + (self.bottom_height / 2), height=self.bottom_height)
        self.print_stuff()

    def get_new_cord(self):
        self.top_height = random.choice(HEIGHTS)
        self.gap_height = 40
        self.bottom_height = 300 - (self.top_height + self.gap_height)

    def print_stuff(self):
        print(f"Ht = {self.top_height}\nHb = {self.bottom_height} \nGap = {self.gap_height} \n")
        print(f"ttl = {self.top_height + self.bottom_height + self.gap_height}")

    def move(self, play_speed):
        if self.upper_obstacle.xcor() < -420 or self.lower_obstacle.xcor() < -420:
            self.upper_obstacle.goto(420, self.upper_obstacle.ycor())
            self.lower_obstacle.goto(420, self.lower_obstacle.ycor())

        new_upper_x_cord = self.upper_obstacle.xcor() - play_speed
        new_lower_x_cord = self.upper_obstacle.xcor() - play_speed
        self.upper_obstacle.goto(new_upper_x_cord, self.upper_obstacle.ycor())
        self.lower_obstacle.goto(new_lower_x_cord, self.lower_obstacle.ycor())
