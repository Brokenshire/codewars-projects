# Python solution for 'Return a string's even characters.' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, STRING, AND SARRAYS.
# Author: Jack Brokenshire
# Date: 16/08/2020

import unittest


def even_chars(st):
    """
    Finds all the even characters in a string.
    :param st: string value.
    :return: a sequence (index begins with 1) of all the even characters from a string. If the string is smaller than
             two characters or longer than 100 characters, the function should return "invalid string".
    """
    if len(st) < 2 or len(st) > 100: return "invalid string"
    else: return [st[i] for i in range(len(st)) if i % 2]


class TestEvenChars(unittest.TestCase):
    """Class to test 'even_chars' function"""

    def test_even_chars(self):
        self.assertEqual(even_chars("a"), "invalid string")
        self.assertEqual(even_chars("abcdefghijklm"), ["b", "d", "f", "h", "j", "l"])
        self.assertEqual(even_chars("aBc_e9g*i-k$m"), ["B", "_", "9", "*", "-", "$"])


if __name__ == "__main__":
    unittest.main()
