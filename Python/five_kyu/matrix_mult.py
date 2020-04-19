# Python solution for 'Square Matrix Multiplication' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS, GRAPHS, DATA STRUCTURES, ARITHMETIC, MATHEMATICS, NUMBERS, LINEAR ALGEBRA, ALGEBRA LOOPS,
#       CONTROL FLOW, BASIC LANGUAGE FEATURES, and FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 19/04/2020

import unittest


def matrix_mult(a, b):
    """
    Performs matrix multiplication on two given matrices.
    :param a: lists of lists containing integers.
    :param b: lists of lists containing integers.
    :return: the right hand side of the equation.
    """
    table = [[0 for x in range(len(b))] for x in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                table[i][j] += a[i][k] * b[k][j]
    return table


class TestMatrixMult(unittest.TestCase):
    """Class to test 'matrix_mult' function"""

    def test_matrix_mult(self):
        self.assertEqual(matrix_mult([[1, 2], [3, 2]], [[3, 2], [1, 1]]), [[5, 4], [11, 8]])
        self.assertEqual(matrix_mult([[9, 7], [0, 1]], [[1, 1], [4, 12]]), [[37, 93], [4, 12]])
        self.assertEqual(matrix_mult([[1, 2, 3], [3, 2, 1], [2, 1, 3]], [[4, 5, 6], [6, 5, 4], [4, 6, 5]]),
                           [[28, 33, 29], [28, 31, 31], [26, 33, 31]])


if __name__ == '__main__':
    unittest.main()
