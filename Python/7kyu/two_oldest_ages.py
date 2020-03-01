# Python solution for 'Two Oldest Ages' codewars question.
# Level: 7 kyu
# Tags: Algorithms and Arrays.
# Author: Jack Brokenshire
# Date: 01/03/2020

import unittest


def two_oldest_ages(ages):
    """
    The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and
    return the two highest numbers within the array. The returned value should be an array in the format
    [second oldest age, oldest age]. The order of the numbers passed in could be any order. The array will
    always include at least 2 items.
    :param ages: an array of numbers.
    :return: the highest two values within the array.
    """
    return sorted(ages)[-2:]


class TestTwoOldestAges(unittest.TestCase):
    """Class to test 'two_oldest_ages' function"""

    def test_two_oldest_ages(self):
        self.assertEqual(two_oldest_ages([1, 5, 87, 45, 8, 8]), [45, 87])
        self.assertEqual(two_oldest_ages([6, 5, 83, 5, 3, 18]), [18, 83])
        self.assertEqual(two_oldest_ages([10, 1]), [1, 10])


if __name__ == '__main__':
    unittest.main()
