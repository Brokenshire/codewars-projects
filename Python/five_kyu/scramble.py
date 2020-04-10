# Python solution for "Scramblies" codewars question.
# Level: 5 kyu
# Tags: Algorithms, Strings, Performance, Optimization.
# Author: Jack Brokenshire
# Date: 19/03/2020

import unittest
from collections import Counter


def scramble(s1, s2):
    """
    Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to
    match str2, otherwise returns false. Notes: Only lower case letters will be used (a-z). No punctuation or digits
    will be included. Performance needs to be considered Input strings s1 and s2 are null terminated.
    :param s1: a string input.
    :param s2: a string input.
    :return: true if str1 can be rearranged to match str2, otherwise returns false.
    """
    return len(Counter(s2) - Counter(s1)) == 0


class TestScramble(unittest.TestCase):
    """Class to test "unique_in_order" function"""

    def test_unique_in_order(self):
        self.assertEqual(scramble("rkqodlw", "world"),  True)
        self.assertEqual(scramble("cedewaraaossoqqyt", "codewars"), True)
        self.assertEqual(scramble("katas", "steak"), False)
        self.assertEqual(scramble("scriptjava", "javascript"), True)
        self.assertEqual(scramble("scriptingjava", "javascript"), True)


if __name__ == "__main__":
    unittest.main()
