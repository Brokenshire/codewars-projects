# Python solution for 'Consecutive letters' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 06/07/2020

import unittest


def solve(st):
    """
    In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if
    each letter occurs only once.
    :param st: lowercase string input.
    :return: true if each letter occurs once in alphabetical order, otherwise, false.
    """
    string = "".join(sorted(st))
    for x in range(1, len(st)):
        if ord(string[x]) - ord(string[x - 1]) != 1:
            return False
    return True


class TestSolve(unittest.TestCase):
    """Class to test 'solve' function"""

    def test_solve(self):
        self.assertEqual(solve("abc"), True)
        self.assertEqual(solve("abd"), False)
        self.assertEqual(solve("dabc"), True)
        self.assertEqual(solve("abbc"), False)


if __name__ == '__main__':
    unittest.main()
