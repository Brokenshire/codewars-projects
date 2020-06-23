# Python solution for 'WeIrD StRiNg CaSe' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, UTILITIES, and STRINGS.
# Author: Jack Brokenshire
# Date: 23/06/2020

import unittest


def to_weird_case(string):
    """
    Transforms a string into weird case.
    :param string: a string of words.
    :return: the same string with all even indexed characters in each word upper cased, and all odd indexed characters
             in each word lower cased.
    """
    final = []
    for x in string.split():
        result = ""
        for i, j in enumerate(x):
            if i % 2:
                result += j.lower()
            else:
                result += j.upper()
        final.append(result)
    return " ".join(final)


class TestToWeirdCase(unittest.TestCase):
    """Class to test 'to_weird_case' function"""

    def test_to_weird_case(self):
        self.assertEqual(to_weird_case('This'), 'ThIs')
        self.assertEqual(to_weird_case('is'), 'Is')
        self.assertEqual(to_weird_case('This is a test'), 'ThIs Is A TeSt')


if __name__ == '__main__':
    unittest.main()
