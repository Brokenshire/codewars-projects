# Python solution for 'Maximum Multiple' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Numbers, Basic Language Features, Arrays, Loops, and Control Flow.
# Author: Jack Brokenshire
# Date: 06/02/2020

import unittest


def max_multiple(divisor, bound):
    """
    Finds the largest dividable integer that is lower than bound.
    :param divisor: positive integer.
    :param bound: positive integer.
    :return: the largest integer N, such that, N is divisible by divisor, N is less
             than or equal to bound, and N is greater than 0.
    """
    return bound - (bound % divisor)


class TestMaxMultiple(unittest.TestCase):
    """Class to test 'max_multiple' function"""

    def test_max_multiple(self):
        self.assertEqual(max_multiple(2, 7), 6);
        self.assertEqual(max_multiple(3, 10), 9);
        self.assertEqual(max_multiple(7, 17), 14);
        self.assertEqual(max_multiple(10, 50), 50);
        self.assertEqual(max_multiple(37, 200), 185);
        self.assertEqual(max_multiple(7, 100), 98);


if __name__ == '__main__':
    unittest.main()
