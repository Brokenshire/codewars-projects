# Python solution for 'Grasshopper - Debug sayHello' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 02/08/2020

import unittest


def say_hello(name):
    """
    The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard.
    It is your job to fix the code and get the program working again!
    :param name: A string value.
    :return: A greeting to the person.
    """
    return "Hello, " + name


class TestSayHello(unittest.TestCase):
    """Class to test 'say_hello' function"""

    def test_say_hello(self):
        self.assertEqual(say_hello('Mr. Spock'), 'Hello, Mr. Spock')
        self.assertEqual(say_hello('Captain Kirk'), 'Hello, Captain Kirk')
        self.assertEqual(say_hello('Liutenant Uhura'), 'Hello, Liutenant Uhura')
        self.assertEqual(say_hello('Dr. McCoy'), 'Hello, Dr. McCoy')
        self.assertEqual(say_hello('Mr. Scott'), 'Hello, Mr. Scott')


if __name__ == "__main__":
    unittest.main()
