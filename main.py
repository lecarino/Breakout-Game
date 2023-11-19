from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from blocks import Blocks
from scoreboard import Scoreboard
#Need blocks, Scoreboard, title screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Breakout")
screen.tracer(0)

#Paddle
paddle = Paddle((0, -250))
screen.listen()
screen.onkey(fun= paddle.left, key= "Left")
screen.onkey(fun= paddle.right, key= "Right")

#Ball
ball = Ball((0,-180))

#Blocks
blocks = Blocks()
blocks.create_blocks()

#Scoreboard 
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #BOUNDARIES OF GAME:
    if ball.ycor() >= 280:
        ball.bounce_y()
    if ball.xcor()>=380 or ball.xcor()<=-380:
        ball.bounce_x()

    #COLLISION WITH PADDLE:
    if ball.distance(paddle) < 40 and ball.ycor() > -233:
        ball.bounce_y()

    # COLLISION WITH BLOCKS:
    for block in blocks.blocks:
        if ball.distance(block) < 40:  # Adjust the distance as needed
            ball.bounce_y()
            blocks.remove_block(block)
            scoreboard.l_point()
    
    if ball.ycor() < -300 or len(blocks.blocks) == 0:
        scoreboard.game_over()
        game_is_on = False



screen.exitonclick()