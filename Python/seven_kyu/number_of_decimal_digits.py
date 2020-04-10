# Python solution for 'Number of Decimal Digits' codewars question.
# Level: 7 kyu
# Tags: Fundamentals. Numbers, Integers, Strings, Loops, Control Flow, and Basic Language Features.
# Author: Jack Brokenshire
# Date: 28/03/2020

import unittest


def number_of_decimal_digits(n):
    """
    Determine the total number of digits in the integer (n>=0) given as input to the function. For example, 9 is a
    single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.
    :param n: a integer input.
    :return: the number of digits in the integer.
    """
    return len(str(n))


class TestNumberOfDecimalDigits(unittest.TestCase):
    """Class to test 'number_of_decimal_digits' function"""

    def test_number_of_decimal_digits(self):
        self.assertEqual(number_of_decimal_digits(5), 1)
        self.assertEqual(number_of_decimal_digits(12345), 5)
        self.assertEqual(number_of_decimal_digits(9876543210), 10)


if __name__ == '__main__':
    unittest.main()
