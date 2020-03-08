# Python solution for 'Find The Parity Outlier' codewars question.
# Level: 6 kyu
# Tags: Algorithms.
# Author: Jack Brokenshire
# Date: 08/03/2020

import unittest


def find_outlier(integers):
    """
    You are given an array (which will have a length of at least 3, but could be very large) containing integers.
    The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
    integer N. Write a method that takes the array as an argument and returns this "outlier" N.
    :param integers: an array, at least length 3.
    :return: the odd integer out from the rest.
    """
    odds = [x for x in integers if x % 2 != 0]
    evens = [x for x in integers if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


class TestFindIt(unittest.TestCase):
    """Class to test 'find_it' function"""

    def test_find_it(self):
        self.assertEqual(find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)


if __name__ == '__main__':
    unittest.main()
