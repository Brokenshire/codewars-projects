# Python solution for 'Return the first M multiples of N' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 09/07/2020

import unittest


def multiples(m, n):
    """
    Builds a list of the first m multiples of the real number n.
    :param m: an positive integer value.
    :param n: an real integer number.
    :return: an array of the first m multiples of the real number n.
    """
    return [n * x for x in range(1, m + 1)]


class TestMultiples(unittest.TestCase):
    """Class to test 'multiples' function"""

    def test_multiples(self):
        self.assertEqual(multiples(3, 5), [5, 10, 15])


if __name__ == '__main__':
    unittest.main()
