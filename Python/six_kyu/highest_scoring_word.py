# Python solution for "Highest Scoring Word" codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, STRINGS, ARRAYS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 01/04/2020

import unittest


def highest_scoring_word(x):
    """
    Given a string of words, you need to find the highest scoring word. Each letter of a word scores points according
    to its position in the alphabet: a = 1, b = 2, c = 3 etc. You need to return the highest scoring word as a string.
    If two words score the same, return the word that appears earliest in the original string. All letters will be
    lowercase and all inputs will be valid.
    :param x: a string of words.
    :return: finds and returns the word with the highest score.
    """
    a = [sum(ord(i) - 96 for i in j) for j in x.split()]
    return x.split()[a.index(max(a))]


class TestHighestScoringWord(unittest.TestCase):
    """Class to test "highest_scoring_word" function"""

    def test_highest_scoring_word(self):
        self.assertEqual(highest_scoring_word('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(highest_scoring_word('what time are we climbing up the volcano'), 'volcano')
        self.assertEqual(highest_scoring_word('take me to semynak'), 'semynak')


if __name__ == "__main__":
    unittest.main()
