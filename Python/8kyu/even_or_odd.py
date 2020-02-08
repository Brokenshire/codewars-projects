# Python solution for 'Even or Odd' codewars question.
# Level: 8 kyu
# Tags: Fundamentals, Mathematics, Algorithms, and Numbers
# Author: Jack Brokenshire
# Date: 08/02/2020

import unittest


def even_or_odd(number):
    """
    Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for
    even numbers or "Odd" for odd numbers.
    :param number: a positive integer value.
    :return: return 'Even' when the input value is even, otherwise return 'Odd'.
    """
    if number % 2 == 0:
        return "Even"
    return "Odd"


class TestEvenOrOdd(unittest.TestCase):
    """Class to test 'even_or_odd' function"""

    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(2) == "Even")
        self.assertEqual(even_or_odd(0) == "Even")
        self.assertEqual(even_or_odd(7) == "Odd")
        self.assertEqual(even_or_odd(1) == "Odd")
        self.assertEqual(even_or_odd(-1) == "Odd")


if __name__ == '__main__':
    unittest.main()
