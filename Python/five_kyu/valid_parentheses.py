# Python solution for 'Valid Parentheses' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS, VALIDATION, and UTILITIES.
# Author: Jack Brokenshire
# Date: 25/06/2020

import unittest


def valid_parentheses(string):
    """
    Takes a string of parentheses, and determines if the order of the parentheses is valid.
    :param string: a string of parentheses and characters.
    :return: true if the string is valid, and false if it's invalid.
    """
    stack = []
    for x in string:
        if x == "(":
            stack.append(x)
        elif x == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return not stack


class TestValidParentheses(unittest.TestCase):
    """Class to test 'valid_parentheses' function"""

    def test_valid_parentheses(self):
        self.assertEqual(valid_parentheses("  ("), False)
        self.assertEqual(valid_parentheses(")test"), False)
        self.assertEqual(valid_parentheses(""), True)
        self.assertEqual(valid_parentheses("hi())("), False)
        self.assertEqual(valid_parentheses("hi(hi)()"), True)


if __name__ == '__main__':
    unittest.main()
