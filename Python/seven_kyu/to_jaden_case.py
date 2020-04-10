# Python solution for 'Jaden Casing Strings' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Strings, and Arrays.
# Author: Jack Brokenshire
# Date: 17/02/2020

import unittest


def to_jaden_case(string):
    """
    Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from
    Jaden Smith, but they are not capitalized in the same way he originally typed them.
    :param string: A string value input.
    :return: A new string with each word in the sentence capitalized.
    """
    return " ".join(x.capitalize() for x in string.split())


class TestToJadenCase(unittest.TestCase):
    """Class to test 'to_jaden_case' function"""

    def test_name_list(self):
        quote = "How can mirrors be real if our eyes aren't real"
        self.assertEqual(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")


if __name__ == '__main__':
    unittest.main()
