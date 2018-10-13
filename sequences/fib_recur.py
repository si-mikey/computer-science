def fib_recur(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fib_recur(n - 1) + fib_recur(n - 2)

f = fib_recur(10)
print(f)
