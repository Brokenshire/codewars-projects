# Python solution for 'Remove duplicate words' codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS, STRINGS, REGULAR EXPRESSION, SDECLARATIVE PROGRAMMING,
#       ADVANCED LANGUAGE FEATURES, and FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 01/06/2020

import unittest


def remove_duplicate_words(s):
    """
    Removes all duplicate words from a string, leaving only single (first) words entries.
    :param s: a string of spaced words.
    :return: string with each word only once.
    """
    words = []
    for x in s.split():
        if x not in words:
            words.append(x)
    return " ".join(words)


class TestRemoveDuplicateWords(unittest.TestCase):
    """Class to test 'remove_duplicate_words' function"""

    def test_remove_duplicate_words(self):
        self.assertEquals(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
        self.assertEquals(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")


if __name__ == '__main__':
    unittest.main()
