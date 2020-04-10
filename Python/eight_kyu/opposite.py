# Python solution for 'Opposite number' codewars question.
# Level: 8 kyu
# Tags: Fundamentals.
# Author: Jack Brokenshire
# Date: 21/02/2020

import unittest


def opposite(number):
    """
    Very simple, given a number, find its opposite.
    :param number: An negative OR positive integer.
    :return: The opposite of the given integer.
    """
    return number * -1


class TestOpposite(unittest.TestCase):
    """Class to test 'opposite' function"""

    def test_opposite(self):
        self.assertEqual(opposite(1), -1)


if __name__ == '__main__':
    unittest.main()
