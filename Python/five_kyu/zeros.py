# Python solution for 'Number of trailing zeros of N!' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS, MATHEMATICS, and NUMBERS,
# Author: Jack Brokenshire
# Date: 26/06/2020

import unittest


def zeros(n):
    """
    Calculates the number of trailing zeros in a factorial of a given number.
    :param n: an integer value.
    :return: number of zeros trailing factorial number.
    """
    count = 0
    i = 5
    while n / i > 0:
        count += n // i
        i *= 5
    return count


class TestZeros(unittest.TestCase):
    """Class to test 'zeros' function"""

    def test_zeros(self):
        self.assertEqual(zeros(0), 0, "Testing with n = 0")
        self.assertEqual(zeros(6), 1, "Testing with n = 6")
        self.assertEqual(zeros(30), 7, "Testing with n = 30")


if __name__ == '__main__':
    unittest.main()
