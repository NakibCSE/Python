import turtle

turtle.color("red","green")
turtle.begin_fill()
while True:
    turtle.forward(300)
    turtle.left(170)
    if abs(turtle.position())<1:
        break
turtle.end_fill()
turtle.done()