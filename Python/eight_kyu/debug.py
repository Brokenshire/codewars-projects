# Python solution for 'Grasshopper - Function syntax debugging' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 10/08/2020

import unittest


def main(verb, noun):
    """A student was working on a function and made some syntax mistakes while coding. Help them find their mistakes and fix them.

    Args:
        verb (str): A verb string.
        noun (str): A noun string.

    Returns:
        str: The concatenation of the verb plus noun.
    """
    return verb + noun


class TestMain(unittest.TestCase):
    """Class to test 'main' function"""

    def test_main(self):
        self.assertEqual(main('take ', 'item'), 'take item')
        self.assertEqual(main('use ', 'sword'), 'use sword')


if __name__ == "__main__":
    unittest.main()
