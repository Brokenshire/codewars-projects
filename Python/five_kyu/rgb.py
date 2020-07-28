# Python solution for 'RGB To Hex Conversion' codewars question.
# Level: 5 kyu
# Tags: ALGORITHMS
# Author: Jack Brokenshire
# Date: 28/07/2020

import unittest


def rgb(r, g, b):
    """
    Converts RGB decimal values to hexadecimal.
    :param r: integer value.
    :param g: integer value.
    :param b: integer value.
    :return: hexadecimal version of RGB decimal numbers.
    """
    return "".join(["%02X" % max(0, min(x, 255)) for x in [r, g, b]])


class TestRGB(unittest.TestCase):
    """Class to test 'rgb' function"""

    def test_rgb(self):
        self.assertEqual(rgb(0, 0, 0), "000000", "testing zero values")
        self.assertEqual(rgb(1, 2, 3), "010203", "testing near zero values")
        self.assertEqual(rgb(255, 255, 255), "FFFFFF", "testing max values")
        self.assertEqual(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        self.assertEqual(rgb(-20, 275, 125), "00FF7D", "testing out of range values")


if __name__ == "__main__":
    unittest.main()
