# Python solution for 'Multiplication Tables' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, MATHEMATICS, ALGORITHMS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 29/04/2020

import unittest


def multiplication_table(row, col):
    """
    Function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table
    sized according to the given dimensions. Each value on the table should be equal to the value of multiplying the
    number in its first row times the number in its first column.
    :param row: an integer value.
    :param col: an integer value.
    :return: an array of arrays filled with integers of the multiplication.
    """
    return [[(i + 1) * (j + 1) for i in range(col)] for j in range(row)]


class TestMultiplicationTable(unittest.TestCase):
    """Class to test 'multiplication_table' function"""

    def test_multiplication_table(self):
        self.assertEqual(multiplication_table(2, 2), [[1, 2], [2, 4]])
        self.assertEqual(multiplication_table(3, 3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])


if __name__ == '__main__':
    unittest.main()
