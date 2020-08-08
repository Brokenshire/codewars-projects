# Python solution for 'Returning Strings' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS AND STRINGS.
# Author: Jack Brokenshire
# Date: 08/08/2020

import unittest


def greet(name):
    """ Make a function that will return a greeting statement that uses an input.

    Args:
        name (str): a persons name.

    Returns:
        str: "Hello, <name> how are you doing today?".
    """
    return "Hello, {} how are you doing today?".format(name)


class TestGreet(unittest.TestCase):
    """Class to test 'greet' function"""

    def test_greet(self):
        self.assertEqual(greet('Ryan'), "Hello, Ryan how are you doing today?")


if __name__ == "__main__":
    unittest.main()