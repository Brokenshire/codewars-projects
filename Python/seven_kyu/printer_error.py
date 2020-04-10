# Python solution for "Printer Errors" codewars question.
# Level: 7 kyu
# Tags: Fundamentals
# Author: Jack Brokenshire
# Date: 25/03/2020

import unittest


def printer_error(s):
    """
    A printer error occurs when a character in the string is not within the range a to m.
    :param s: a string of letters.
    :return: The number of errors in the string compared to the total length.
    """
    return "{}/{}".format(sum(1 for x in s if x in"nopqrstuvwqyxz"), len(s))


class TestPrinterError(unittest.TestCase):
    """Class to test "printer_error" function"""

    def test_printer_error(self):
        self.assertEqual(printer_error("aaabbbbhaijjjm"), "0/14")
        self.assertEqual(printer_error("aaaxbbbbyyhwawiwjjjwwm"), "8/22")
        self.assertEqual(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "3/56")


if __name__ == "__main__":
    unittest.main()
