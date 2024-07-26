
def find_fib(n):
    if n < 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i+=1
        fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next

def lsit_fibo(n):
    li_fib = []
    fib_x = 1
    fib_next = 1
    li_fib.append(fib_x)
    li_fib.append(fib_next)
    for i in range(n-2):
        fib_x, fib_next = fib_next, fib_x + fib_next
        li_fib.append(fib_next)
    return li_fib

if __name__ == "__main__":
    for x in range(1,11):
        print(find_fib(x))
    print(lsit_fibo(1))
    print(lsit_fibo(2))
    print(lsit_fibo(10))