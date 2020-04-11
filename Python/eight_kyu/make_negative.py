# Python solution for 'Return Negative' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS and NUMBERS.
# Author: Jack Brokenshire
# Date: 11/04/2020

import unittest


def make_negative(number):
    """
    Make a given number negative.
    :param number: an integer value.
    :return: the integer as a negative number.
    """
    return -abs(number)


class TestMakeNegative(unittest.TestCase):
    """Class to test make_negative function"""

    def test_make_negative(self):
        self.assertEqual(make_negative(42), -42)
        self.assertEqual(make_negative(1), -1)
        self.assertEqual(make_negative(-5), -5)
        self.assertEqual(make_negative(0), 0)


if __name__ == '__main__':
    unittest.main()
