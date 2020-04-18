# Python solution for 'Maximum subarray sum' codewars question.
# Level: 5 kyu
# Tags: FUNDAMENTALS, ALGORITHMS, LISTS, DATA STRUCTURES, and DYNAMIC PROGRAMMING.
# Author: Jack Brokenshire
# Date: 17/04/2020

import unittest


def max_sequence(arr):
    """
    The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or
    list of integers.
    :param arr: an array or list of integers.
    :return: the maximum value found within the subarray.
    """
    best = 0
    for x in range(len(arr)):
        for y in range(len(arr)):
            if sum(arr[x:y+1]) > best:
                best = sum(arr[x:y+1])
    return best


class TestMaxSequence(unittest.TestCase):
    """Class to test 'max_sequence' function"""

    def test_max_sequence(self):
        self.assertEqual(max_sequence([]), 0)
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == '__main__':
    unittest.main()
