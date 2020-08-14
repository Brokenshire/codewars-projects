# Python solution for 'Find Multiples of a Number' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 14/08/2020

import unittest


def find_multiples(integer, limit):
    """
    Finds all integers multiples.
    :param integer: integer value.
    :param limit: integer value.
    :return: a list of its multiples up to another value, limit.
    """
    return [x for x in range(1, limit + 1) if x % integer == 0]


class TestFindMultiples(unittest.TestCase):
    """Class to test 'find_multiples' function"""

    def test_find_multiples(self):
        self.assertEqual(find_multiples(5, 25), [5, 10, 15, 20, 25])
        self.assertEqual(find_multiples(1, 2), [1, 2])


if __name__ == "__main__":
    unittest.main()
