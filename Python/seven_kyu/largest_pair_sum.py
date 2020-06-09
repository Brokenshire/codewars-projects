# Python solution for 'Largest pair sum in array' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 09/06/2020

import unittest


def largest_pair_sum(numbers):
    """
    Given a sequence of numbers, find the largest pair sum in the sequence.
    :param numbers: an array of integers.
    :return: the sum of the two largest integers within the array.
    """
    return sum(sorted(numbers)[-2:])


class TestLargestPairSum(unittest.TestCase):
    """Class to test 'largest_pair_sum' function"""

    def test_largest_pair_sum(self):
        self.assertEquals(largest_pair_sum([10, 14, 2, 23, 19]), 42)
        self.assertEquals(largest_pair_sum([-100, -29, -24, -19, 19]), 0)
        self.assertEquals(largest_pair_sum([1, 2, 3, 4, 6, -1, 2]), 10)
        self.assertEquals(largest_pair_sum([-10, -8, -16, -18, -19]), -18)


if __name__ == '__main__':
    unittest.main()
