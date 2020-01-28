# Python solution for Most digits codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Numbers, and Strings
# Author: Jack Brokenshire
# Date: 27/01/2020

import unittest


def find_longest(arr):
    """ Find the number with the most digits.
        If two numbers in the argument array have the same number of digits,
        return the first one in the array.
    """
    return max(arr, key=lambda x: len(str(x)))


class TestFindLongest(unittest.TestCase):
    """Class to test find_longest function"""

    def test_find_longest(self):
        self.assertEqual(find_longest([1, 10, 100]), 100)
        self.assertEqual(find_longest([9000, 8, 800]), 9000)
        self.assertEqual(find_longest([8, 900, 500]), 900)
        self.assertEqual(find_longest([3, 40000, 100]), 40000)
        self.assertEqual(find_longest([1, 200, 100000]), 100000)


if __name__ == '__main__':
    unittest.main()
