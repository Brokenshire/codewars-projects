# Python solution for 'Find all non-consecutive numbers' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS AND ARRAYS.
# Author: Jack Brokenshire
# Date: 05/08/2020

import unittest


def all_non_consecutive(arr):
    """
    Find all the elements of an array that are non consecutive. A number is non consecutive if it is not exactly one
    larger than the previous element in the array. The first element gets a pass and is never considered non consecutive.
    :param arr: An array of integers.
    :return: The results as an array of objects with two values i: <the index of the non-consecutive number> and n:
             <the non-consecutive number>.
    """
    return [{'i': i + 1, 'n': arr[i + 1]} for i in range(len(arr) - 1) if arr[i] + 1 != arr[i + 1]]


class TestAllNonConsecutive(unittest.TestCase):
    """Class to test 'all_non_consecutive' function"""

    def test_all_non_consecutive(self):
        self.assertEqual(all_non_consecutive([1, 2, 3, 4, 6, 7, 8, 10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])


if __name__ == "__main__":
    unittest.main()
