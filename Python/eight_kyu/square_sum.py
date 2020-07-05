# Python solution for 'Square(n) Sum' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, ARITHMETIC, MATHEMATICS, ALGORITHMS, NUMBERS, ARRAYS, LISTS, and DATA STRUCTURES.
# Author: Jack Brokenshire
# Date: 05/07/2020

import unittest


def square_sum(numbers):
    """
    Complete the square sum function so that it squares each number passed into it and then sums the results together.
    :param numbers: an array of integers.
    :return: the sum of all the square elements in the array.
    """
    return sum(x ** 2 for x in numbers)


class TestSquareSum(unittest.TestCase):
    """Class to test 'square_sum' function"""

    def test_square_sum(self):
        self.assertEqual(square_sum([1, 2]), 5)
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)


if __name__ == '__main__':
    unittest.main()
