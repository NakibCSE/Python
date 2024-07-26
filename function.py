import turtle

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

counter = 0
while counter < 90:
    if counter <= 10:
        turtle.color("blue")
    elif counter <= 20:
        turtle.color("red")
    elif counter <= 30:
        turtle.color("pink")
    elif counter <= 40:
        turtle.color("black")
    elif counter <= 50:
        turtle.color("green")
    elif counter <= 60:
        turtle.color("yellow")
    elif counter <= 70:
        turtle.color("orange") 
    turtle.speed(0)
    draw_square(100)
    turtle.right(4)
    counter += 1

turtle.exitonclick()