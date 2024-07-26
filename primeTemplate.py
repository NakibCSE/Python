import math

def isPrime (n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.sqrt(n) + 1
    for x in range(3, m, 2):
        if n %  x == 0:
            return False
    return True
    