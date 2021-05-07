from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from obstacle import Obstacle
import time

# Constants
OBSTACLE_SPEED = 0.1
GRAVITY = 0.1
FLAP_STRENGTH = 15
OBSTACLES = []

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Flappy Byrd")
screen.tracer(0)

# Initialize player scoreboard and obstacles - Game assets
player = Player()
scoreboard = ScoreBoard()
obstacles = []

# Respond to clicks
screen.listen()
screen.onkey(player.flap, "Up")

# Game State
game_is_on = True

# Game start time
start = time.time()


# Calculate gameplay duration
def get_time_played(end_time):
    runtime = end_time - start
    runtime = round(runtime)
    print(str(runtime))
    return runtime


# Generate multiple obstacles
def generate_obstacles():
    for x in range(400, 1240, 120):
        new_obstacle = Obstacle(x_cord=x)
        obstacles.append(new_obstacle)


generate_obstacles()
print(f"{len(obstacles)} Obstacles")

# Game Loop
while game_is_on:
    screen.update()
    player.fall(play_speed=GRAVITY)

    # Move all obstacles
    for obstacle in obstacles:
        obstacle.move(play_speed=OBSTACLE_SPEED)

    # Detect floor crash
    if player.ycor() > 275 or player.ycor() < -275:
        print("CRASH DETECTED")
        ending_time = time.time()
        game_is_on = False
        scoreboard.add_point(score=get_time_played(ending_time))
        scoreboard.update_scoreboard()

    # Detect obstacle crash
    # if player.distance(obstacle.upper_obstacle) < 100 or player.distance(obstacle.lower_obstacle) < 100:
    #     print("HIT!")
    #     game_is_on = False


screen.exitonclick()
