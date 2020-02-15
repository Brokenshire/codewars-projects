# Python solution for 'Exes and Ohs' codewars question.
# Level: 7 kyu
# Tags: Algorithms, Aggregations, Arithmetic, Mathematics, Numbers, and Integers.
# Author: Jack Brokenshire
# Date: 15/02/2020

import unittest


def xo(s):
    """
    Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be
    case insensitive. The string can contain any char.
    :param s: A string value input.
    :return: True if amount of 'x's and 'o's are the same, Else False.
    """
    return s.lower().count("x") == s.lower().count("o")


class TestXo(unittest.TestCase):
    """Class to test 'xo' function"""

    def test_xo(self):
        self.assertEqual(xo('xo'), 'True expected')
        self.assertEqual(xo('xo0'), 'True expected')
        self.assertEqual(not xo('xxxoo'), 'False expected')


if __name__ == '__main__':
    unittest.main()
