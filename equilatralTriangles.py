import turtle
turtle.speed(2)
def equilatralTriangle(legthOfSide):
    for i in range(3):
        turtle.forward(legthOfSide)
        turtle.left(120)

equilatralTriangle(400)


turtle.exitonclick()