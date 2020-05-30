# Python solution for 'Find the missing letter' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, MATHEMATICS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 31/05/2020

import unittest
from string import ascii_lowercase, ascii_uppercase


def find_missing_letter(chars):
    """
    Finds the missing character inside an array of characters.
    :param chars: an array of characters.
    :return: the missing letter in the array.
    """
    charset = ascii_lowercase if chars[0] >= "a" else ascii_uppercase
    for letter in charset[charset.index(chars[0]):]:
        if letter not in chars:
            return letter[0]


class TestFindMissingLetter(unittest.TestCase):
    """Class to test 'find_missing_letter' function"""

    def test_find_missing_letter(self):
        self.assertEquals(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
        self.assertEquals(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')


if __name__ == '__main__':
    unittest.main()
