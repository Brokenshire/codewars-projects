# Python solution for 'Roman Numerals Encoder' codewars question.
# Level: 6 kyu
# Tags: Algorithms, and Encoding
# Author: Jack Brokenshire
# Date: 07/02/2020

import unittest


def roman_num(n):
    """
     Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral
     representation of that integer. Modern Roman numerals are written by expressing each digit separately starting with
     the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM,
     90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending
     order: MDCLXVI.
    :param n: a positive integer value.
    :return: a string containing the Roman Numeral representation of that integer 'n'.
    """
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = "M CM D CD C XC L XL X IX V IV I".split()
    result = []
    for a, r in zip(nums, roman):
        b, n = divmod(n, a)
        result.append(r * b)
    return ''.join(result)


class TestRomanNum(unittest.TestCase):
    """Class to test 'roman_num' function"""

    def test_roman_num(self):
        self.assertEqual(roman_num(1), 'I')
        self.assertEqual(roman_num(4), 'IV')
        self.assertEqual(roman_num(6), 'VI')
        self.assertEqual(roman_num(14), 'XIV')
        self.assertEqual(roman_num(21), 'XXI')
        self.assertEqual(roman_num(89), 'LXXXIX')
        self.assertEqual(roman_num(91), 'XCI')
        self.assertEqual(roman_num(984), 'CMLXXXIV')
        self.assertEqual(roman_num(1000), 'M')
        self.assertEqual(roman_num(1889), 'MDCCCLXXXIX')
        self.assertEqual(roman_num(1989), 'MCMLXXXIX')


if __name__ == '__main__':
    unittest.main()
