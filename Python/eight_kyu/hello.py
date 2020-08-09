# Python solution for 'Hello, Name or World!' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 09/08/2020

import unittest


def hello(name=None):
    """Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

    Args:
        name (str): A persons name.

    Returns:
        str: "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).
    """
    return "Hello, World!" if name is None or not name else "Hello, {}!".format(name.title())


class TestHello(unittest.TestCase):
    """Class to test 'hello' function"""

    def test_hello(self):
        tests = (
            ("John", "Hello, John!"),
            ("aLIce", "Hello, Alice!"),
            ("", "Hello, World!"),
        )

        for inp, exp in tests:
            self.assertEqual(hello(inp), exp)

        self.assertEqual(hello(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
