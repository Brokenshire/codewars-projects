# Python solution for 'Breaking chocolate problem' codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS and NUMBERS.
# Author: Jack Brokenshire
# Date: 17/06/2020

import unittest


def break_chocolate(n, m):
    """
    Split the chocolate bar of given dimension n x m into small squares.
    :param n: integer value.
    :param m: integer value.
    :return: number of splits for n x m square.
    """
    return n * m - 1 if n * m > 0 else 0


class TestBinaryArrayToNumber(unittest.TestCase):
    """Class to test 'break_chocolate' function"""

    def test_break_chocolate(self):
        self.assertEqual(break_chocolate(5, 5), 24)
        self.assertEqual(break_chocolate(1, 1), 0)


if __name__ == '__main__':
    unittest.main()
