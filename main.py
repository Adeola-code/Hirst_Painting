# import colorsys
#
# import colorgram
# colors=colorgram.extract("hirst.jpg", 6)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle

color_list=[(245, 245, 245), (115, 160, 192), (134, 46, 112), (242, 243, 246), (103, 34, 79), (200, 121, 179)]

from turtle import Turtle, Screen, colormode
turtle.colormode(255)
tim=Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for dot_count in range(1,36):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count%6==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(300)
        tim.setheading(0)

screen=Screen()
screen.exitonclick()