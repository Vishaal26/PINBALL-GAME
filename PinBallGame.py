import turtle
from random import randint

#SCREEN>>>>>
screen = turtle.Screen()
screen.title("Pinball game")
screen.bgcolor("light blue")
screen.setup(width=1000, height=600)

#PADDLE>>>>>
paddle = turtle.Turtle()
paddle.speed(100)
paddle.shape("square")
paddle.color("gold")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(-30, -270)

#BALL>>>
ball = turtle.Turtle()
ball.speed(1000)
ball.shape("circle")
ball.color("green")
ball.penup()
x = randint(-400, 400)
ball.goto(x, 260)
ball.dx = 2
ball.dy = -2

#SCORE>>>>
score = 0
score_board = turtle.Turtle()
score_board.speed(0)
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("SCORE : 0", align="center", font=("times", 20, "bold"))


def right():
    x = paddle.xcor()
    x = x + 15
    paddle.setx(x)


def left():
    x = paddle.xcor()
    x = x - 15
    paddle.setx(x)


screen.listen()
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")

while True:
    screen.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.xcor() > 480:
        ball.setx(480)
        ball.dx = ball.dx * -1

    if ball.xcor() < -480:
        ball.setx(-480)
        ball.dx = ball.dx * -1

    if ball.ycor() > 280:
        ball.setx(280)
        ball.dy = ball.dy * -1

    if ball.ycor() < -260:
        score_board.clear()
        score_board_1 = turtle.Turtle()
        score_board_1.speed(0)
        score_board_1.penup()
        score_board_1.hideturtle()
        score_board_1.goto(0, 0)
        score_board_1.color("black")
        score_board_1.write("Score : {} ". format(score), align="center", font=("times", 30, "bold"))
        break

    if(paddle.ycor() + 30 > ball.ycor() > paddle.ycor() - 30) and (paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50):
        score += 1
        score_board.clear()
        score_board.write("SCORE: {}".format(score), align="center", font=("times", 20, "bold"))

        if(ball.dy > 0) and (ball.dy < 5):
            ball.dy += 0.5
        elif (ball.dx > 0) and (ball.dx < 5):
            ball.dy = ball.dy - 0.5

        if(ball.dx > 0) and (ball.dx < 5):
            ball.dx = ball.dx + 0.5
        elif(ball.dx < 0) and (ball.dx > -5):
            ball.dx = ball.dx - 0.5

        ball.dy = ball.dy * -1

while True:
    screen.update()
