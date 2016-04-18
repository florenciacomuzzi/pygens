import unittest

from fibonacci import fib_gen

class FibTestCase(unittest.TestCase):
    def test_gen(self):
        fib = fib_gen()
        expected = [1, 1, 2, 3, 5, 8, 13]
        for value in expected:
            self.assertEqual(next(fib),value)
