# Python solution for 'Array.diff' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, and Arrays.
# Author: Jack Brokenshire
# Date: 14/02/2020

import unittest


def array_diff(a, b):
    """
    Your goal in this kata is to implement a difference function, which subtracts one list from another and
    returns the result. It should remove all values from list a, which are present in list b.
    :param a: An array of integers to be changed.
    :param b: An array of integers to be removed from 'a'.
    :return: A new array with integers within 'b' removed from 'a'.
    """
    return [x for x in a if x not in b]


class TestArrayDiff(unittest.TestCase):
    """Class to test 'array_diff' function"""

    def test_array_diff(self):
        self.assertEqual(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEqual(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEqual(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEqual(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEqual(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")


if __name__ == '__main__':
    unittest.main()
