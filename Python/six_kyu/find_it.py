# Python solution for 'Find the odd int' codewars question.
# Level: 6 kyu
# Tags: Fundamentals.
# Author: Jack Brokenshire
# Date: 07/03/2020

import unittest


def find_it(seq):
    """
    Given an array, find the integer that appears an odd number of times. There will always be only one integer that
    appears an odd number of times.
    :param seq: an array of integers.
    :return: the integer that appears an odd number of times.
    """
    for x in seq:
        if seq.count(x) % 2 != 0:
            return x


class TestFindIt(unittest.TestCase):
    """Class to test 'find_it' function"""

    def test_find_it(self):
        self.assertEqual(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
        self.assertEqual(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)
        self.assertEqual(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)
        self.assertEqual(find_it([10]), 10)
        self.assertEqual(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)
        self.assertEqual(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)


if __name__ == '__main__':
    unittest.main()
