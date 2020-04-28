# Python solution for 'Find the smallest integer in the array' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 28/04/2020

import unittest


def find_smallest_int(arr):
    """
    Given an array of integers find the smallest number.
    :param arr: an array of integers.
    :return: the smallest number within the array.
    """
    return min(arr)


class TestFindSmallestInt(unittest.TestCase):
    """Class to test 'find_smallest_int' function"""

    def test_find_smallest_int(self):
        self.assertEqual(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
        self.assertEqual(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
        self.assertEqual(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)


if __name__ == '__main__':
    unittest.main()
