while True:
    n = int(input("Enter a number: "))
    if n<0:
        print("We only allow positive integer, Please try again: ")
    if n == 0:
        break
    print("The square of ",n," is ", n*n)