# Python solution for 'Odd or Even?' codewars question.
# Level: 7 kyu
# Tags: Fundamentals, Arithmetic, Mathematics, Algorithms, Numbers, and Arrays.
# Author: Jack Brokenshire
# Date: 15/02/2020

import unittest


def odd_or_even(arr):
    """
    Given a list of numbers, determine whether the sum of its elements is odd or even. Give your answer as a string
    matching "odd" or "even". If the input array is empty consider it as: [0] (array with a zero).
    :param arr: A list of numbers.
    :return: 'even' if the sum of the numbers in the list is even, otherwise 'odd'.
    """
    return "even" if sum(arr) % 2 == 0 else "odd"


class TestOddOrEven(unittest.TestCase):
    """Class to test 'odd_or_even' function"""

    def test_odd_or_even(self):
        self.assertEqual(odd_or_even([0, 1, 2]), "odd")
        self.assertEqual(odd_or_even([0, 1, 3]), "even")
        self.assertEqual(odd_or_even([1023, 1, 2]), "even")


if __name__ == '__main__':
    unittest.main()
