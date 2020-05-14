# Python solution for 'Is n divisible by x and y?' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 14/05/2020

import unittest


def is_divisible(n, x, y):
    """
    checks if a number n is divisible by two numbers x AND y.
    :param n: positive, non negative integer.
    :param x: positive, non negative integer.
    :param y: positive, non negative integer.
    :return: if n is divisible by x and y.
    """
    return n % x == 0 and n % y == 0


class TestIsDivisible(unittest.TestCase):
    """Class to test 'is_divisible' function"""

    def test_is_divisible(self):
        self.assertEqual(is_divisible(3, 3, 4), False)
        self.assertEqual(is_divisible(12, 3, 4), True)
        self.assertEqual(is_divisible(8, 3, 4), False)
        self.assertEqual(is_divisible(48, 3, 4), True)


if __name__ == '__main__':
    unittest.main()
