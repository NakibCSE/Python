import math

def isPrime(n = 1013):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(math.sqrt(n) + 1)
    for x in range(3, m, 2):
        if n %  x == 0:
            return False
    return True


def isPrime3(n = 1013):
    if n == 2:
        return True #2 is prime
    if n % 2 == 0:
        print(n," is divisible 2")
        return False   # All even number except 2 are not prime
    if n < 2:
        return False   #Numbers less than 2 are not prime number\
    prime = True
    for x in range(3, n, 2):
        if n % x == 0:
            print(n, " is divisible by", x)
            prime = False
            return prime
    return prime


import timeit
t1 = timeit.timeit(isPrime3) 
t2 = timeit.timeit(isPrime)

print(t1, t2, t1/t2) 