# Python solution for 'No oddities here' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, and ARRAYS.
# Author: Jack Brokenshire
# Date: 30/05/2020

import unittest


def no_odds(values):
    """
    Finds all the even integers inside an array.
    :param values: an array of integers.
    :return: an array of even integers.
    """
    return [x for x in values if x % 2 == 0]


class TestNoOdds(unittest.TestCase):
    """Class to test 'no_odds' function"""

    def test_no_odds(self):
        self.assertEquals(no_odds([0, 1]), [0], 'Zero through one')
        self.assertEquals(no_odds([0, 1, 2, 3]), [0, 2], 'Zero through three')
        self.assertEquals(no_odds([1, 3, 5, 7, 9]), [], 'Odds through ten')
        self.assertEquals(no_odds([0, 2, 4, 6, 8, 10]), [0, 2, 4, 6, 8, 10], 'Evens through ten')
        self.assertEquals(no_odds([-1, -3, -5, -7, -9]), [], 'Negative odds')
        self.assertEquals(no_odds([2, 4, 8, 6, 0]), [2, 4, 8, 6, 0], 'Out of order')
        self.assertEquals(no_odds([]), [], 'Empty list')


if __name__ == '__main__':
    unittest.main()
