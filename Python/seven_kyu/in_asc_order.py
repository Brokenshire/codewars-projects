# Python solution for "Are the numbers in order?" codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS, FUNDAMENTALS, MATHEMATICS, NUMBERS, CONTROL FLOW, BASIC LANGUAGE FEATURES, and OPTIMIZATION.
# Author: Jack Brokenshire
# Date: 06/04/2020

import unittest


def in_asc_order(arr):
    """
    Determines if the given array is in ascending order or not.
    :param arr: an integer array.
    :return: True if array is in ascending order otherwise, False.
    """
    return arr == sorted(arr)


class TestInAscOrder(unittest.TestCase):
    """Class to test "in_asc_order" function"""

    def test_in_asc_order(self):
        self.assertEqual(in_asc_order([1, 2]), True)
        self.assertEqual(in_asc_order([2, 1]), False)
        self.assertEqual(in_asc_order([1, 2, 3]), True)
        self.assertEqual(in_asc_order([1, 3, 2]), False)
        self.assertEqual(in_asc_order([1, 4, 13, 97, 508, 1047, 20058]), True)
        self.assertEqual(in_asc_order([56, 98, 123, 67, 742, 1024, 32, 90969]), False)


if __name__ == "__main__":
    unittest.main()
