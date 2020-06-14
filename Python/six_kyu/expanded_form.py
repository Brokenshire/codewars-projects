# Python solution for 'Write Number in Expanded Form' codewars question.
# Level: 6 kyu
# Tags: FUNDAMENTALS, STRINGS, NUMBERS, MATHEMATICS, and ALGORITHMS.
# Author: Jack Brokenshire
# Date: 14/06/2020

import unittest


def expanded_form(num):
    """
    Expands an integer into ones, tens, hundreds, etc...
    :param num: an integer value.
    :return: a string of the integer in expanded form.
    """
    result = []
    divider = 10
    while divider < num:
        temp = num % divider
        if temp != 0:
            result.insert(0, str(temp))
        num -= temp
        divider *= 10
    result.insert(0, str(num))
    return " + ".join(result)


class TestExpandedForm(unittest.TestCase):
    """Class to test 'expanded_form' function"""

    def test_expanded_form(self):
        self.assertEquals(expanded_form(12), '10 + 2')
        self.assertEquals(expanded_form(42), '40 + 2')
        self.assertEquals(expanded_form(70304), '70000 + 300 + 4')


if __name__ == '__main__':
    unittest.main()
