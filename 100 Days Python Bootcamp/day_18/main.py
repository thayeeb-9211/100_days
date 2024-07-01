from turtle import Turtle, Screen
import colorgram
from random import choice

screen = Screen()

extracted_colors = colorgram.extract('sunflowers.jpeg',12)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in extracted_colors]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
screen.colormode(255)
t = Turtle()
t.hideturtle()
t.penup()
for y in range(-250,201,50):
    t.setpos(-250,y)
    for _ in range(10):
        t.pendown()
        t.dot(20,choice(colors))
        t.penup()
        t.fd(50)



screen.exitonclick()