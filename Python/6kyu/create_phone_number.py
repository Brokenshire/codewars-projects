# Python solution for 'Create Phone Number' codewars question.
# Level: 6 kyu
# Tags: Algorithms, Arrays, Strings, Loops, Control Flow, Basic Language Features, Fundamentals, Formatting,
#       Regular Expressions, Declarative Programming, and Advanced Language Features.
# Author: Jack Brokenshire
# Date: 12/02/2020

import unittest


def create_phone_number(n):
    """
    Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers
    in the form of a phone number. The returned format must be correct in order to complete this challenge.
    Don't forget the space after the closing parentheses!
    :param n: An input array of integers.
    :return: A string of those numbers in the array in phone number form.
    """
    return "({}) {}-{}".format("".join(map(str, n[0:3])), "".join(map(str, n[3:6])), "".join(map(str, n[6:])))


class TestCreatePhoneNumber(unittest.TestCase):
    """Class to test 'create_phone_number' function"""

    def test_create_phone_number(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")


if __name__ == '__main__':
    unittest.main()
