# Python solution for 'Sum of two lowest positive integers' codewars question.
# Level: 7 kyu
# Tags: Fundamentals and Arrays.
# Author: Jack Brokenshire
# Date: 06/03/2020

import unittest


def sum_two_smallest_numbers(numbers):
    """
    Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive
    integers. No floats or non-positive integers will be passed.
    :param numbers: an array of 4 or more positive numbers.
    :return: the sum of the two smallest values in the array.
    """
    return sum(sorted(numbers)[0:2])


class TestSumTwoSmallestNumbers(unittest.TestCase):
    """Class to test 'sum_two_smallest_numbers' function"""

    def test_sum_two_smallest_numbers(self):
        self.assertEqual(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        self.assertEqual(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        self.assertEqual(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)


if __name__ == '__main__':
    unittest.main()
