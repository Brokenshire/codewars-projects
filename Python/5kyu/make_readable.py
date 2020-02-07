# Python solution for 'Human Readable Time' codewars question.
# Level: 5 kyu
# Tags: Algorithms, Date/Time, Mathematics, and Numbers
# Author: Jack Brokenshire
# Date: 07/02/2020

import unittest


def make_readable(seconds):
    """
    Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable
    format (HH:MM:SS)
        HH = hours, padded to 2 digits, range: 00 - 99
        MM = minutes, padded to 2 digits, range: 00 - 59
        SS = seconds, padded to 2 digits, range: 00 - 59
    The maximum time never exceeds 359999 (99:59:59)
    :param seconds: non-negative integer.
    :return: the time in a human-readable format (HH:MM:SS)
    """
    hours = seconds // 3600
    mins = (seconds // 60) % 60
    secs = seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)


class TestRomanNum(unittest.TestCase):
    """Class to test 'roman_num' function"""

    def test_roman_num(self):
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(5), "00:00:05")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")


if __name__ == '__main__':
    unittest.main()
