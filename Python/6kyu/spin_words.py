# Python solution for 'Stop gninnipS My sdroW!' codewars question.
# Level: 6 kyu
# Tags: Algorithms, Strings, and Formatting.
# Author: Jack Brokenshire
# Date: 12/02/2020

import unittest


def spin_words(sentence):
    """
    Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
    letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
    Spaces will be included only when more than one word is present.
    :param sentence: A string which may be a sentence.
    :return: the same string however, if the letters in a word are five or more reverse it.
    """
    return " ".join([x if len(x) < 5 else x[::-1] for x in sentence.split(" ")])


class TestSpinWords(unittest.TestCase):
    """Class to test 'spin_words' function"""

    def test_spin_words(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")


if __name__ == '__main__':
    unittest.main()
