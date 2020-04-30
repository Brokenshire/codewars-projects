# Python solution for 'Memoized Fibonacci' codewars question.
# Level: 5 kyu
# Tags: REFACTORING, MEMOIZATION, DESIGN PATTERNS, and DESIGN PRINCIPLES.
# Author: Jack Brokenshire
# Date: 30/04/2020

import unittest
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Memoixation solution to fibonacci.
    :param n: an integer value.
    :return: the fibonacci number.
    """
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


class TestFibonacci(unittest.TestCase):
    """Class to test 'fibonacci' function"""

    def test_fibonacci(self):
        self.assertEqual(fibonacci(70), 190392490709135)
        self.assertEqual(fibonacci(60), 1548008755920)
        self.assertEqual(fibonacci(50), 12586269025)


if __name__ == '__main__':
    unittest.main()
