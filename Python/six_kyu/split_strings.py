# Python solution for "Split Strings" codewars question.
# Level: 6 kyu
# Tags: Algorithms, Regular Expressions, Declarative Programming, Advanced Language Features, Fundamentals, and Strings.
# Author: Jack Brokenshire
# Date: 20/03/2020

import unittest


def split_strings(s):
    """
    Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number
    of characters then it should replace the missing second character of the final pair with an underscore ('_').
    :param s: a string input.
    :return: the string as an array of pairs. If not even add an underscore to final character to make a pair.
    """
    if len(s) % 2 != 0:
        s += "_"
    return [s[x:x + 2] for x in range(0, len(s), 2)]


class TestSplitStrings(unittest.TestCase):
    """Class to test "split_strings" function"""

    def test_split_strings(self):
        self.assertEqual("asdfadsf", ['as', 'df', 'ad', 'sf'])
        self.assertEqual("asdfads", ['as', 'df', 'ad', 's_'])
        self.assertEqual("", [])
        self.assertEqual("x", ["x_"])


if __name__ == "__main__":
    unittest.main()
