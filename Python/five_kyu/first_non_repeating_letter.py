# Python solution for 'First non-repeating character' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS, STRINGS, and SEARCH.
# Author: Jack Brokenshire
# Date: 26/05/2020

import unittest


def first_non_repeating_letter(string):
    """
    Finds and returns the first non repeating character inside a string.
    :param string: a string value.
    :return: the first character that is not repeated anywhere in the string.
    """
    return next((x for x in string if string.lower().count(x.lower()) == 1), "")


class TestFirstNonRepeatingLetter(unittest.TestCase):
    """Class to test 'first_non_repeating_letter' function"""

    def test_first_non_repeating_letter(self):
        self.assertEquals(first_non_repeating_letter('a'), 'a')
        self.assertEquals(first_non_repeating_letter('stress'), 't')
        self.assertEquals(first_non_repeating_letter('moonmen'), 'e')
        self.assertEquals(first_non_repeating_letter(''), '')
        self.assertEquals(first_non_repeating_letter('abba'), '')
        self.assertEquals(first_non_repeating_letter('aa'), '')
        self.assertEquals(first_non_repeating_letter('~><#~><'), '#')
        self.assertEquals(first_non_repeating_letter('hello world, eh?'), 'w')
        self.assertEquals(first_non_repeating_letter('sTreSS'), 'T')
        self.assertEquals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')


if __name__ == '__main__':
    unittest.main()
