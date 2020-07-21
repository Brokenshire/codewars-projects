# Python solution for 'Fix string case' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS
# Author: Jack Brokenshire
# Date: 21/07/2020

import unittest


def solve(s):
    """
    String that may have mixed uppercase and lowercase letters and your task is to convert that string to either
    lowercase only or uppercase
    :param s: a string input.
    :return: convert string into lower or upper case making the fewest changes. if the string contains equal number of
             uppercase and lowercase letters, convert the string to lowercase.
    """
    l = 0
    u = 0
    for x in s:
        if x == x.lower():
            l += 1
        else:
            u += 1
    if l < u:
        return s.upper()
    return s.lower()


class TestSolve(unittest.TestCase):
    """Class to test 'solve' function"""

    def test_solve(self):
        self.assertEqual(solve("code"), "code")
        self.assertEqual(solve("CODe"), "CODE")
        self.assertEqual(solve("COde"), "code")
        self.assertEqual(solve("Code"), "code")


if __name__ == '__main__':
    unittest.main()
