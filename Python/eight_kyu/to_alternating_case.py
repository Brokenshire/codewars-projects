# Python solution for 'altERnaTIng cAsE <=> ALTerNAtiNG CaSe' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS.
# Author: Jack Brokenshire
# Date: 18/08/2020

import unittest


def to_alternating_case(string):
    """
    Changes each character to different casing.
    :param string: a string value.
    :return: a new string in alternating casing.
    """
    return "".join(string[i].lower() if string[i].isupper() else string[i].upper() for i in range(len(string)))


class TestToAlternatingCase(unittest.TestCase):
    """Class to test 'to_alternating_case' function"""

    def test_to_alternating_case(self):
        self.assertEqual(to_alternating_case("hello world"), "HELLO WORLD")
        self.assertEqual(to_alternating_case("HELLO WORLD"), "hello world")
        self.assertEqual(to_alternating_case("hello WORLD"), "HELLO world")
        self.assertEqual(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")
        self.assertEqual(to_alternating_case("12345"), "12345")
        self.assertEqual(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")
        self.assertEqual(to_alternating_case("String.prototype.toAlternatingCase"),
                           "sTRING.PROTOTYPE.TOaLTERNATINGcASE")
        self.assertEqual(to_alternating_case(to_alternating_case("Hello World")), "Hello World")
        title = "altERnaTIng cAsE"
        title = to_alternating_case(title)
        self.assertEqual(title, "ALTerNAtiNG CaSe")
        title = to_alternating_case(title)
        self.assertEqual(title, "altERnaTIng cAsE")
        title = to_alternating_case(title)
        self.assertEqual(title, "ALTerNAtiNG CaSe")
        title = to_alternating_case(title)
        self.assertEqual(title, "altERnaTIng cAsE")
        title = "altERnaTIng cAsE <=> ALTerNAtiNG CaSe"
        title = to_alternating_case(title)
        self.assertEqual(title, "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
        title = to_alternating_case(title)
        self.assertEqual(title, "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")
        title = to_alternating_case(title)
        self.assertEqual(title, "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
        title = to_alternating_case(title)
        self.assertEqual(title, "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")


if __name__ == "__main__":
    unittest.main()
