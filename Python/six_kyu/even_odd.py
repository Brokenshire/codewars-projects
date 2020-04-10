# Python solution for "Even Odd Pattern #1" codewars question.
# Level: 6 kyu
# Tags: Puzzles, Arrays, Mathematics, Algorithms, and Numbers.
# Author: Jack Brokenshire
# Date: 24/03/2020

import unittest


def even_odd(arr):
    """
    Function which adds onto total when even and times number onto total when odd.
    :param arr: an array of integers.
    :return: the sum of adding when even and multiplying when odd.
    """
    total = 0
    for i, j in enumerate(arr):
        if i % 2 == 0:
            total += j
        else:
            total *= j
    return total


class TestEvenOdd(unittest.TestCase):
    """Class to test "even_odd" function"""

    def test_even_odd(self):
        self.assertEqual(even_odd([1, 2, 3]), 5)
        self.assertEqual(even_odd([0, 2, 3]), 3)
        self.assertEqual(even_odd([1, 0, 3]), 3)
        self.assertEqual(even_odd([1, 2, 2, 1, 6, 1, 3, 9, 6, 1]), 123)


if __name__ == "__main__":
    unittest.main()
