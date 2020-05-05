# Python solution for 'Grasshopper - Summation' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, LOOPS, CONTROL FLOW, and BASIC LANGUAGE FEATURES
# Author: Jack Brokenshire
# Date: 05/05/2020

import unittest


def summation(num):
    """
    Finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
    :param num: an integer.
    :return: the sum of the range of numbers.
    """
    return sum(x for x in range(num+1))


class TestSummation(unittest.TestCase):
    """Class to test 'summation' function"""

    def test_summation(self):
        self.assertEqual(summation(1), 1)
        self.assertEqua(summation(8), 36)
        self.assertEqua(summation(22), 253)
        self.assertEqua(summation(100), 5050)
        self.assertEqua(summation(213), 22791)


if __name__ == '__main__':
    unittest.main()
