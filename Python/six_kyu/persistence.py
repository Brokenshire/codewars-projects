# Python solution for 'Persistent Bugger.' codewars question.
# Level: 6 kyu
# Tags: Fundamentals, and Numbers
# Author: Jack Brokenshire
# Date: 11/02/2020

import unittest


def persistence(n):
    """
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
    which is the number of times you must multiply the digits in num until you reach a single digit.
    :param n: an integer value.
    :return: the numbers of times the digits in 'n' need to be multiplied to get to a single digit.
    """
    if n < 10:
        return 0
    total = 1
    for i in str(n):
        total = total * int(i)
    return 1 + persistence(total)


class TestPersistence(unittest.TestCase):
    """Class to test 'persistence' function"""

    def test_persistence(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(999), 4)


if __name__ == '__main__':
    unittest.main()
