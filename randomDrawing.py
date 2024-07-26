import turtle
import random

#list of colours
colours = ["red", "green", "blue", "yellow", "orange", "black", "purple"]
turtle.penup()
for i in range(1000):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)

    #set a random position
    turtle.setposition(x, y)

    #Set a random color
    i = random.randint(0, len(colours) - 1)
    turtle.dot(colours[i])
turtle.done()