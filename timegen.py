import time

from fibonacci import fib_gen, fib_func

start = time.time()
fib = fib_gen()
[next(fib) for i in range(1000)]
end = time.time()
print('Total time for generator: {} seconds'.format(end - start))



start = time.time()
fib_func(1000)
[next(fib) for i in range(1000)]
end = time.time()
print('Total time for function: {} seconds'.format(end - start))

