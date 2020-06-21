# Python solution for 'Smallest unused ID' codewars question.
# Level: 8 kyu
# Tags: ALGORITHMS and FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 21/06/2020

import unittest


def next_id(arr):
    """
    Finds and returns the smallest unused element from 0 to n.
    :param arr: an array of integers.
    :return: the smallest unused ID for your next new data item.
    """
    for x in range(len(arr) + 1):
        if x not in arr:
            return x


class TestNextId(unittest.TestCase):
    """Class to test 'next_id' function"""

    def test_next_id(self):
        self.assertEqual(next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)
        self.assertEqual(next_id([5, 4, 3, 2, 1]), 0)
        self.assertEqual(next_id([0, 1, 2, 3, 5]), 4)
        self.assertEqual(next_id([0, 0, 0, 0, 0, 0]), 1)
        self.assertEqual(next_id([]), 0)


if __name__ == '__main__':
    unittest.main()
