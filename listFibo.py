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
print(lsit_fibo(10))



