# Python solution for 'Playing with digits' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, Mathematics, Algorithms, and Numbers.
# Author: Jack Brokenshire
# Date: 12/03/2020

import unittest


def dig_pow(n, p):
    """
    Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find
    a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal
    to k * n. In other words: Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    If it is the case we will return k, if not return -1.
    :param n: positive integer.
    :param p: positive integer.
    :return:  sum of digits of n taken to the successive powers p is equal to k * n.
    """
    t = sum(pow(int(j), p+i) for i, j in enumerate(str(n)))
    return t/n if t % n == 0 else -1


class TestDigPow(unittest.TestCase):
    """Class to test 'dig_pow' function"""

    def test_dig_pow(self):
        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(46288, 3), 51)


if __name__ == '__main__':
    unittest.main()
