# Python solution for 'Gauß needs help! (Sums of a lot of numbers)' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Mathematics, Algorithms, Numbers, Performance, and Integers.
# Author: Jack Brokenshire
# Date: 05/02/2020

import unittest


def f(n):
    """
    Function finds the sum from 1 to 'n'.
    :param n: an random variable type.
    :return: the sum from 1 to the value 'n'. If not a valid positive int return None.
    """
    return (n + 1) * n //2 if (type(n) is int and n>0) else None


class TestF(unittest.TestCase):
    """Class to test 'f' function"""

    def test_f(self):
        self.assertEqual(f(1), 1)
        self.assertEqual(f(100), 5050)


if __name__ == '__main__':
    unittest.main()
