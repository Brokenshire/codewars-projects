# Python solution for 'Regex Password Validation' codewars question.
# Level: 5 kyu
# Tags: Fundamentals, Regular Expressions, Declarative Programming, Advanced Language Features, Strings,
#                     Validation, Algorithms, and Utilities.
# Author: Jack Brokenshire
# Date: 09/02/2020

import unittest


regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"


class TestRegex(unittest.TestCase):
    """Class to test 'regex'"""

    def test_regex(self):
        from re import search
        self.assertEqual(bool(search(regex, 'fjd3IR9')), True)
        self.assertEqual(bool(search(regex, 'ghdfj32')), False)
        self.assertEqual(bool(search(regex, 'DSJKHD23')), False)
        self.assertEqual(bool(search(regex, 'dsF43')), False)
        self.assertEqual(bool(search(regex, '4fdg5Fj3')), True)
        self.assertEqual(bool(search(regex, 'DHSJdhjsU')), False)
        self.assertEqual(bool(search(regex, 'fjd3IR9.;')), False)
        self.assertEqual(bool(search(regex, 'fjd3  IR9')), False)
        self.assertEqual(bool(search(regex, 'djI38D55')), True)
        self.assertEqual(bool(search(regex, 'a2.d412')), False)
        self.assertEqual(bool(search(regex, 'JHD5FJ53')), False)
        self.assertEqual(bool(search(regex, '!fdjn345')), False)
        self.assertEqual(bool(search(regex, 'jfkdfj3j')), False)
        self.assertEqual(bool(search(regex, '123')), False)
        self.assertEqual(bool(search(regex, 'abc')), False)
        self.assertEqual(bool(search(regex, '123abcABC')), True)
        self.assertEqual(bool(search(regex, 'ABC123abc')), True)
        self.assertEqual(bool(search(regex, 'Password123')), True)


if __name__ == '__main__':
    unittest.main()
