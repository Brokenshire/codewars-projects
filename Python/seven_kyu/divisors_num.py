# Python solution for 'Count the divisors of a number' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, ARITHMETIC, MATHEMATICS, ALGORITHMS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 02/07/2020

import unittest


def divisors(n):
    """
    Count the number of divisors of a positive integer n.
    :param n: an integer input.
    :return: the number of divisors of an integer.
    """
    return sum(1 for x in range(1, n + 1) if n % x == 0)


class TestDivisors(unittest.TestCase):
    """Class to test 'divisors' function"""

    def test_divisors(self):
        self.assertEqual(divisors(4), 3)
        self.assertEqual(divisors(5), 2)
        self.assertEqual(divisors(12), 6)
        self.assertEqual(divisors(30), 8)
        self.assertEqual(divisors(4096), 13)


if __name__ == '__main__':
    unittest.main()
