import turtle
def drawTriangel(side_length):
    turtle.shape("turtle")
    turtle.speed(2)
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)


drawTriangel(100)
