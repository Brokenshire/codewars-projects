# Python solution for 'Find the first non-consecutive number' codewars question.
# Level: 8 kyu
# Tags: Fundamentals and Arrays.
# Author: Jack Brokenshire
# Date: 27/02/2020

import unittest


def first_non_consecutive(arr):
    """
    Finds the first element within an array that is not consecutive.
    :param arr: An array of ints.
    :return: the first element not consecutive, otherwise None.
    """
    for i, j in enumerate(arr):
        if j != arr[0] + i:
            return j
    return None


class TestFirstNonConsecutive(unittest.TestCase):
    """Class to test 'first_non_consecutive' function"""

    def test_first_non_consecutive(self):
        self.assertEqual(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]), 6)
        self.assertEqual(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]), None)
        self.assertEqual(first_non_consecutive([4, 6, 7, 8, 9, 11]), 6)
        self.assertEqual(first_non_consecutive([4, 5, 6, 7, 8, 9, 11]), 11)
        self.assertEqual(first_non_consecutive([31, 32]), None)
        self.assertEqual(first_non_consecutive([-3, -2, 0, 1]), 0)
        self.assertEqual(first_non_consecutive([-5, -4, -3, -1]), -1)


if __name__ == '__main__':
    unittest.main()
