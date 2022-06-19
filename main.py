import colorgram
from turtle import Turtle, Screen
import random

# Extract all colours from hirst-spot-painting
colours = colorgram.extract('hirst-spot-painting.jpg', 30)


# Generate list of RGB colour tuples
rgb_colours = []
for colour in colours:
	r = colour.rgb.r
	g = colour.rgb.g
	b = colour.rgb.b
	new_colour = (r, g, b)
	rgb_colours.append(new_colour)

# print(rgb_colours)

# Use generated list to create unique spot painting

colour_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (126, 40, 61), (21, 86, 61), (59, 48, 37),
               (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
               (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202),
               (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33),
               (170, 203, 205), (223, 178, 169)]

cursor = Turtle()
cursor.speed("fastest")
cursor.hideturtle()
screen = Screen()
screen.colormode(255)

cursor.penup()
cursor.setposition(-250, -200)
num_dots = 0
while num_dots < 100:
	for dots in range (10):
		cursor.penup()
		cursor.forward(50)
		cursor.dot(20, random.choice(colour_list))
		num_dots += 1
	cursor.left(90)
	cursor.forward(50)
	cursor.right(90)
	cursor.backward(500)

screen.exitonclick()
