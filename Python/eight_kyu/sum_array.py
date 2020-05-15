# Python solution for 'Sum Arrays' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, LOOPS, CONTROL FLOW, BASIC LANGUAGE FEATURES, and ARRAYS.
# Author: Jack Brokenshire
# Date: 15/05/2020

import unittest


def sum_array(a):
    """
    Returns the sum of the numbers.
    :param a: an array of integers.
    :return: the sum of the array.
    """
    return sum(a)


class TestSumArray(unittest.TestCase):
    """Class to test 'sum_array' function"""

    def test_sum_array(self):
        self.assertEqual(sum_array([]), 0)
        self.assertEqual(sum_array([1, 2, 3]), 6)
        self.assertEqual(sum_array([1.1, 2.2, 3.3]), 6.6)
        self.assertEqual(sum_array([4, 5, 6]), 15)
        self.assertEqual(sum_array(range(101)), 5050)


if __name__ == '__main__':
    unittest.main()
