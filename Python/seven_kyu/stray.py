# Python solution for "Find the stray number" codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, NUMBERS, and ALGORITHMS.
# Author: Jack Brokenshire
# Date: 10/04/2020

import unittest


def stray(arr):
    """
    You are given an odd-length array of integers, in which all of them are the same, except for one single number.
    :param arr: an array of integers.
    :return: the single different number in the array.
    """
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


class TestStray(unittest.TestCase):
    """Class to test "stray" function"""

    def test_stray(self):
        self.assertEqual(stray([1, 1, 1, 1, 1, 1, 2]), 2)
        self.assertEqual(stray([2, 3, 2, 2, 2]), 3)
        self.assertEqual(stray([3, 2, 2, 2, 2]), 3)


if __name__ == "__main__":
    unittest.main()
