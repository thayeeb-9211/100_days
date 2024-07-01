import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)

tim = Turtle()
tim.shape('turtle')
tim.color('coral')
screen = Screen()

# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)
#
#
# for _ in range(8):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()
#
#
# colors = ['red', 'black', 'coral', 'green', 'cyan', 'brown']
#
# for sides in range (3,13):
#     tim.pencolor(choice(colors))
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.fd(50)
#         tim.right(angle)
#
#
def pick_color():

    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

# tim.pensize(10)
# tim.speed('fastest')
# directions = [0, 90, 180, 270]
# for _ in range(100):
#     tim.pencolor(pick_color())
#     tim.fd(30)
#     direction = choice(directions)
#     tim.setheading(direction)

tilt = 3
tim.speed('fastest')
for _ in range(360 // tilt):
    tim.pencolor(pick_color())
    tim.circle(100)
    tim.left(tilt)

screen.exitonclick()