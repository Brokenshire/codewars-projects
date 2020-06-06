# Python solution for 'Sort Numbers' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 06/06/2020

import unittest


def sort_numbers(nums):
    """
    Sorts an array of numbers.
    :param nums: array of integers.
    :return: sorted array.
    """
    if nums:
        return sorted(nums)
    return []


class TestSortNumbers(unittest.TestCase):
    """Class to test 'sort_numbers' function"""

    def test_sort_numbers(self):
        self.assertEquals(sort_numbers([1, 2, 10, 5]), [1, 2, 5, 10])


if __name__ == '__main__':
    unittest.main()
