# Python solution for 'Counting Duplicates' codewars question.
# Level: 6 kyu
# Tags: Fundamentals and Strings.
# Author: Jack Brokenshire
# Date: 09/03/2020

import unittest


def duplicate_count(text):
    """
    Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
    that occur more than once in the input string. The input string can be assumed to contain only alphabets (both
    uppercase and lowercase) and numeric digits.
    :param text: an input string.
    :return: the amount of duplicate characters within the string.
    """
    return len([x for x in set(text.lower()) if text.lower().count(x) > 1])


class TestDuplicateCount(unittest.TestCase):
    """Class to test 'duplicate_count' function"""

    def test_duplicate_count(self):
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdea"), 1)
        self.assertEqual(duplicate_count("indivisibility"), 1)


if __name__ == '__main__':
    unittest.main()
