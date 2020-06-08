# Python solution for 'CamelCase Method' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, FUNDAMENTALS, and STRINGS.
# Author: Jack Brokenshire
# Date: 08/06/2020

import unittest


def camel_case(string):
    """
    Capitalizes all words first letter without spaces.
    :param string: a string input of word(s).
    :return: All words first letters capitalized without spaces.
    """
    return "".join(x.capitalize() for x in string.split())


class TestCamelCase(unittest.TestCase):
    """Class to test 'camel_case' function"""

    def test_camel_case(self):
        self.assertEquals(camel_case("test case"), "TestCase")
        self.assertEquals(camel_case("camel case method"), "CamelCaseMethod")
        self.assertEquals(camel_case("say hello "), "SayHello")
        self.assertEquals(camel_case(" camel case word"), "CamelCaseWord")
        self.assertEquals(camel_case(""), "")


if __name__ == '__main__':
    unittest.main()
