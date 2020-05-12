# Python solution for 'Multiplication table' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, ARITHMETIC, MATHEMATICS, ALGORITHMS, NUMBERS, and ARRAYS.
# Author: Jack Brokenshire
# Date: 12/05/2020

import unittest


def mult_table(size):
    """
    Build Multiplication table given an integer value.
    :param size: an interger value.
    :return: NxN multiplication table, of size provided in parameter.
    """
    return [[i * j for i in range(1, size + 1)] for j in range(1, size + 1)]


class TestMultTable(unittest.TestCase):
    """Class to test 'mult_table' function"""

    def test_mult_table(self):
        self.assertEqual(mult_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])


if __name__ == '__main__':
    unittest.main()
