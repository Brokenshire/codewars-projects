# Python solution for 'Backspaces in string' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, FUNDAMENTALS, and STRINGS.
# Author: Jack Brokenshire
# Date: 05/06/2020

import unittest


def clean_string(s):
    """
    Process a string with "#" representing backspaces.
    :param s: a string value.
    :return: the string after processing the backspaces.
    """
    stack = []
    for x in s:
        if x == "#":
            if stack:
                stack.pop()
        else:
            stack.append(x)
    return "".join(stack)


class TestCleanString(unittest.TestCase):
    """Class to test 'clean_string' function"""

    def test_clean_string(self):
        self.assertEquals(clean_string('abc#d##c'), "ac")
        self.assertEquals(clean_string('abc####d##c#'), "")
        self.assertEquals(clean_string("#######"), "")
        self.assertEquals(clean_string(""), "")


if __name__ == '__main__':
    unittest.main()
