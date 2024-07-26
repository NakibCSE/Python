import turtle
name = turtle.textinput("name", "What is your name?: ")
name = name.lower()
if name.startswith("mr"):
    print("Hello Sir, How are you?")
elif name.startswith("mrs"):
    print("Hello Madam, How are you?")
else:
    name = name.capitalize()
    str = "Hi "+name+"! How are you?"
    print(str)

turtle.exitonclick()  