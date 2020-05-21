# Python solution for 'Roman Numerals Decoder' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, PARSING, and STRINGS.
# Author: Jack Brokenshire
# Date: 21/05/2020

import unittest


def roman_numerals_decoder(roman):
    """
    Takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
    :param roman: a roman numeral.
    :return: the roman numeral as a numeric decimal integer.
    """
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i, c in enumerate(roman):
        if (i + 1) == len(roman) or roman_numerals[c] >= roman_numerals[roman[i + 1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result


class TestRomanNumeralsDecoder(unittest.TestCase):
    """Class to test 'roman_numerals_decoder' function"""

    def test_roman_numerals_decoder(self):
        self.assertEqual(roman_numerals_decoder('XXI'), 21)
        self.assertEqual(roman_numerals_decoder('I'), 1)
        self.assertEqual(roman_numerals_decoder('IV'), 4)
        self.assertEqual(roman_numerals_decoder('MMVIII'), 2008)
        self.assertEqual(roman_numerals_decoder('MDCLXVI'), 1666)


if __name__ == '__main__':
    unittest.main()
