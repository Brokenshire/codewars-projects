# Python solution for 'Find the unique number' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Algorithms, Numbers, and Arrays.
# Author: Jack Brokenshire
# Date: 05/02/2020

import unittest


def find_uniq(arr):
    """
    There is an array with some numbers. All numbers are equal except for one. Try to find it!
    It’s guaranteed that array contains at least 3 numbers.
    :param arr: An array containing 3 or more numbers with one being different than the rest.
    :return: The integer within the array which isn't the same.
    """
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


class TestFindUniq(unittest.TestCase):
    """Class to test 'find_uniq' function"""

    def test_find_uniq(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
        self.assertEqual(find_uniq([3, 10, 3, 3, 3]), 10)


if __name__ == '__main__':
    unittest.main()
