# Python solution for 'Difference of 2' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS,ARRAYS, SORTING, LOOPS, CONTROL FLOW, BASIC LANGUAGE FEATURES, FUNDAMENTALS, and UTILITIES.
# Author: Jack Brokenshire
# Date: 07/05/2020

import unittest


def twos_difference(lst):
    """
    Given an array of integers returns a list of tuples in ascending order with integers 2 numbers apart.
    :param lst: an array of integer values.
    :return: all pairs of integers from a given array of integers that have a difference of 2.
    """
    return sorted((i, j) for i in lst for j in lst if j - i == 2)


class TestTwosDifference(unittest.TestCase):
    """Class to test 'twos_difference' function"""

    def test_twos_difference(self):
        self.assertEqual(twos_difference([1, 2, 3, 4]), [(1, 3), (2, 4)])
        self.assertEqual(twos_difference([1, 3, 4, 6]), [(1, 3), (4, 6)])
        self.assertEqual(twos_difference([0, 3, 1, 4]), [(1, 3)])
        self.assertEqual(twos_difference([4, 1, 2, 3]), [(1, 3), (2, 4)])
        self.assertEqual(twos_difference([6, 3, 4, 1, 5]), [(1, 3), (3, 5), (4, 6)])
        self.assertEqual(twos_difference([3, 1, 6, 4]), [(1, 3), (4, 6)])
        self.assertEqual(twos_difference([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]), [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)])
        self.assertEqual(twos_difference([1, 4, 7, 10]), [])
        self.assertEqual(twos_difference([]), [])


if __name__ == '__main__':
    unittest.main()
