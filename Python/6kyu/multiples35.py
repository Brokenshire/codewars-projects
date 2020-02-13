# Python solution for 'Multiples of 3 or 5' codewars question.
# Level: 6 kyu
# Tags: Algorithms, Numbers, Integers, Parsing, and Strings.
# Author: Jack Brokenshire
# Date: 13/02/2020

import unittest


def multiples35(number):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    multiples is 23. Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number
    passed in. Note: If the number is a multiple of both 3 and 5, only count it once.
    :param number: An integer value.
    :return: The sum of all the multiples of 3 or 5 below the number passed in.
    """
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


class TestMultiples35(unittest.TestCase):
    """Class to test 'multiples35' function"""

    def test_multiples35(self):
        self.assertEqual(multiples35(10), 23)


if __name__ == '__main__':
    unittest.main()
