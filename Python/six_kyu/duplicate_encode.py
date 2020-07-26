# Python solution for 'Duplicate Encoder' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, STRINGS, AND ARRAYS.
# Author: Jack Brokenshire
# Date: 26/07/2020

import unittest


def duplicate_encode(word):
    """
    converts a string to a new string where each character in the new string is "(" if that character appears only once
    in the original string, or ")" if that character appears more than once in the original string.
    :param word: a string input.
    :return: a new string with duplicate characters represented by ')' and single characters by '('.
    """
    return "".join(")" if word.lower().count(x) > 1 else "(" for x in word.lower())


class TestDuplicateEncode(unittest.TestCase):
    """Class to test 'duplicate_encode' function"""

    def test_duplicate_encode(self):
        self.assertEqual(duplicate_encode("din"), "(((")
        self.assertEqual(duplicate_encode("recede"), "()()()")
        self.assertEqual(duplicate_encode("Success"), ")())())", "should ignore case")
        self.assertEqual(duplicate_encode("(( @"), "))((")


if __name__ == "__main__":
    unittest.main()
