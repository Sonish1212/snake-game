from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_snake = Snake()
food = Food()
screen = Screen()
score_board = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()
screen.onkey(game_snake.move_forward, "Up")
screen.onkey(game_snake.move_backward, "Down")
screen.onkey(game_snake.move_left, "Left")
screen.onkey(game_snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    game_snake.move()

    # Detect the Snake Food
    if game_snake.head.distance(food) < 15:
        food.refresh()
        game_snake.extend()
        score_board.increase_score()

    if game_snake.head.xcor() > 280 or game_snake.head.xcor() < -280 or game_snake.head.ycor() > 280 or game_snake.head.ycor() < -280:
        game_snake.reset_snake()
        score_board.reset()

    # Detect the collision with snake tail
    for segment in game_snake.segment[1:]:
        if game_snake.head.distance(segment) < 10:
            game_snake.reset_snake()
            score_board.reset()


screen.exitonclick()
