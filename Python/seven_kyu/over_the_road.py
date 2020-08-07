# Python solution for 'Over The Road' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, NUMBERS, MATHEMATICS, ALGORITHMS, AND PERFORMANCE.
# Author: Jack Brokenshire
# Date: 07/08/2020

import unittest


def over_the_road(address, n):
    """ You've just moved into a perfectly straight street with exactly n identical houses on either side of the road.
        Naturally, you would like to find out the house number of the people on the other side of the street.

    Args:
        address (integer): current address.
        n (integer): length of street.

    Returns:
        integer: Given your house number address and length of street n, give the house number on the opposite side of
                 the street.
    """
    return 2 * n - address + 1


class TestOverTheRoad(unittest.TestCase):
    """Class to test 'over_the_road' function"""

    def test_over_the_road(self):
        self.assertEqual(over_the_road(1, 3), 6)
        self.assertEqual(over_the_road(3, 3), 4)
        self.assertEqual(over_the_road(2, 3), 5)
        self.assertEqual(over_the_road(3, 5), 8)
        self.assertEqual(over_the_road(7, 11), 16)


if __name__ == "__main__":
    unittest.main()
