# Python solution for 'Sum of odd numbers' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, ARRAYS, LISTS, DATA STRUCTURES, NUMBERS, ARITHMETIC, MATHEMATICS, and ALGORITHMS.
# Author: Jack Brokenshire
# Date: 11/05/2020

import unittest


def row_sum_odd_numbers(n):
    """
    Calculate the row sums of this triangle from the row index (starting at index 1).
    :param n: an integer.
    :return: the sum of the row in the triangle.
    """
    return n**3


class TestRowSumOddNumbers(unittest.TestCase):
    """Class to test 'row_sum_odd_numbers' function"""

    def test_row_sum_odd_numbers(self):
        self.assertEqual(row_sum_odd_numbers(1), 1)
        self.assertEqual(row_sum_odd_numbers(2), 8)
        self.assertEqual(row_sum_odd_numbers(13), 2197)
        self.assertEqual(row_sum_odd_numbers(19), 6859)
        self.assertEqual(row_sum_odd_numbers(41), 68921)


if __name__ == '__main__':
    unittest.main()
