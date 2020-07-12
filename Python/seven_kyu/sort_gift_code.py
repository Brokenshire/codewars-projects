# Python solution for 'Sort the Gift Code' codewars question.
# Level: 7 kyu
# Tags: FUNDAMENTALS, HACKING HOLIDAYS, SORTING, ALGORITHMS, and STRINGS.
# Author: Jack Brokenshire
# Date: 12/07/2020

import unittest


def sort_gift_code(code):
    """
    Sorts a string in alphabetical order.
    :param code: a string containing up to 26 unique alphabetical characters.
    :return: a string containing the same characters in alphabetical order.
    """
    return "".join(sorted(code))


class TestSortGiftCode(unittest.TestCase):
    """Class to test 'sort_gift_code' function"""

    def test_sort_gift_code(self):
        self.assertEqual(sort_gift_code('abcdef'), 'abcdef')
        self.assertEqual(sort_gift_code('pqksuvy'), 'kpqsuvy')
        self.assertEqual(sort_gift_code('zyxwvutsrqponmlkjihgfedcba'), 'abcdefghijklmnopqrstuvwxyz')


if __name__ == '__main__':
    unittest.main()
