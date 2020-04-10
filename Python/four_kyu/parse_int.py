# Python solution for 'parseInt() reloaded' codewars question.
# Level: 4 kyu
# Tags: Algorithms, Numbers, Integers, Parsing, and Strings.
# Author: Jack Brokenshire
# Date: 13/02/2020

import unittest


def parse_int(strng):
    """
    In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.
    Examples:
    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
    Additional Notes:
    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
    All tested numbers are valid, you don't need to validate them
    :param strng: An input string which words represent a number.
    :return: The int of the string word.
    """
    words = {j: i for i, j in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen '
                                        'fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
    words.update({j: 10 * i for i, j in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
    thousands = {j: 1000 ** i for i, j in enumerate('thousand million billion trillion quadrillion quintillion '
                                                    'sextillion septillion octillion nonillion decillion'.split(), 1)}
    num = group = 0
    for x in strng.replace(' and ', ' ').replace('-', ' ').split():
        if x == 'hundred':
            group *= words[x]
        elif x in words:
            group += words[x]
        else:
            num += group * thousands[x]
            group = 0
    return num + group


class TestParseInt(unittest.TestCase):
    """Class to test 'parse_int' function"""

    def test_parse_int(self):
        self.assertEqual(parse_int('one'), 1)
        self.assertEqual(parse_int('twenty'), 20)
        self.assertEqual(parse_int('two hundred forty-six'), 246)


if __name__ == '__main__':
    unittest.main()
