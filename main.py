from turtle import Screen
from paddle import Paddle
from ball import Ball
from net import Net
from scoreboard import Scoreboard
import time
TIME_SPEED=0.1

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
net = Net()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(TIME_SPEED)
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        TIME_SPEED *= 0.9

    if ball.xcor() > 380:
        ball.goto(0, 0)
        TIME_SPEED = 0.1
        ball.bounce_x()
        scoreboard.keep_l_score()

    if ball.xcor() < -380:
        ball.goto(0,0)
        TIME_SPEED = 0.1
        ball.bounce_x()
        scoreboard.keep_r_score()



screen.exitonclick()

