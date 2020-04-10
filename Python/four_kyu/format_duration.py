# Python solution for 'Human readable duration format' codewars question.
# Level: 4 kyu
# Tags: Algorithms, Formats, Strings, Dates/Time, and Formatting.
# Author: Jack Brokenshire
# Date: 14/03/2020

import unittest

times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]


def format_duration(seconds):
    """
    The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is
    expressed as a combination of years, days, hours, minutes and seconds.
    :param seconds: an integer input.
    :return: the formatted version of the number of seconds, in human-friendly way.
    """
    if not seconds:
        return "now"
    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs


class TestFormatDuration(unittest.TestCase):
    """Class to test 'format_duration' function"""

    def test_format_duration(self):
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")


if __name__ == '__main__':
    unittest.main()
