# Python solution for 'Parse float' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS AND NUMBERS.
# Author: Jack Brokenshire
# Date: 01/08/2020

import unittest


def parse_float(string):
    """
    Takes a string and returns the float value, otherwise, None.
    :param string: a string value.
    :return: a number or None.
    """
    try:
        return float(string)
    except:
        return None


class TestParseFloat(unittest.TestCase):
    """Class to test 'parse_float' function"""

    def test_parse_float(self):
        ts = (
            ("1.0", 1.0),
            ("a", None),
            ("234.0234", 234.0234)
        )

        for t in ts:
            self.assertEqual(parse_float(t[0]), t[1])


if __name__ == "__main__":
    unittest.main()
