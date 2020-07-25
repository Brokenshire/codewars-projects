# Python solution for 'Capitalization and Mutability' codewars question.
# Level: 8 kyu
# Tags: BUGS, STRINGS, UTILITIES, BASIC LANGUAGE FEATURES, AND FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 25/07/2020

import unittest


def capitalize_word(word):
    """
    Capitalize the first letter of the word.
    :param word: a string input.
    :return: the word in title form.
    """
    return word.title()


class TestCapitalizeWord(unittest.TestCase):
    """Class to test 'capitalize_word' function"""

    def test_capitalize_word(self):
        self.assertEqual(capitalize_word('word'), 'Word')
        self.assertEqual(capitalize_word('i'), 'I')
        self.assertEqual(capitalize_word('glasswear'), 'Glasswear')


if __name__ == '__main__':
    unittest.main()
