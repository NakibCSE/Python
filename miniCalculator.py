terminate = False
while not terminate:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    while True:
        operation = input("Enter add/sub/mul/div to perform the operation or quit to exit: ")
        if operation == "quit":
            terminate = True
            break
        if operation not in ["add", "sub", "mul", "div"]:
            print("Please enter a valid operation: ")
            continue
        if operation == 'add':
            print("The summation is = ", number1+number2)
            break
        if operation == 'sub':
            print("The subtraction is = ",number1 - number2)
            break
        if operation == 'mul':
            print("The multiplication is = ", number1*number2)
            break
        if operation == 'div':
            print("The division is ",number1/number2)
            break

        