# Python solution for "Find the divisors!" codewars question.
# Level: 7 kyu
# Tags: ALGORITHMS, MATHEMATICS, and NUMBERS.
# Author: Jack Brokenshire
# Date: 02/04/2020

import unittest


def divisors(integer):
    """
    Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's
    divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string
    '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
    :param integer: a integer value.
    :return: a list of values which are divisors of an integer.
    """
    values = [x for x in range(2, integer) if integer % x == 0]
    return values if values else "{} is prime".format(integer)


class TestDivisors(unittest.TestCase):
    """Class to test "divisors" function"""

    def test_divisors(self):
        self.assertEqual(divisors(15), [3, 5])
        self.assertEqual(divisors(12), [2, 3, 4, 6])
        self.assertEqual(divisors(13), "13 is prime")


if __name__ == "__main__":
    unittest.main()
