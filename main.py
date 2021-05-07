from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from obstacle import Obstacle
import math
import time

# Constants
OBSTACLE_SPEED = 0.1
GRAVITY = 0.05
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


def get_collision_distance(height, obs: Obstacle):
    u_dist = player.distance(obs.upper_obstacle)
    l_dist = player.distance(obs.lower_obstacle)
    a_squared = (height / 2) ** 2
    b_squared = 10 ** 2
    c_squared = math.sqrt(a_squared + b_squared)
    print(f"Obstacle height: ${height} \nColl_dist: {c_squared}")
    print(f"Upper Dist: ${u_dist} \nLower Dist: {l_dist}")

    # Increase the size of the zone sensitive to collision with the player
    return c_squared * 2.5


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

    # Detect obstacle collision
    for obstacle in obstacles:
        top_height = obstacle.top_height
        bottom_height = obstacle.bottom_height
        if 40 > obstacle.upper_obstacle.xcor() > -40:
            if player.distance(obstacle.upper_obstacle) \
                    < get_collision_distance(height=top_height, obs=obstacle) or \
                    player.distance(obstacle.lower_obstacle) \
                    < get_collision_distance(height=bottom_height, obs=obstacle):
                print("HIT!")
                game_is_on = False


screen.exitonclick()
