# Python solution for 'Convert boolean values to strings 'Yes' or 'No'.' codewars question.
# Level: 8 kyu
# Tags: FUNDAMENTALS, BOOLEAN, and SBEST PRACTICES.
# Author: Jack Brokenshire
# Date: 01/05/2020

import unittest


def bool_to_word(boolean):
    """
    Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
    :param boolean: boolean variable.
    :return: Yes if true, otherwise, No.
    """
    return "Yes" if boolean else "No"


class TestBoolToWord(unittest.TestCase):
    """Class to test 'bool_to_word' function"""

    def test_bool_to_word(self):
        self.assertEqual(bool_to_word(True), 'Yes')
        self.assertEqual(bool_to_word(False), 'No')


if __name__ == '__main__':
    unittest.main()
