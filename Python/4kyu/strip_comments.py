# Python strip_comments for 'Strip Comments' codewars question.
# Level: 4 kyu
# Tags: Algorithms and Strings.
# Author: Jack Brokenshire
# Date: 13/03/2020

import unittest


def strip_comments(string, markers):
    """
    Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
    Any whitespace at the end of the line should also be stripped out.
    :param string: a string input.
    :param markers: list of characters.
    :return: a new string with whitespace and comment markers removed.
    """
    parts = string.split("\n")
    for v in markers:
        parts = [x.split(v)[0].rstrip() for x in parts]
    return "\n".join(parts)


class TestStripComments(unittest.TestCase):
    """Class to test 'strip_comments' function"""

    def test_strip_comments(self):
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
                         "apples, pears\ngrapes\nbananas")
        self.assertEqual(strip_comments("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")


if __name__ == '__main__':
    unittest.main()
