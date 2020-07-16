# Python solution for 'max diff - easy' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, NUMBERS, COLLECTIONS, LISTS, DATA STRUCTURES, AND ARRAYS.
# Author: Jack Brokenshire
# Date: 16/07/2020

import unittest


def max_diff(lst):
    """
    Finds the difference beteween the largest and smallest items in a list.
    :param lst: a list of integers.
    :return: the difference between the biggest and the smallest value in a list received as parameter, otherwise, 0.
    """
    if lst:
        return max(lst) - min(lst)
    return 0


class TestMaxDiff(unittest.TestCase):
    """Class to test 'max_diff' function"""

    def test_max_diff(self):
        self.asserEqual(max_diff([0, 1, 2, 3, 4, 5, 6]), 6)
        self.asserEqual(max_diff([-0, 1, 2, -3, 4, 5, -6]), 11)
        self.asserEqual(max_diff([0, 1, 2, 3, 4, 5, 16]), 16)
        self.asserEqual(max_diff([16]), 0)
        self.asserEqual(max_diff([]), 0)


if __name__ == '__main__':
    unittest.main()
