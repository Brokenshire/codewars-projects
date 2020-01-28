# Python solution for Beginner Series #3 Sum of Numbers codewars question.
# Level: 7 kyu
# Tags: Fundamentals, and Algorithms
# Author: Jack Brokenshire
# Date: 24/01/2020

import unittest


def get_sum(a, b):
    """ Given two integers a and b, which can be positive or negative,
        find the sum of all the numbers between including them too and return it.
        If the two numbers are equal return a or b.
    """
    return sum(range(min(a, b), max(a, b) + 1))


class TestSum(unittest.TestCase):
    """Class to test get_sum function"""
    
    def test_sum(self):
        self.assertEqual(get_sum(0, -1), -1)
        self.assertEqual(get_sum(1, 0), 1)
        self.assertEqual(get_sum(1, 2), 3)
        self.assertEqual(get_sum(0, 1), 1)
        self.assertEqual(get_sum(1, 1), 1)
        self.assertEqual(get_sum(-1, 0), -1)
        self.assertEqual(get_sum(-1, 2), 2)


if __name__ == '__main__':
    unittest.main()
