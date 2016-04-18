def fib_gen():
    a, b = 1, 1
    while True:
        yield a 
        a, b = b, a + b

def fib_func(n):
    values = []
    a, b = 1, 1
    for _ in range(n):
        values.append(a)
        a, b = b, a + b
    return values
