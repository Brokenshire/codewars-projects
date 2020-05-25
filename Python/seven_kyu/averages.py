# Python solution for 'Averages of numbers' codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS, FUNDAMENTALS, and BASIC LANGUAGE FEATURES.
# Author: Jack Brokenshire
# Date: 25/05/2020

import unittest


def averages(arr):
    """
    Computes the average of two integers and returns an array of them.
    :param arr: array of integers.
    :return: an array of the averages of each integer-number and his follower.
    """
    if arr is None:
        return []
    return [(arr[x] + arr[x+1]) / 2 for x in range(len(arr)-1)]


class TestAverages(unittest.TestCase):
    """Class to test 'averages' function"""

    def test_averages(self):
        tests = (
            ([2, 2, 2, 2], [2, 2, 2, 2, 2]),
            ([0, 0, 0, 0], [2, -2, 2, -2, 2]),
            ([2, 4, 3, -4.5], [1, 3, 5, 1, -10]),
            ([], [])
        )

        for exp, inp in tests:
            self.assertEquals(averages(inp), exp)


if __name__ == '__main__':
    unittest.main()
