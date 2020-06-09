# Python solution for 'Convert string to camel case' codewars question.
# Level: 6 kyu
# Tags: ALGORITHMS, REGULAR EXPRESSIONS, DECLARATIVE PROGRAMMING, ADVANCED LANGUAGE FEATURES. FUNDAMENTALS, and STRINGS.
# Author: Jack Brokenshire
# Date: 10/06/2020

import unittest


def to_camel_case(text):
    """
    Converts dash/underscore delimited words into camel casing.
    :param text: a string of words with '-' and '_' as spaces.
    :return: the string as camel case.
    """
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])


class TestToCamelCase(unittest.TestCase):
    """Class to test 'to_camel_case' function"""

    def test_to_camel_case(self):
        self.assertEquals(to_camel_case(''), '', "An empty string was provided but not returned")
        self.assertEquals(to_camel_case("the_stealth_warrior"), "theStealthWarrior",
                          "to_camel_case('the_stealth_warrior') did not return correct value")
        self.assertEquals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior",
                          "to_camel_case('The-Stealth-Warrior') did not return correct value")
        self.assertEquals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")


if __name__ == '__main__':
    unittest.main()
