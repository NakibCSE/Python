import turtle

turtle.color("green")
turtle.speed(0)

countter = 0
while countter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    countter += 1

turtle.exitonclick()