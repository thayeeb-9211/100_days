import colorgram
import turtle as t
from turtle import Turtle, Screen
from random import choice

pen = t.Turtle() 
screen = Screen()
screen.colormode(255)

# Extraction of colors from an image
extracted_colors = colorgram.extract('100 Days Python Bootcamp/DAY_18/sunflowers.jpeg', 30)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in extracted_colors]

# Method to draw square with dots 
# space --> distance between dots 
# x     --> side of square 
def draw(space, x):

    # Calculate starting position to center the grid
    # The turtle starts at the bottom-left corner of the grid
    grid_size = (x - 1) * space  # (number of spaces) * space size
    start_x = -grid_size / 2
    start_y = -grid_size / 2

    pen.goto(start_x, start_y)

    pen.speed("fastest") 
    for i in range(x): 
        for j in range(x): 
            # dot 
            pen.dot(20, choice(colors)) 
            # distance for another dot 
            pen.forward(space) 
        pen.backward(space * x) 
        # direction 
        pen.left(90) 
        pen.forward(space) 
        pen.right(90) 
  
# Main Section 
pen.penup()



draw(50, 10)

# Hide the turtle 
pen.hideturtle()
screen.exitonclick()
