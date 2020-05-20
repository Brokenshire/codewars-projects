# Python solution for 'Greet Me' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS and STRINGS.
# Author: Jack Brokenshire
# Date: 20/05/2020

import unittest


def greet(name):
    """
    Greets a person with their name capitalized.
    :param name: a string.
    :return: greets that name, capitalized and ends with an exclamation point.
    """
    return "Hello " + name.capitalize() + "!"


class TestGreet(unittest.TestCase):
    """Class to test 'greet' function"""

    def test_greet(self):
        self.assertEqual(greet('riley'), 'Hello Riley!')
        self.assertEqual(greet('molly'), "Hello Molly!")
        self.assertEqual(greet('BILLY'), "Hello Billy!")


if __name__ == '__main__':
    unittest.main()
