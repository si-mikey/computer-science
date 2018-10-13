def fib_recur(n):
    if n < 2:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)

for n in range(0, 15):
    print(fib_recur(n))

