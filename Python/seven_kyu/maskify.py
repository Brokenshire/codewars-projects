# Python solution for "Credit Card Mask" codewars question.
# Level: 7 kyu
# Tags: Algorithms, Utilities, and Strings.
# Author: Jack Brokenshire
# Date: 23/03/2020

import unittest


def mask(cc):
    """
    Function mask, which changes all but the last four characters into '#'.
    :param cc: a string value.
    :return: a new string with only the last four characters shown.
    """
    return "".join([j if i < 4 else "#" for i, j in enumerate(cc[::-1])][::-1])


class TestMask(unittest.TestCase):
    """Class to test "mask" function"""

    def test_mask(self):
        self.assertEqual(mask(''), '')
        self.assertEqual(mask('123'), '123')
        self.assertEqual(mask('SF$SDfgsd2eA'), '########d2eA')
        self.assertEqual(mask("4556364607935616"), "############5616")
        self.assertEqual(mask("64607935616"), "#######5616")
        self.assertEqual(mask("1"), "1")
        self.assertEqual(mask(""), "")
        self.assertEqual(mask("Skippy"), "##ippy")
        self.assertEqual(mask("Nananananananananananananananana Batman!"), "####################################man!")


if __name__ == "__main__":
    unittest.main()
