def isPrime3(n):
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

