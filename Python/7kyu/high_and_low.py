# Python solution for 'Highest and Lowest' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, and Strings
# Author: Jack Brokenshire
# Date: 10/02/2020

import unittest


def high_and_low(numbers):
    """
    In this little assignment you are given a string of space separated numbers, and have to return the highest and
    lowest number. All numbers are valid Int32, no need to validate them. There will always be at least one number in
    the input string. Output string must be two numbers separated by a single space, and highest number is first.
    :param numbers: A input string with numbers separated by spaces.
    :return: The highest and lowest numbers within the string of numbers separated by a space.
    """
    nums = [int(x) for x in numbers.split(" ")]
    return "{} {}".format(max(nums), min(nums))


class TestHighAndLow(unittest.TestCase):
    """Class to test 'high_and_low' function"""

    def test_high_and_low(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");


if __name__ == '__main__':
    unittest.main()
