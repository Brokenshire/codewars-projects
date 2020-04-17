# Python solution for 'Break camelCase' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS,STRINGS, FORMATTING, and ALGORITHMS.
# Author: Jack Brokenshire
# Date: 17/04/2020

import unittest
import re


def break_camel_case(s):
    """
    Complete the solution so that the function will break up camel casing, using a space between words.
    :param s: a string input.
    :return: a new string with spaces before capital letters.
    """
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)


class TestBreakCamelCase(unittest.TestCase):
    """Class to test 'break_camel_case' function"""

    def test_break_camel_case(self):
        self.assertEqual(break_camel_case("helloWorld"), "hello World")
        self.assertEqual(break_camel_case("camelCase"), "camel Case")
        self.assertEqual(break_camel_case("breakCamelCase"), "break Camel Case")


if __name__ == '__main__':
    unittest.main()
