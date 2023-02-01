import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int(m) + 1
    for x in range(3,m,2):
        if n%x==0:
            return False
    return True

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

for x in range(number1, number2):
    if(is_prime(x)):
        print(x," is a prime number")
    else:
        print(x," is not a prime number")
