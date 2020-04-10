# Python solution for "Don't give me five!" codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS, BASIC LANGUAGE FEATURES, FUNDAMENTALS, MATHEMATICS, NUMBERS, and ARRAYS.
# Author: Jack Brokenshire
# Date: 04/04/2020

import unittest


def dont_give_me_five(start, end):
    """
    Start number and the end number of a region and should return the count of all numbers except numbers with a 5 in
    it. The start and the end number are both inclusive!
    :param start: starting integer for range.
    :param end: ending integer for range.
    :return: the amount of numbers within the range without a 5 in it.
    """
    return len([x for x in range(start, end+1) if "5" not in str(x)])


class TestDontGiveMeFive(unittest.TestCase):
    """Class to test "dont_give_me_five" function"""

    def test_dont_give_me_five(self):
        self.assertEqual(dont_give_me_five(1, 9), 8)
        self.assertEqual(dont_give_me_five(4, 17), 12)


if __name__ == "__main__":
    unittest.main()
