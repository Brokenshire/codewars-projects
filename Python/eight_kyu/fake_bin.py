# Python solution for 'Fake Binary' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, STRINGS, and ARRAYS.
# Author: Jack Brokenshire
# Date: 13/07/2020

import unittest


def fake_bin(x):
    """
    Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
    :param x: sting of digits.
    :return: the resulting string.
    """
    return "".join("0" if int(i) < 5 else "1" for i in str(x))


class TestFakeBin(unittest.TestCase):
    """Class to test 'fake_bin' function"""

    def test_fake_bin(self):
        tests = [
            # [expected, input]
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]

        for exp, inp in tests:
            self.assertEqual(fake_bin(inp), exp)


if __name__ == '__main__':
    unittest.main()
