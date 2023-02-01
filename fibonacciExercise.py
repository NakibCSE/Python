import turtle

def fibonacci(n):
    fib_x = 1
    fib_next = 1
    if n <= 2:
        fib_n = 1
    else:
        i = 3
        while i <= n:
            i += 1
            fib_next, fib_x = fib_next + fib_x , fib_next
            turtle.circle(fib_x, fib_next)
            
fibonacci(13)
turtle.exitonclick()