# Python solution for 'String ends with?' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS and STRINGS.
# Author: Jack Brokenshire
# Date: 13/04/2020

import unittest


def end_with(string, ending):
    """
    Boolean return value if string has the same ending as another string.
    :param string: the string to be checked.
    :param ending: the ending string.
    :return: True if the last characters of string are the same as ending otherwise, False.
    """
    return string.endswith(ending)


class TestEndWith(unittest.TestCase):
    """Class to test end_with function"""

    def test_end_with(self):
        self.assertEqual(end_with('abc', 'bc'), True)
        self.assertEqual(end_with('abc', 'd'), False)
        self.assertEqual(end_with('abcde', 'cde'), True)
        self.assertEqual(end_with('abcde', 'abc'), False)
        self.assertEqual(end_with('abcde', ''), True)


if __name__ == '__main__':
    unittest.main()
