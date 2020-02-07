# Python solution for 'Function 1 - hello world' codewars question.
# Level: 8 kyu
# Tags: Fundamentals, Functions, Control Flow, and Basic Language Features
# Author: Jack Brokenshire
# Date: 07/02/2020

import unittest


def greet():
    """
    Make a simple function called greet that returns the most-famous "hello world!".
    :return: 'hello world!'
    """
    return "hello world!"


class TestGreet(unittest.TestCase):
    """Class to test 'greet' function"""

    def test_greet(self):
        self.assertEqual(greet(), "hello world!")


if __name__ == '__main__':
    unittest.main()
