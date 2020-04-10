# Python solution for 'Sum of Minimums!' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Numbers, and Arrays.
# Author: Jack Brokenshire
# Date: 29/02/2020

import unittest


def sum_of_minimums(numbers):
    """
    Given a 2D list of size m * n. Your task is to find the sum of minimum value in each row.
    :param numbers: a list of size m * n.
    :return: the sum of each minimum value in each row.
    """
    return sum(min(x) for x in numbers)


class TestSumOfMinimums(unittest.TestCase):
    """Class to test 'sum_of_minimums' function"""

    def test_sum_of_minimums(self):
        self.assertEqual(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]), 9)
        self.assertEqual(sum_of_minimums([[11, 12, 14, 54], [67, 89, 90, 56], [7, 9, 4, 3], [9, 8, 6, 7]]), 76)


if __name__ == '__main__':
    unittest.main()
