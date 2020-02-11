# Python solution for 'Convert number to reversed array of digits' codewars question.
# Level: 8 kyu
# Tags: Fundamentals, Numbers, and Arrays
# Author: Jack Brokenshire
# Date: 11/02/2020

import unittest


def digitize(n):
    """
    You have to return the digits of this number within an array in reverse order.
    :param n: an input integer.
    :return: the input integer in the form of an array in reverse order.
    """
    return list(map(int, str(n)[::-1]))


class TestDigitize(unittest.TestCase):
    """Class to test 'digitize' function"""

    def test_digitize(self):
        self.assertEqual(digitize(35231), [1, 3, 2, 5, 3])


if __name__ == '__main__':
    unittest.main()
