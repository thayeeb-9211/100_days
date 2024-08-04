import turtle as t
from turtle import Turtle, Screen
from random import choice, randint
import random
import math

tim = Turtle()

#simple triangle
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# for _ in range(3):
#   tim.left(120)
#   tim.forward(100)


# Encircling a loop for 100 steps
# for steps in range(100):
#   for c in ('blue', 'red', 'green'):
#     tim.color(c)
#     tim.forward(steps)
#     tim.right(30)

######## Challenge 1 - Draw a Square ############
# def Draws_square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.left(90)
#         tim.forward(100)

########### Challenge 2 - Draw a Dashed Line ########

# def draws_dashed_line():
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
# draws_dashed_line()

########### Challenge 3 - Draw Shapes ########

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.pensize(5)
#         tim.right(angle)
#         tim.speed(0)

# for shape_side_n in range(3, 11):
#     tim.color(choice(colours))
#     draw_shape(shape_side_n)

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def random_walk():

#     directions = [0, 90, 180, 270]
#     tim.pensize(15)
#     tim.speed(0)

#     for _ in range(200):
#         tim.color(random.choice(colours))
#         tim.forward(30)
#         tim.setheading(choice(directions))
# random_walk()



########### Challenge 5 - Spirograph ########

# t.colormode(255)
# tim.speed('fastest')

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# size_of_gap = 3
# def spirograpgh():
#     tim.color(random_color())
#     for _ in range(360 // size_of_gap):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.left(size_of_gap)
# spirograpgh()

screen = Screen()
screen.exitonclick()