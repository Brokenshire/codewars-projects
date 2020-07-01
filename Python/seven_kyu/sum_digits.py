# Python solution for 'Summing a number's digits' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, ARITHMETIC, MATHEMATICS, ALGORITHMS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 01/07/2020

import unittest


def sum_digits(number):
    """
    Takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.
    :param number: an integer value.
    :return: sum of the absolute value of each of the number's decimal digits.
    """
    return sum(int(x) for x in str(abs(number)))


class TestSumDigits(unittest.TestCase):
    """Class to test 'sum_digits' function"""

    def test_sum_digits(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(99), 18)
        self.assertEqual(sum_digits(-32), 5)


if __name__ == '__main__':
    unittest.main()
