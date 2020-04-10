# Python solution for 'You're a square!' codewars question.
# Level: 7 kyu
# Tags: Fundamentals.
# Author: Jack Brokenshire
# Date: 04/03/2020

import unittest
import math


def is_square(n):
    """
    Given an integral number, determine if it's a square number: In mathematics, a square number or perfect square is
    an integer that is the square of an integer; in other words, it is the product of some integer with itself. The
    tests will always use some integral number, so don't worry about that in dynamic typed languages.
    :param n: an integral integer number.
    :return: True if the integer is a square number.
    """
    if n < 0: return False
    return n == int(math.sqrt(n) + 0.5) ** 2


class TestIsSquare(unittest.TestCase):
    """Class to test 'is_square' function"""

    def test_is_square(self):
        self.assertEqual(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
        self.assertEqual(is_square(0), True, "0 is a square number")
        self.assertEqual(is_square(3), False, "3 is not a square number")
        self.assertEqual(is_square(4), True, "4 is a square number")
        self.assertEqual(is_square(25), True, "25 is a square number")
        self.assertEqual(is_square(26), False, "26 is not a square number")


if __name__ == '__main__':
    unittest.main()
