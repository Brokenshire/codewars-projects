# Python solution for "Replace With Alphabet Position" codewars question.
# Level: 6 kyu
# Tags: Fundamentals and Strings.
# Author: Jack Brokenshire
# Date: 21/03/2020

import unittest


def alphabet_position(text):
    """
    In this kata you are required to, given a string, replace every letter with its position in the alphabet. If
    anything in the text isn't a letter, ignore it and don't return it. "a" = 1, "b" = 2, etc.
    :param text: a string value.
    :return: the index of each character in the input sting as a string.
    """
    return " ".join([str(list("abcdefghijklmnopqrstuvwxyz").index(x) + 1) for x in text.lower() if x.isalpha()])


class TestAlphabetPosition(unittest.TestCase):
    """Class to test "alphabet_position" function"""

    def test_alphabet_position(self):
        from random import randint
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."),
                         "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."),
                         "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        self.assertEqual(alphabet_position(number_test), "")


if __name__ == "__main__":
    unittest.main()
