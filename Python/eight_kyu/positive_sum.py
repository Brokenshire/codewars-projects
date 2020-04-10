# Python solution for 'Sum of positive' codewars question.
# Level: 8 kyu
# Tags: Fundamentals, Arrays, and Numbers.
# Author: Jack Brokenshire
# Date: 12/02/2020

import unittest


def positive_sum(arr):
    """
    You get an array of numbers, return the sum of all of the positives ones. Note: if there is nothing to sum,
    the sum is default to 0.
    :param arr: An array of integers.
    :return: The sum all positive integers within the given array.
    """
    return sum([x for x in arr if x > 0])


class TestPositiveSum(unittest.TestCase):
    """Class to test 'positive_sum' function"""

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(positive_sum([1, -2, 3, 4, 5]), 13)
        self.assertEqual(positive_sum([-1, 2, 3, 4, -5]), 9)
        self.assertEqual(positive_sum([]), 0)
        self.assertEqual(positive_sum([-1, -2, -3, -4, -5]), 0)


if __name__ == '__main__':
    unittest.main()
