# Python solution for 'Sort the odd' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS AND ARRAYS.
# Author: Jack Brokenshire
# Date: 17/07/2020

import unittest


def sort_array(source_array):
    """
    Sort ascending odd numbers but even numbers must be on their places.
    :param source_array: an array of integers.
    :return: an odd sorted array where even numbers remain in place.
    """
    odds = iter(sorted(x for x in source_array if x % 2))
    return [next(odds) if x % 2 else x for x in source_array]


class TestSortArray(unittest.TestCase):
    """Class to test 'sort_array' function"""

    def test_sort_array(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        self.assertEqual(sort_array([]), [])


if __name__ == '__main__':
    unittest.main()
