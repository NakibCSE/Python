import turtle

name = turtle.textinput("name", "What is your name?")
name = name.lower()
if name.startswith('mr'):
    print("Hello sir, how are you?")
elif name.startswith('mrs') or name.startswith('miss') or name.startswith('mis'):
    print("Hello madam, how are you??")
else:
    name = name.capitalize()
    str = "Hi "+name+"! How are you?"
    print(str)
turtle.exitonclick()