import time

from fibonacci import fib_gen, fib_func

ITERATIONS = 200000


start = time.time()
fib = fib_gen()
results = [next(fib) for i in range(ITERATIONS)]
end = time.time()
print('Total time for generator: {} seconds'.format(end - start))



start = time.time()
results = fib_func(ITERATIONS)
end = time.time()
print('Total time for function: {} seconds'.format(end - start))

