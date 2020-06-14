# Python solution for 'Say hello!' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 14/06/2020

import unittest


def greet(name):
    """
    Greets a person.
    :param name: a string input.
    :return: None if string empty or None else greets the name.
    """
    if name == "" or name is None:
        return None
    else:
        return "hello " + name + "!"


class TestGreet(unittest.TestCase):
    """Class to test 'greet' function"""

    def test_greet(self):
        self.assertEquals(greet("Niks"), "hello Niks!", "didn't work for 'Niks'")
        self.assertEquals(greet("Nick"), "hello Nick!", "didn't work for 'Nick'")
        self.assertEquals(greet(""), None, "didn't work for empty string")
        self.assertEquals(greet(None), None, "didn't work for None")


if __name__ == '__main__':
    unittest.main()
