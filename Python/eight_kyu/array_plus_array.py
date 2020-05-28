# Python solution for 'Array plus array' codewars question.
# Level: 8 kyu
# Tags: BUGS, FUNDAMENTALS, ARRAYS, NUMBERS, and BASIC LANGUAGE FEATURES,
# Author: Jack Brokenshire
# Date: 27/05/2020

import unittest


def array_plus_array(arr1, arr2):
    """
    Finds the sum of two arrays.
    :param arr1: an array of integers.
    :param arr2: an array of integers.
    :return: the sum of the elements of both arrays.
    """
    return sum(arr1) + sum(arr2)


class TestArrayPlusArray(unittest.TestCase):
    """Class to test 'array_plus_array' function"""

    def test_array_plus_array(self):
        self.assertEquals(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
        self.assertEquals(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
        self.assertEquals(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
        self.assertEquals(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)


if __name__ == '__main__':
    unittest.main()
