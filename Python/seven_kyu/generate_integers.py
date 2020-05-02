# Python solution for 'Series of integers from m to n' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 02/05/2020

import unittest


def generate_integers(m, n):
    """
    Accepts two arguments and generates a sequence containing the integers from the first argument to the second inclusive.
    :param m: an integer value of starting index.
    :param n: an integer value of ending index.
    :return: the values in the range between m and n.
    """
    return list(range(m, n + 1))


class TestGenerateIntegers(unittest.TestCase):
    """Class to test 'generate_integers' function"""

    def test_generate_integers(self):
        self.assertEqual(generate_integers(2, 5), [2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
