# Python solution for 'The highest profit wins!' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, LISTS, DATA STRUCTURES, and ARRAYS.
# Author: Jack Brokenshire
# Date: 23/04/2020

import unittest
from random import randint


def min_max(lst):
    """
    Function that returns both the minimum and maximum number of the given list/array.
    :param lst: an array of integers.
    :return: returns a list with the smallest then largest numbers in the array.
    """
    return [min(lst), max(lst)]


class TestMinMax(unittest.TestCase):
    """Class to test 'min_max' function"""

    def test_min_max(self):
        self.assertEqual([1, 2, 3, 4, 5], [1, 5])
        self.assertEqual([2334454, 5], [5, 2334454])

        for i in range(0, 20):
            r = randint(0, 100)
            self.assertEqual([r], [r, r])


if __name__ == '__main__':
    unittest.main()
