# Python solution for 'Sum of all the multiples of 3 or 5' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 18/05/2020

import unittest


def find(n):
    """
    Finds the sum of all multiples of 3 and 5 of an integer.
    :param n: an integer value.
    :return: the sum of all multiples of 3 and 5.
    """
    return sum(x for x in range(n+1) if x % 5 == 0 or x % 3 == 0)


class TestFind(unittest.TestCase):
    """Class to test 'find' function"""

    def test_find(self):
        self.assertEqual(find(5), 8)
        self.assertEqual(find(10), 33)


if __name__ == '__main__':
    unittest.main()
