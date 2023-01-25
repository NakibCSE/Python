number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter third number: "))

max_number = number1

if number2>max_number:
    max_number = number2
if number3 > max_number:
    max_number = number3

print("The largest number is = ",max_number)