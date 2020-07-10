def fib_mem(n):
    cache= [-1] * (n+1)
    cache[0] = 0
    cache[1] = 1
    return fibonacci_mem(n, cache)

def fibonacci_mem(n, cache):
    if cache[n] != -1:
        return cache[n]
    cache[n] = fibonacci_mem(n-1, cache) + fibonacci_mem(n-2, cache)
    return cache[n]

print(fib_mem(10))