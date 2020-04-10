# Python solution for 'Sum of Intervals' codewars question.
# Level: 4 kyu
# Tags: Algorithms, Aggregations, Arithmetic, Mathematics, Numbers, and Integers.
# Author: Jack Brokenshire
# Date: 14/02/2020

import unittest


def sum_of_intervals(intervals):
    """
    Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all
    the interval lengths. Overlapping intervals should only be counted once. Intervals are represented by a pair of
    integers in the form of an array. The first value of the interval will always be less than the second value. Interval
    example: [1, 5] is an interval from 1 to 5. The length of this interval is 4. The sum of the lengths of these
    intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
    :param intervals: An array of intervals.
    :return: The sum of all the interval lengths.
    """
    return len(set(i for x in intervals for i in range(x[0], x[1])))


class TestSumOfIntervals(unittest.TestCase):
    """Class to test 'sum_of_intervals' function"""

    def test_sum_of_intervals(self):
        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)


if __name__ == '__main__':
    unittest.main()
