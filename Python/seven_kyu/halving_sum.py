# Python solution for 'Halving Sum' codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS
# Author: Jack Brokenshire
# Date: 12/06/2020

import unittest


def halving_sum(n):
    """
    Halving the sum of integer.
    :param n: a positive integer.
    :return: all elements of the sum are the results of integer division.
    """
    if n == 1:
        return 1
    else:
        return n + halving_sum(n // 2)


class TestHalvingSum(unittest.TestCase):
    """Class to test 'halving_sum' function"""

    def test_halving_sum(self):
        self.assertEquals(halving_sum(25), 47)
        self.assertEquals(halving_sum(127), 247)


if __name__ == '__main__':
    unittest.main()
