# Python solution for 'Multiply' codewars question.
# Level: 8 kyu
# Tags: Algorithms, Date/Time, Mathematics, and Numbers
# Author: Jack Brokenshire
# Date: 07/02/2020

import unittest


def multiply(a, b):
    """
    The code does not execute properly. Try to figure out why.
    :param a: a positive integer value
    :param b: a positive integer value
    :return: the result of multiplying the two integers together
    """
    return a * b


class TestMultiply(unittest.TestCase):
    """Class to test 'multiply' function"""

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)


if __name__ == '__main__':
    unittest.main()
