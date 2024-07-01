# etch-a-sketch

from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.fd(10)
def move_backward():
    t.bk(10)
def turn_left():
    t.left(10)
def turn_right():
    t.right(10)
def reset():
    screen.resetscreen()
    t.showturtle()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=reset)

screen.exitonclick()