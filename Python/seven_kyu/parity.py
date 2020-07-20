# Python solution for 'Array element parity' codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS and ARRAYS
# Author: Jack Brokenshire
# Date: 20/07/2020

import unittest


def solve(arr):
    """
    Array of integers whose elements have both a negative and a positive value, except for one integer that is either
    only negative or only positive.
    :param arr: array of positive and negative integers.
    :return: find integer that only has a negative and not a positive or other way around.
    """
    return next(x for x in arr if abs(x) not in arr or -x not in arr)


class TestSolve(unittest.TestCase):
    """Class to test 'solve' function"""

    def test_solve(self):
        self.assertEqual(solve([1, -1, 2, -2, 3]), 3)
        self.assertEqual(solve([-3, 1, 2, 3, -1, -4, -2]), -4)
        self.assertEqual(solve([1, -1, 2, -2, 3, 3]), 3)
        self.assertEqual(solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]), -38)
        self.assertEqual(solve([-9, -105, -9, -9, -9, -9, 105]), -9)


if __name__ == '__main__':
    unittest.main()
