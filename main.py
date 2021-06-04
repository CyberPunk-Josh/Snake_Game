from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# creating a snake:
snake = Snake()
# creating food:
food = Food()
# creating score board:
scoreBoard = ScoreBoard()

# direction of the snake (controls):
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')

# moving the snake:
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # collision width food:
    if snake.head.distance(food) < 15:
        scoreBoard.increase_score()
        snake.extend()
        food.refresh()

    # detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreBoard.game_over()

    # detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreBoard.game_over()

screen.exitonclick()
