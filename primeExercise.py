import math 

def isPrime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    prime = True
    m = int(math.sqrt(n) + 1)
    for i in range(3, m, 2):
        if n % i == 0:
            prime = False
            return prime
    return prime


n1 = 1
n2 = 100

for i in range(n1, n2):
    if isPrime(i) == True:
        print(i)


